#Libraries#
import os
from pandas import DataFrame
import numpy
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.naive_bayes import MultinomialNB

#Declarations#
NEWLINE = "\n"
#count_vectorizer = CountVectorizer()
#classifier = MultinomialNB()

HAM = 'ham'
SPAM = 'spam'

SOURCES = [
    ('data/spam',        SPAM),
    ('data/easy_ham',    HAM),
    ('data/hard_ham',    HAM),
    ('data/beck-s',      HAM),
    ('data/farmer-d',    HAM),
    ('data/kaminski-v',  HAM),
    ('data/kitchen-l',   HAM),
    ('data/lokay-m',     HAM),
    ('data/williams-w3', HAM),
    ('data/BG',          SPAM),
    ('data/GP',          SPAM),
    ('data/SH',          SPAM)
]

SKIP_FILES = {'cmds'}

#Function for reading all file contents 
def read_files(path):
    #Considering every file in root folder
    for root, dir_names, file_names in os.walk(path):
        #recursively call into sub-directories
        for path in dir_names:
            read_files(os.path.join(root, path))
        #print(file_names)
        for file_name in file_names:
            #skip those files in SKIP_FILES
            if file_name not in SKIP_FILES:
                #print(file_name)
                file_path = os.path.join(root, file_name)
                #print("file_path: " + file_path)
                if os.path.isfile(file_path):
                    past_header, lines = False, []
                    #Opening the file
                    f = open(file_path, encoding = 'latin-1')
                    #Checking line by line, start adding lines only after NEWLINE
                    for line in f:
                        if past_header:
                            lines.append(line)
                        elif line == NEWLINE:
                            past_header = True
                    f.close()
                    content = NEWLINE.join(lines)
                    #print(content)
#                    print(file_path)
                    yield file_path, content
                    
                    
                    
#Creates data into data frame                    
def build_data_frame(path, classification):
    rows = []
    index = []
    for file_name, text in read_files(path):
        rows.append({'text':text, 'class': classification})
        #print(text)
        index.append(file_name)
    data_frame = DataFrame(rows, index = index)
    return data_frame




data = DataFrame({'text': [], 'class': []})

for path, classification in SOURCES:
    data = data.append(build_data_frame(path, classification))

data = data.reindex(numpy.random.permutation(data.index))
#counts = count_vectorizer.fit_transform(data['text'].values)

#targets = data['class'].values
#classifier.fit(counts, targets)


#print(data)