Feature: Login
  In order to manage the health records
  As a user
  I want to access the OpenEMR portal


#  Scenario: Valid Login
#    Given I have browser with openemr page
#    When I enter username as "admin"
#    And I enter password as "pass"
#    And I select language as "English (Indian)"
#    And I click on login
#    Then I should get access to portal with title as "OpenEMR"

  @valid
  Scenario Outline: Valid Login
    Given I have browser with openemr page
    When I enter username as "<username>"
    And I enter password as "<password>"
    And I select language as "<language>"
    And I click on login
    Then I should get access to portal with title as 'OpenEMR'

    Examples:
      | username   | password   | language         |
      | physician  | physician  | English (Indian) |
      | admin      | pass       | English (Indian) |
      | accountant | accountant | English (Indian) |