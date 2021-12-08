import spacy
import os
import fitz


videoText = [] #Video text content
VideoContentPath = "C:\cs410\FinalProject\Videos"
i = 0
for filename in os.listdir(VideoContentPath):
   with open(os.path.join(VideoContentPath, filename), 'r') as f:
       videoText.append(f.read())
       i=i+1

pdfPath = "C:\cs410\FinalProject\EBook\MITEI-The-Future-of-the-Electric-Grid.pdf"
pdfPage = []
with fitz.open(pdfPath) as doc:
    for page in doc:
        pdfPage.append(page.getText())
        
      

nlp = spacy.load('en_core_web_sm')
i=0
j=0
for video in videoText:
    v = nlp(video)
    for pg in pdfPage:
        p = nlp(pg)
        s = v.similarity(p)
        if s > 0.7 :
            print ("Video ("+str(i+1)+") "+" similarity with page -("+ str(j+1) +") "+ str(s))
        j=j+1
    i=i+1

