*** Settings ***
Library     SeleniumLibrary
Resource    ../resource/base.resource

*** Test Cases ***
TC1 Valid Login
    Launch Browser
    Input Text    id=authUser    admin
    Input Password    id=clearPass    pass
    Select From List By Label    xpath=//select[@name='languageChoice']     English (Indian)
    Click Element    css=#login-button
    Title Should Be    OpenEMR
