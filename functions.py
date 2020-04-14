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

# def read_report(file_one,file_two):
#     if (file_one != None and file_two != None):
#         with open(file_one,'r') as file1:
#             with open(file_two,'r') as file2:
#                 if file_one[-3:] == "ocx":
#                     content = docx2txt.process(file_one)
#                     content2 = docx2txt.process(file_two)
#                     same = set(content).intersection(content2)
#                 elif file_one[-3:] == "txt":
#                     same = set(file1).intersection(file2)
#
#         same.discard('\n')
#         with open('report.txt','w') as file_out:
#             for line in same:
#                 file_out.write(line)
def read_report(file_one,file_two):
    if (file_one != None and file_two != None):
        # with open(file_one,'r') as file1:
        #     with open(file_two,'r') as file2:
        if file_one[-3:] == "ocx":
            list1 = docx2txt.process(file_one)
            list2 = docx2txt.process(file_two)
                    #same = set(content).intersection(content2)
                #elif file_one[-3:] == "txt":
                    #same = set(file1).intersection(file2)
        else:
            list1 = open(file_one).readlines()
            list2 = open(file_two).readlines()

        file3 = open('report.txt', 'w')
        for i in list1:
            for j in list2:
                if i == j:
                    file3.write(i)

def highlight(text,seq):
    # get string to look for (if empty, no searching)
    #s = "document has stayed the"
    s = seq
    if s:
        # start from the beginning (and when we come to the end, stop)
        idx = '1.0'
        while 1:
            # find next occurrence, exit loop if no more
            idx = text.search(s, idx, nocase=1, stopindex='end')
            if not idx: break
            # index right after the end of the occurrence
            lastidx = '%s+%dc' % (idx, len(s))
            # tag the whole occurrence (start included, stop excluded)
            text.tag_add('found', idx, lastidx)
            # prepare to search for next occurrence
            idx = lastidx
        # use a red foreground for all the tagged occurrences
        text.tag_config('found', foreground='red')
