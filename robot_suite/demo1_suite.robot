*** Settings ***
Library     DateTime
Library    String

*** Test Cases ***
TC1
    Log To Console  message=Balaji Dinakaran

TC2
    Log To Console    welcome to robot session
    
TC3
    ${my_name}  Set Variable    balaji
    Log To Console    ${my_name}
    Log     ${my_name}
    ${my_name}      Convert To Upper Case   ${my_name}
     Log     ${my_name}

TC4
    ${radius}   Set Variable    20
    ${result}   Evaluate    3.14*${radius}*${radius}    
    Log    ${result}

TC5
    ${date}=     Get Current Date
    Log To Console    ${date}

