encoded_data = {
    193: 'land', 284: 'sun', 16: 'too', 136: 'huge', 26: 'dont', 286: 'such', 130: 'noun', 202: 'student', 184: 'brown', 135: 'complete', 118: 'play', 29: 'cook', 72: 'yard', 233: 'clock', 275: 'would', 265: 'plain', 5: 'excite', 132: 'fire', 28: 'wish', 213: 'cool', 272: 'child', 163: 'past', 212: 'colony', 222: 'oil', 7: 'dog', 115: 'back', 100: 'money', 214: 'kind', 64: 'open', 107: 'finger', 19: 'touch', 109: 'are', 241: 'dad', 104: 'am', 208: 'modern', 108: 'meant', 44: 'ocean', 228: 'pitc...
}

# Create pyramid levels
pyramid_levels = []
current_level = []

for number in sorted(encoded_data.keys()):
    current_level.append(number)
    if len(current_level) == 2 ** (len(pyramid_levels) + 1):
        pyramid_levels.append(current_level)
        current_level = []

# Read the last number from each hierarchy
last_numbers = []
for level in pyramid_levels:
    last_numbers.append(level[-1])

print("Last number from each hierarchy:", last_numbers)
