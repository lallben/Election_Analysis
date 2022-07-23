# Election_Analysis
This project utilised Python for data analytics specifically to disscet and extract information from data related to an election.
## Project Overview
Tom, a Colorado Board of Election employee, has asked for assitance in audting the results of the elections in a US Congressional Prescint in Colorado. He is looking for assistance with regards to two specific areas:
### Tabulation of the results
- Total # of Votes cast in the election
- The total votes received by each candidate
- The percentage of votes received by each candidate
- Identification of the Winner of the election based on the popular vote
### Investigate the possibilty of Automation
Tom wants to know if there is a way by which the process can be automated for use by utilising programming in Python rather than use the normal route of Excel as has been done in the past. The code developed to audit the Colorado elections, if successful, can then possibly be utilised by other Congressional, Senatorial Districts as well as Local Elections.
## Sources of Information/Resources used
- Python version 3.7.6
- VisualStudio Code v 1.69.2
- Data source: election_results.csv (with data recieved through Mail In Ballots; Punch Cards; DRE Voting Machines)
## Election Audit Results
### Overall Results:
![Overall results](https://github.com/lallben/Election_Analysis/blob/main/screenshot_text%20file_results_1.png)<br>
### Candidate Results:
![Candidate results](https://github.com/lallben/Election_Analysis/blob/main/screenshot_text%20file_results_3.png)<br>
### County Results:
![County results](https://github.com/lallben/Election_Analysis/blob/main/screenshot_text%20file_results_2.png)<br>
### Overview of Results
![Summary results](https://github.com/lallben/Election_Analysis/blob/main/screenshot_text%20file_results.png)<br>
### Access to Files
The code to produce the audit and the results was developed in Python which can be accessed [here](https://github.com/lallben/Election_Analysis/blob/main/PyPoll.py).<br>
The results of the code are written to a [text file](https://github.com/lallben/Election_Analysis/blob/main/Analysis/election_analysis.txt)<br>
## Election Audit Summary
As a result of this exercise it is evident that the code that has been developed can be utilised for auditing elections at the Congressional, Senatorial and/or Local level. The code would be a valuable asset to create efficiencies i.e reduce time taken to produce the results as well as increase the reliability on the results.<br>
The script can include the specific Congressional/Senatorial/Local election that is being audited. Currently the results are displayed in a generic fashion with the only distinguishing feature being the counties. This could be achieved via inviting an Input from the user for the particular result.<br>
In order to make the process fully automated there would need to be an input for the name of the file from which the data is being accessed from as well as a user inout for the name of file to which the results are to be written. There is a good chance that the files would not have the same name across the various jurisdictions, which would also be imparctical from tracking purposes. 
There is room to enhance the utility of the script which could include the tracking of the votes submitted by Mail in Ballots; Punch Cards & DRE Voting machines. if the original data includes the source of the vote, this would help the Election Commission get a really good idea as to the medium being used by the public to cast their votes.
