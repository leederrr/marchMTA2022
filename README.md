# March 2022 MTA Turnstile Useage
## Overview
Analysis of the MTA turnstile data from March 2022 with a Python script. The turnstile dataset was provided publicly by the MTA, which includes multiple text files divided by data per week. The month of March 2022 was chosen since NYC had lifted many COVID-19 protocols, and there could potentially be a change in pandemic habits including more transit riders. This was a personal project for an introductory computer science class completed in May 2022.
## Code Files
**MarchMTANYC.txt** 
> Text file that contains the cleaned out data of about 50 different subway stations around NYC. Includes the starting time and the ending time of the last recorded turnstile counts. Data originally contained records from the whole day at different hours. The data was cleaned so that the counts for just the day of entries and exits of a specific turnstile would be calculated in the Python script.
> 
**TurnstileDataScript.py**
> Python script that does the calculations for the total entries and exits of a turnstile based on user inputs of the station name and the date desired.
>
> ## References
