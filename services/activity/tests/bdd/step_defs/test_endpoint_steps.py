from pytest_bdd import scenarios, parsers, given, when, then

import pytest

import requests

scenarios('../features/endpoint.feature')

EXTRA_TYPES = {
    'Number': int,
}

@given('the activity api is queried with no params')
def response(docker_web):
  return requests.get(docker_web)

@then(parsers.parse('the response status code is "{code:Number}"', extra_types=EXTRA_TYPES))
def response_code(response, code):
  assert response.status_code == code
