Feature: Activity Endpoint
  as a client,
  I want to receive information about activities I have posted
  So that I can keep track of how I am spending my time

  Scenario: Simple get request
    Given the activity api is queried with no params
    #And there is some activity data in the database
    Then the response status code is 200
    #    And I receive a copy of the data in the database
