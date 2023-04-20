*** Settings ***
Library     demo1.py

*** Keywords ***
Subtract Number
    [Arguments]     ${a}     ${b}
    ${res}      Evaluate    ${a}-${b}
    [Return]    ${res}

*** Test Cases ***
TC1
    ${res}  Add Number    10    10
    Log To Console    ${res}
    
TC2
    ${result}   Subtract Number    4    2
    Log To Console    ${result}