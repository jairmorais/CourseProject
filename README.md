# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.

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
