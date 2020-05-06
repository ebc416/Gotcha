# Open file for reading in text mode (default mode)
import re
import difflib
import docx2txt
import math
import string
import sys
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

translation_table = str.maketrans(string.punctuation + string.ascii_uppercase," " * len(string.punctuation) + string.ascii_lowercase)

def pCheck(file1_data,file2_data):
    similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    return int(similarity_ratio * 100)
    #return fuzz.ratio(file1_data,file2_data)


def efrainspChecker(file1_data,file2_data):
    #for testing purposes
    #print("The following is part of the fuzz implementation:")
    #print(fuzz.ratio(file1_data,file2_data))
    #print(fuzz.partial_ratio(file1_data,file2_data))
    return fuzz.partial_ratio(file1_data,file2_data)

def read_report(file_one,file_two):
    if (file_one != None and file_two != None):
        if file_one[-3:] == "ocx" and file_two[-3:] == "ocx":
            rev_list1 = docx2txt.process(file_one)
            rev_list2 = docx2txt.process(file_two)
            list1 = rev_list1.splitlines()
            list2 = rev_list2.splitlines()
            # print("this is a list1")
            # print(list1)
            # print("this is a list2")
            # print(list2)
            same = set(list1).intersection(list2)
            return same
        elif file_one[-3:] == "txt" and file_two[-3:] == "txt":
            list1 = open(file_one).readlines()
            list2 = open(file_two).readlines()
            print("this is a list1")
            print(list1)
            print("this is a list2")
            print(list2)

            same = set(list1).intersection(list2)
            return same
        elif file_one[-3:] != file_two[-3:]:
            return "Error"


def highlightfile_docs(text,seq):
    # get string to look for (if empty, no searching)
    #s = "document has stayed the"
    s = seq
    if s:
        # start from the beginning (and when we come to the end, stop)
        idx = '1.0'
        while 1:
            # find next occurrence, exit loop if no more
            idx = text.search(s, idx, nocase=1, stopindex='end')
            beforeidx = idx+"-1c"
            #print("this is idx: ",idx)
            #print("this is beforeidx: ",beforeidx)
            if not idx: break
            # index right after the end of the occurrence
            lastidx = '%s+%dc' % (idx, len(s))
            #print("this is lastidx: ",lastidx)
            # tag the whole occurrence (start included, stop excluded)
            #print("this is the characters beforeidx: ",text.get(beforeidx))
            #print("this is the characters lastidx: ",text.get(lastidx))
            text.tag_add('found', idx, lastidx)
            # prepare to search for next occurrence
            idx = lastidx
        # use a red foreground for all the tagged occurrences
        #text.tag_config('found', foreground='red')
        text.tag_config('found', background="yellow")

def highlight_typedtxts(text,seq):
    # get string to look for (if empty, no searching)
    #s = "document has stayed the"
    s = seq
    if s:
        # start from the beginning (and when we come to the end, stop)
        idx = '1.0'
        while 1:
            # find next occurrence, exit loop if no more
            idx = text.search(s, idx, nocase=1, stopindex='end')
            beforeidx = idx+"-1c"
            #print("this is idx: ",idx)
            #print("this is beforeidx: ",beforeidx)
            if not idx: break
            # index right after the end of the occurrence
            lastidx = '%s+%dc' % (idx, len(s))
            #print("this is lastidx: ",lastidx)
            # tag the whole occurrence (start included, stop excluded)
            #print("this is the characters beforeidx: ",text.get(beforeidx))
            #print("this is the characters lastidx: ",text.get(lastidx))
            if (text.get(beforeidx)).isspace() and (text.get(lastidx)).isspace():
                text.tag_add('found', idx, lastidx)
            #text.tag_add('found', idx, lastidx)
            # prepare to search for next occurrence
            idx = lastidx
        # use a red foreground for all the tagged occurrences
        #text.tag_config('found', foreground='red')
        text.tag_config('found', background="yellow")

def get_words_from_line_list(text):

    text = text.translate(translation_table)
    word_list = text.split()

    return word_list


def count_frequency(word_list):

    D = {}

    for new_word in word_list:

        if new_word in D:
            D[new_word] = D[new_word] + 1

        else:
            D[new_word] = 1

    return D


def word_frequencies_for_file(text_content):

    line_list = text_content
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)


    return freq_mapping

def stats(tcontent):
    printout = "Stats:\n"
    line_list = tcontent
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)

    strLine = str(len(line_list)-1)
    strWrd = str(len(word_list))
    strFrq = str(len(freq_mapping))
    printout += str(strLine + " characters.\n")
    printout += str(strWrd+ " words.\n")
    printout += str(strFrq + " unique words.\n")

    return printout


def dotProduct(D1, D2):
    Sum = 0.0

    for key in D1:

        if key in D2:
            Sum += (D1[key] * D2[key])

    return Sum

def vector_angle(D1, D2):
    numerator = dotProduct(D1, D2)
    denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2))

    return math.acos(numerator / denominator)


def documentSimilarity(store1,store2):

    sorted_word_list_1 = word_frequencies_for_file(store1)
    sorted_word_list_2 = word_frequencies_for_file(store2)

    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
    print("Similarity Score: % 0.6f "% distance)
