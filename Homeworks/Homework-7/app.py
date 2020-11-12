"""
Homework 7 for the Pirple Python-Is-Easy Course
Author: jzaunegger
Date: November 12th, 2020

About: 
    This homework was about learning about using dictionaries 
    in practical examples.
"""

# Guess if a given key and value are present in the given dictionary
def guess(dictionary, keyName, valueGuess):
    if(dictionary[keyName] == valueGuess):
        return True
    else:
        return False


# Create Dictionary
song = {
    "Song_Name": "Medicated",
    "Artist": "Wiz Khalifa",
    "Featured_Artists": ["Chevy Woods", "Juicy J"],
    "Album": "O.N.I.F.C",
    "Year_Released": 2012,
    "Genre": ["Hip Hop", "Rap"],
    "Song_Duration_in_Minutes": 5.5
}

# Print Dictionary
for entry in song:
    print(entry.replace("_", " "), ":", song[entry])


# Make a guess 

# Returns True
print(guess(song, "Song_Name", "Medicated"))

# Returns False
# print(guess(song, "Song_Name", "Rooftops"))