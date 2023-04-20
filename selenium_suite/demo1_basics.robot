*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC1
    Open Browser     browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=http://facebook.com
    Input Text    id:email    hello123@gmail.com
    Input Password    id=pass    wleomce123
    Click Element    name=login

TC2
    Open Browser     browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=http://facebook.com
    Element Text Should Be    xpath=//h2    Facebook helps you connect and share with the people in your life.
    Element Should Contain    xpath=//h2    Facebook helps you connect


#fb signup