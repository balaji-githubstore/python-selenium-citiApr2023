*** Settings ***
Library     demo1.py

*** Test Cases ***
TC1
    ${res}  Add Number    10    10
    Log To Console    ${res}