#Libraries#
import os
from pandas import DataFrame
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score


#Declarations#
NEWLINE = "\n"
pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range=(1,2))),
    ('classifier', MultinomialNB()) 
])

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

examples = ['Free Viagra call today!', "I'm going to attend the Linux users group tomorrow."]

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



#Now that the data is available in the required format, we can finally build our classifer. We evaluate it using 6_fold cross-validation
k_fold = KFold(n=len(data), n_folds=6)
scores = []
confusion = numpy.array([[0,0], [0,0]])

#We get 6 pairs of 1:5 test-train data indices
for train_indices, test_indices in k_fold:
    
    train_text = data.iloc[train_indices]['text'].values
    train_y = data.iloc[train_indices]['class'].values
    
    test_text = data.iloc[test_indices]['text'].values
    test_y = data.iloc[test_indices]['class'].values

    
    pipeline.fit(train_text, train_y)
    predictions = pipeline.predict(test_text)
    
    confusion += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions, pos_label=SPAM)
    
    scores.append(score)
print('Total emails classified:', len(data))
print('Score:', sum(scores)/len(scores))
print('Confusion matrix:')
print(confusion)



#print(data)