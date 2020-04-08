# Open file for reading in text mode (default mode)
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
