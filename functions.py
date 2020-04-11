# Open file for reading in text mode (default mode)
import re
import difflib
import docx2txt
from difflib import SequenceMatcher

def pCheck(file1_data,file2_data):
    similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    return int(similarity_ratio * 100)

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def efrainspChecker(file1_data,file2_data):
    #for testing purposes
    #print("The following is part of the fuzz implementation:")
    #print(fuzz.ratio(file1_data,file2_data))
    #print(fuzz.partial_ratio(file1_data,file2_data))
    return fuzz.partial_ratio(file1_data,file2_data)

def read_report(file_one,file_two):
    if (file_one != None and file_two != None):
        with open(file_one,'r') as file1:
            with open(file_two,'r') as file2:
                if file_one[-3:] == "ocx":
                    content = docx2txt.process(file_one)
                    content2 = docx2txt.process(file_two)
                    same = set(content).intersection(content2)
                elif file_one[-3:] == "txt":
                    same = set(file1).intersection(file2)

        same.discard('\n')
        with open('report.txt','w') as file_out:
            for line in same:
                file_out.write(line)
