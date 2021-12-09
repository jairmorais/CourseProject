pip install spacy
python -m spacy download en_core_web_sm
python -m pip install --upgrade pymupdf
@echo off
python project.py %1 %2 > output.txt 
 