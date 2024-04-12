import random

def hex_to_notes(hex_string):
    # Define the note mapping
    notes = ['c4', 'c#4', 'd4', 'd#4', 'e4', 'f4', 'f#4', 'g4', 'g#4', 'a4', 'a#4', 'b4',
             'c5', 'c#5', 'd5', 'd#5', 'e5', 'f5', 'f#5', 'g5', 'g#5', 'a5', 'a#5', 'b5']
    
    # Map each hex digit to a note
    result = [notes[int(char, 16)] for char in hex_string]
    return result

def create_durations():
    sum = 0
    durations = []
    while sum <= 64:
        rand = random.randint(1, 8)
        sum += rand
        durations.append(rand)
    
    durations[len(durations)-1] -= (sum-64)
    if(durations[len(durations)-1] == 0):
        durations.pop()

    return durations

durations = create_durations()
print(durations)
print(durations[len(durations)-1])