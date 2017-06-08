# Write a Python program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.

Define a function that takes the following dictionary as a parameter and converts it into a DataFrame.
The function should return those rows where the number of attempts is less than 2 and score is greater than 15.
 
**Input:**
    
    {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}


**Output:**
        
        attempts   name    qualify  score
    9          1       Jonas         yes   19.0