*** Settings ***
Library        Selenium2Library
*** Test Cases ***
Open Google
  Navigate To Google
  Verify Page Contains Google
*** Keywords ***
Navigate To Google
  Open Browser   https://www.google.fi   browser=chrome
Verify Page Contains Google
  ${Get_title}=      Get Title
  Should Be Equal As Strings     ${Get_title}   Google
  Close Browser