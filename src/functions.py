import os
import glob
import re
import csv
import spacy
from tqdm import tqdm


# Function that returns a list of files in each subfolder located in the in/USEcorpus folder
def get_list_of_files(subfolders):
    files = []
    for subfolder in subfolders:
        subfolder = subfolder
        path = os.path.join('in', 'USEcorpus', subfolder)
        # Creating a list of the .txt files present in each of the subfolders
        files.extend(glob.glob(os.path.join(path, '*.txt'))) # extend the files list with the files in the subfolder
    
    return files, subfolder

# Calculating the relative frequency of nouns, verbs, adjectives, and adverbs
def calculate_relative_frequency(doc, files):
    # Calculating the relative frequency of nouns, verbs, adjectives, and adverbs
        num_words = len(doc) # number of words in the document
        num_nouns = len([token for token in doc if token.pos_ == 'NOUN']) # token for token means that we are looping over each token in the document
        num_verbs = len([token for token in doc if token.pos_ == 'VERB']) # number of verbs in the document
        num_adjs = len([token for token in doc if token.pos_ == 'ADJ']) # number of adjectives in the document
        num_adv = len([token for token in doc if token.pos_ == 'ADV']) # number of adverbs in the document
        freq_nouns = num_nouns / num_words * 10000
        freq_verbs = num_verbs / num_words * 10000
        freq_adjs = num_adjs / num_words * 10000
        freq_adv = num_adv / num_words * 10000
        
        # Calculate the number of unique words associated with each PERSON, LOC, and ORG entity
        num_person_words = len(set([word for word in doc if word.ent_type_ == 'PERSON']))
        num_loc_words = len(set([word for word in doc if word.ent_type_ == 'LOC']))
        num_org_words = len(set([word for word in doc if word.ent_type_ == 'ORG']))
        
        # Add the results for the file to the results list
        results = []
        results.append([files, freq_nouns, freq_verbs, freq_adjs, freq_adv, num_person_words, num_loc_words, num_org_words])

        return results

def processing_text(files):
    # Loading the language model
    nlp = spacy.load('en_core_web_md') # loading model
    
    results = []
    for file in tqdm(files): # for each file in the list of files (created earlier)
        # Open the file and read its contents
        with open(file, 'r', encoding="latin-1") as f:
            text = f.read()

        # Preprocessing: Remove all text inside angled brackets (<>)
        text = re.sub(r'<.*?>', '', text)

        # Create a Spacy Doc object from the text (still for each file in each subfolder (N.B. the loop))
        doc = nlp(text)

        result = calculate_relative_frequency(doc, file)
        results.extend(result)
        
    return results


# Write the results to a CSV file for the subfolder
def write_to_csv(results, subfolder):
    with open(os.path.join('out', f'{subfolder}_results.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['File_name', 'Noun_Freq', 'Verb_Freq', 'Adj_Freq', 'Adv_Freq', 'PERSON_Tags', 'LOC_Tags', 'ORG_Tags'])
        writer.writerows(results)