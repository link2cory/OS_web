from pytest_bdd import scenarios, parsers, given, when, then

import pytest

import requests

scenarios('../features/api_get.feature')

EXTRA_TYPES = {
    'Number': int,
}

@given('the activity api is queried with no params')
def response(docker_web):
  return requests.get(docker_web)

@given('there is an activity record in the database')
def activity_record(docker_web):
    activity_record = {'name': 'testing'}
    # create a record by POSTing to the endpoint
    requests.post(docker_web, activity_record)

    return activity_record

@then(parsers.parse('the response status code is "{code:Number}"', extra_types=EXTRA_TYPES))
def response_code(response, code):
  assert response.status_code == code

@then('the response contains the aforementioned activity record')
def response_content(response, activity_record):    
    record_found = False

    # check if there is a record contained in the response that has the same
    # data as the activity_record passed
    for response_record in response.json():
        print(response_record)
        print(activity_record)
        # the response record will have extra fields so check for subset 
        # rather than equivalence
        if response_record.items() >= activity_record.items():
            record_found = True
            break
    assert record_found

