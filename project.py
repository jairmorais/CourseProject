import spacy
import os
import fitz
import sys

def Similarity(VideoPath, pdfFile):

    videoText = [] #Video text content
    VideoContentPath = VideoPath
    i = 0
    for filename in os.listdir(VideoContentPath):
        with open(os.path.join(VideoContentPath, filename), 'r') as f:
            videoText.append(f.read())
            i=i+1

    pdfPath = pdfFile
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

  
    

if __name__ == "__main__":
    arg = sys.argv[1:]
    print(arg[0])
    print(arg[1])
    Similarity(str(arg[0]), str(arg[1]))