*** Settings ***
Documentation       This helps to understand test template concepts with excel
Library     SeleniumLibrary
Resource    ../resource/base.resource

Library     DataDriver      file=../test_data/open_emr_data.xlsx       sheet_name=ValidLogin

Test Setup   Launch Browser
Test Teardown   Close Browser

Test Template   Valid Login Template

*** Test Cases ***
TC1


*** Keywords ***
Valid Login Template
    [Arguments]     ${username}     ${password}     ${language}     ${expected_title}
    Input Text    id=authUser    ${username}
    Input Password    id=clearPass    ${password}
    Select From List By Label    xpath=//select[@name='languageChoice']     ${language}
    Click Element    css=#login-button
    Title Should Be    ${expected_title}
