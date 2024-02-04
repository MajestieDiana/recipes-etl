import isodate
import pandas as pd

# Read the json file in local directory
df = pd.read_json("recipes.json", lines=True)



# Task 1: extract every recipe that has “chilies” (including miss-spelling) in ingredients

## Use regular expression for potential miss-spelling
chilies_df = df.loc[df["ingredients"].str.contains(r'chil[lie]s?', case=False)] 



# Task 2: grade difficulty for extracted recipies based on sum of prepTime and cookTime

## step 1: formating ISO-8601 into aggregatable duration time
def parse_iso_duration(iso_time):
    '''
    Parsing ISO8601 time format into duration format [days hh:mm:ss]
    
    Args: 
        iso_time (object): time in ISO8601 format [PT*M*S]
    
    Returns: 
        duration (timedelta64): Time duration in [0days hh:mm:ss] format, otherwise [0days hh:mm:-1]
    '''
    try: 
        # attempt to perform the parsing
        duration = isodate.parse_duration(iso_time)
    except isodate.isoerror.ISO8601Error:
        # handle 'Na/NaN' and other non-ISO8601 error
        duration = pd.Timedelta(seconds=-1)
    return duration

### apply parsing to prepTime and cookTime, then calculate the sum into a new column 'difficulty'
chilies_df['difficulty'] = chilies_df['prepTime'].apply(parse_iso_duration) + chilies_df['cookTime'].apply(parse_iso_duration)

## step 2: grade difficulty based on sum of cookTime and prepTime
def grade_difficulty(timeDuration): 
    '''
    Grading difficulty based on sum of cookTime and prepTime
    
    Args: 
        timeDuration (timedelta64): time in timedelta format [0days hh:mm:ss(or -1)]
    
    Returns: 
        grade (object): corresponding difficulty ('Hard', 'Medium', 'Easy', 'Unknown')
    '''
    grade = ''
    if timeDuration > pd.Timedelta(hours = 1): 
        grade = 'Hard'
    elif timeDuration > pd.Timedelta(minutes = 30): 
        grade = 'Medium'
    elif timeDuration > pd.Timedelta(minutes = 0): 
        grade = 'Easy'
    else: 
        grade = 'Unknown'
    return grade

### apply difficulty grading for the chilies recipes
chilies_df['difficulty'] = chilies_df['difficulty'].apply(grade_difficulty)

# Save the output to csv file
chilies_df.to_csv('chilies.csv')