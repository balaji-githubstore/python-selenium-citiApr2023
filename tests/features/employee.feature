Feature: Patient
  In order to manage patient records
  As an admin
  I would like to add,edit,delete patients details

  @fb
  Scenario: Add Valid Patient
    Given I have browser with fb page
    When I click on create new patient
    And I fill the registration form
      | firstname | lastname | mobile_number | gender |
      | john      | wick     | 899889        | Custom |
    Then I should see succesful message as "registered"

  @fb2
  Scenario Outline: Add Valid Patient2
    Given I have browser with fb page
    When I click on create new patient
    And I fill the registration form
      | firstname | lastname | mobile_number | gender   |
      | <fname>   | <lname>  | <mobile>      | <gender> |
    Then I should see succesful message as "registered"
    Examples:
      | fname | lname | mobile | gender |
      | john  | wick  | 8899   | Male   |
      | peter | ke    | 777    | Custom |