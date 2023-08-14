import spacy
import src.functions as func

def main():
    # Define the names of subfolders in which the data is located
    subfolders = ['a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1']

    # Get a list of files located in each subfolder
    print("Getting the list of files in each subfolder...")
    files, subfolder = func.get_list_of_files(subfolders)

    # Extracting the relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words as well as the total number of unique PER, LOC, ORGS
    print("Extracting information from text...")
    results = func.processing_text(files)

    # Writing the results to a CSV file, one file per subfolder
    print("Writing the results to CSV files...")
    func.write_to_csv(results, subfolder)

if __name__ == "__main__":
    main()