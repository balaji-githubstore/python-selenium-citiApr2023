@patient
Feature: Patient
  In order to manage patient records
  As an admin
  I would like to add,edit,delete patients details

  @addpatient
  Scenario: Add Valid Patient
    Given I have browser with openemr page
    When I enter username as "admin"
    And I enter password as "pass"
    And I select language as "English (Indian)"
    And I click on login
    And I click on patient menu
    And I click on new-search menu
    And I fill the patient record who
      | firstname | lastname | gender   | dob   |
      | <fname>   | <lname>  | <gender> | <dob> |
    Then the alert message should contatin "Tobacco"