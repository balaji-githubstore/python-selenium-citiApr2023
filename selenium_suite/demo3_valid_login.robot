*** Settings ***
Documentation       This helps to understand test template concepts
Library     SeleniumLibrary
Resource    ../resource/base.resource

Test Setup   Launch Browser
Test Teardown   Close Browser

Test Template   Valid Login Template

*** Test Cases ***
TC1_Valid_Login    admin   pass    English (Indian)    OpenEMR
TC2     physician   physician   English (Indian)    OpenEMR


*** Keywords ***
Valid Login Template
    [Arguments]     ${username}     ${password}     ${language}     ${expected_title}
    Input Text    id=authUser    ${username}
    Input Password    id=clearPass    ${password}
    Select From List By Label    xpath=//select[@name='languageChoice']     ${language}
    Click Element    css=#login-button
    Title Should Be    ${expected_title}
