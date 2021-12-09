# Course Project
Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.

# Final Report
Theme 2: Intelligent Learning Platform

## Installation
  #### pip install spacy
  #### python -m spacy download en_core_web_sm
  #### python -m pip install --upgrade pymupdf
  This will be used for the similarity between two documents.

## Execution 
  ### After Installation - Run the command line
  C:\python project.py [Video Content text files folder] [pdf file] >output.txt 
  ### Example
   python project.py C:\cs410\FinalProject\Videos C:\cs410\FinalProject\Book\MITEI-The-Future-of-the-Electric-Grid.pdf > output.txt
  ### Result
  The result will be on the text file : output.txt

## Video Lecture Content and Text Book Document 
  Each video content is a text document and it will be calculate the similarity with each page from the Textbook
  The Result is the closed the Video content are from the page they are related, using that we can relate the age with each page.
## The Result
  The Final result is the list of videos content and the pages that content are related
  Video 1 - related to page 1,2, 5,10
  Video 2 - related to page 3,4,11
  #### Result is on 
## Workload
#### It page of pdf was converted to a documento using pymupdf and put in a array of documents - 4hr
#### It is necessary to get each video content to was transcript to a text file -6hr
#### It was implemented the similarity function using spacy (Package that calculate the similarity of documents) - 12hr
#### In the code there are a cut on 0.7 on the similarity.


# Project Proposal
Theme 2: Intelligent Learning Platform

## Team Members 
Jair Vieira Morais Filho - jairv2@illinois.edu - captain of the team

## Topic : Integration of the lecture videos with the content of the textbook to enable convenient switching between the two.
It would be interesting to have the videos topics interact with the textbook. The textbook has more deep information than the video lectures, so for someone that wants to have a broad view of the subject, he would search in the textbook the information. The same for the text book, it would allow someone relate the information present on the text book to video content.

## Datasets, Algorithms or Techniques
Each video has vocabulary list, list of documents is the pages of the textbook (each document is a page). We have to run text retrieve PLSA for each video vocabulary list present in each video. 
(Lecture 1)-Video 1- List of vocabulary run over the list of pages(documents) and find the pages with more probability to be in the video 1 topic.

## Programming Language - Solution
It will use Python.
It will use the textbook pdf split each page. 
Get the list of videos for each video content.

## Workload
#### It will be necessary for convert the textbook to a table where each row is a page - 4hr
#### It is necessary to get each video content to generate the list of vocabulary for each video -4hr
#### Implement PLSA model for this proposal - 12hr

## Final Result
The result will be a table with (video 1) is also in page 1,3 4


  
