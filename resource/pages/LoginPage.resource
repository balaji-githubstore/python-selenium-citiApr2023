*** Settings ***
Resource    ../base.resource

*** Variables ***
${USERNAME_LOCATOR}     id=authUser
${PASSWORD_LOCATOR}     id=clearPass
${LOGIN_LOCATOR}        css=#login-button
${LANGUAGE_LOCATOR}     xpath=//select[@name='languageChoice']

*** Keywords ***
Enter Username
    [Arguments]     ${username}
    Input Text    ${USERNAME_LOCATOR}    ${username}

Enter Password
    [Arguments]     ${password}
    Input Password    ${PASSWORD_LOCATOR}    ${password}

Select Language
    [Arguments]     ${language}
    Select From List By Label    ${LANGUAGE_LOCATOR}     ${language}

Click Login
    Click Element    ${LOGIN_LOCATOR}
