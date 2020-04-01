# Open file for reading in text mode (default mode)
from difflib import SequenceMatcher

def pCheck(file1_data,file2_data):
    similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    return int(similarity_ratio * 100)
