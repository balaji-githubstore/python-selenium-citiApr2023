*** Settings ***
Library     SeleniumLibrary
Resource    ../resource/base.resource

Test Setup   Launch Browser
Test Teardown   Close Browser

*** Test Cases ***
TC1 Valid Login
    Input Text    id=authUser    physician
    Input Password    id=clearPass    physician
    Select From List By Label    xpath=//select[@name='languageChoice']     English (Indian)
    Click Element    css=#login-button
    Title Should Be    OpenEMR

