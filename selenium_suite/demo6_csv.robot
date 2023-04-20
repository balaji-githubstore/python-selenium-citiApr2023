*** Settings ***
Documentation       This helps to understand test template concepts
Library     SeleniumLibrary
Resource    ../resource/base.resource
Resource    ../resource/pages/LoginPage.resource

Library     DataDriver      file=../test_data/valid_login.csv

Test Setup   Launch Browser
Test Teardown   Close Browser

Test Template   Valid Login Template

*** Test Cases ***
TC1

*** Keywords ***
Valid Login Template
    [Arguments]     ${username}     ${password}     ${language}     ${expected_title}
    Enter Username  ${username}
    Enter Password    ${password}
    Select Language     ${language}
    Click Login
    Title Should Be    ${expected_title}
