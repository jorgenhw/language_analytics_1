<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Cultural Datascience 2023</h1> 
  <h2 align="center">Assignment 1 </h2> 
  <h3 align="center"><i>Extracting linguistic features using spaCy</i></h3><hr>



  <p align="center">
    Jørgen Højlund Wibe
  </p>
</p>

<!-- ABOUT THIS ASSIGNMENT -->
## About the project
This assignment concerns using ```spaCy``` to extract linguistic information from a corpus of texts.

The corpus is an interesting one: *The Uppsala Student English Corpus (USE)*. All of the data is included in the folder called ```in``` but you can access more documentation via [this link](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).

The information to be extracted is the

* Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
* Total number of *unique* PER, LOC, ORGS

## Usage
To use or reproduce our results you need to adopt the following steps.

**NOTE:** There may be slight variations depending on the terminal and operating system you use. The following example is designed to work using the Visual Studio Code version 1.76.0 (Universal). The terminal code should therefore work using a unix-based bash. The avoid potential package conflicts, the ```setup.sh``` bash files contains the steps necesarry to create a virtual environment for the project.

1. Clone repository
2. Run setup.sh

### Clone repository

Clone repository using the following lines in the unix-based bash:

```bash
git clone https://github.com/jorgenhw/language_analytics_assignment_1.git
```
```
cd language_analytics_assignment_1
```
### Run ```setup.sh```

To replicate the results, I have included a bash script that automatically 

1. Creates a virtual environment for the project
2. Activates the virtual environment
3. Installs the correct versions of the packages required
4. Runs the script
5. Deactivates the virtual environment

Run the code below in your bash terminal:

```bash
bash setup.sh
```

## Inspecting results
Text files (.csv) containing the linguistic information extracted from each of the text files are located in the ```out``` folder. Here one can inspect the results for each text file.

<!-- REPOSITORY STRUCTURE -->
## Repository structure
This repository has the following structure:
```
│   main.py
│   README.md
│   requirements.txt
│   setup.sh
│
├───in
│   ├───USEcorpus   
│        ├───a1
│             .txt files
│        ├───a2
│             .txt files
│        ├───a3
│             .txt files
│        ├───a4
│             .txt files
│        ├───a5
│             .txt files
│        ├───b1
│             .txt files
│        ├───b2
│             .txt files
│        ├───b3
│             .txt files
│        ├───b4
│             .txt files
│        ├───b5
│             .txt files
│        ├───b6
│             .txt files
│        ├───b7
│             .txt files
│        ├───b8
│             .txt files
│        ├───c1
│             .txt files
│
├───out
│       a1_results.csv
│       a2_results.csv
│       a3_results.csv
│       a4_results.csv
│       a5_results.csv
│       b1_results.csv
│       b2_results.csv
│       b3_results.csv
│       b4_results.csv
│       b5_results.csv
│       b6_results.csv
│       b7_results.csv
│       b8_results.csv
│       c1_results.csv
│
└──src
        functions.py
```

<!-- REPOSITORY STRUCTURE -->
## Conclusion
In conclusion, this project utilizes the spaCy library to extract linguistic information from the Uppsala Student English Corpus (USE). The results are in an by themselves not of interest, however, the project shows how anyone interested in natural language processing and corpus analysis using spaCy.