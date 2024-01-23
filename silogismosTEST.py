# Define the vowels for each type of statement
vowels = {
    'A': 'a',
    'E': 'e',
    'I': 'i',
    'O': 'o'
}

# Define the function to get the vowel of a statement
def get_vowel(statement):
    if 'All' in statement:
        return vowels['A']
    elif 'No' in statement:
        return vowels['E']
    elif 'Some' in statement:
        if 'not' in statement:
            return vowels['O']
        else:
            return vowels['I']
    else:
        return None

# Define the function to get the terms of a statement
def get_terms(statement):
    terms = statement.split()
    return [terms[0], terms[2]]

# Define the function to generate the conclusion
def get_conclusion(major, minor):
    major_terms = get_terms(major)
    minor_terms = get_terms(minor)
    middle = list(set(major_terms) & set(minor_terms))[0]
    major_term = [x for x in major_terms if x != middle][0]
    minor_term = [x for x in minor_terms if x != middle][0]
    if 'All' in major and 'All' in minor:
        conclusion = 'All ' + minor_term + ' are ' + major_term
    elif 'All' in major and 'Some' in minor:
        conclusion = 'Some ' + minor_term + ' are ' + major_term
    elif 'Some' in major and 'All' in minor:
        conclusion = 'All ' + minor_term + ' are ' + major_term
    elif 'No' in minor:
        conclusion = 'No ' + minor_term + ' are ' + major_term
    else:
        conclusion = None
    return conclusion, middle, major_term, minor_term

# Define the function to get the figure and mode of the syllogism
def get_figure_mode(middle, major_term, minor_term):
    if middle == major_term and middle == minor_term:
        figure = 1
        mode = 'Barbara'
    elif middle == major_term:
        figure = 3
        if 'not' in minor_term:
            mode = 'Celarent'
        else:
            mode = 'Camestres'
    elif middle == minor_term:
        figure = 4
        if 'not' in major_term:
            mode = 'Festino'
        else:
            mode = 'Baroco'
    else:
        figure = 2
        if 'not' in minor_term:
            mode = 'Darapti'
        elif 'not' in major_term:
            mode = 'Datisi'
        else:
            mode = 'Disamis'
    return figure, mode

# Ask the user for the major and minor premises
major = input("Enter the Major Premise: ")
minor = input("Enter the Minor Premise: ")

# Get the vowel of each statement
major_vowel = get_vowel(major)
minor_vowel = get_vowel(minor)

# Get the conclusion and terms of the syllogism
conclusion, middle, major_term, minor_term = get_conclusion(major, minor)

# Print the conclusion and terms of the syllogism
if conclusion:
    print("Conclusion:", conclusion)
else:
    print("No conclusion can be drawn from these premises.")
print("Middle Term:", middle)
print("Vowel of Major Premise:", major_vowel)
print("Vowel of Minor Premise:", minor_vowel)
print("Figure:", figure)
print("Mode:", mode)
