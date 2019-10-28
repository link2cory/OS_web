from pytest_bdd import scenario, parsers, given, when, then

import pytest

import requests

response = requests.Response()

@scenario('../features/endpoint.feature', 'Simple get request')
def test_get():
  pass

@given('the activity api is queried with no params')
def response(docker_web):
  print(docker_web)
  response = requests.get(docker_web)
  return response

@when('I send a get request to the activity endpoint')
def get():
  response = requests.get('http://localhost:5000/api/activity')

@then('the response status code is 200')
def response_code(response):
  assert response.status_code == 200
