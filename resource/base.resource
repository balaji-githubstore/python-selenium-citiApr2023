*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${BROWSER_NAME}     chrome
${URL}      https://demo.openemr.io/b/openemr/

*** Keywords ***
Launch Browser
    Open Browser    browser=${BROWSER_NAME}
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=${URL}