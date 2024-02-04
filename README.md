# Assessment Recipes - ETL

## Description
A python/pandas assessment that contains two tasks regarding extract, transform and load a json file into csv file. 
- By Zhiying(Diana) Liu [@MajestieDiana](https://github.com/MajestieDiana)

## Table of Contents
1. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
2. [Usage](#usage)
3. [Dependencies](#dependencies)
4. [Python Version](#python-version)

## Getting Started

### Prerequisites
Make sure you have the following installed before running the code:

- Python (version 3.11.7) or other compatible version

### Installation
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/MajestieDiana/recipes-etl
2. Change to the project directory `recipes-etl`, make sure the path is correct
    ```bash
    cd /your-path/recipes-etl
3. Install the required dependencies. (only two modules so did not include a `requirements.txt`)
    ```bash
    pip install isodate
    pip install pandas

## Usage
Run following command in terminal, output is generated in a new file `chilies.csv`
    
    python main.py

### What it does
The script filters out recipes that have chilies in ingredients from existing recipes file in the directory, and graded the difficulty of each recipe based on required cooking and preping time, which is then loaded into a new csv file. 

### How it does it
1. Reads json file `recipes.json` in the downloaded directory `recipes-etl` and loads into a pandas dataframe. 
2. Uses pandas.loc to extract recipes with chilies (including missspelling) in ingredients into a new dataframe.
3. Defines two functions
    - `parse_iso_duration` transforming ISO8601 time formate into duration format
    - `grade_difficulty` grading difficulty based on the sum of cook and prep time
      - `Hard`: sum of time > 1 hour
      - `Medium`: 30 min < sum of time < 1 hour
      - `Easy`: sum of time < 30 min
      - `Unknown`: others
4. Applies the above two functions to grade difficulty for recipes with chilies based on the sum of cooking and preping time
5. Load the result into a new csv file `chilies.csv`, stored in the same directory

## Dependencies
Third party modules used: 
- isodate
- pandas

## Python Version
This project was developed using Python version 3.11.7
Ensure you have a compatible version installed.
