
# def decode(message_file):
#     # Step 1: Read the file and store the data in a dictionary
#     number_word_dict = {}
#     with open(message_file, 'r') as file:
#         for line in file:
#             number, word = line.split()
#             number_word_dict[int(number)] = word

#     # Step 2: Determine the number of levels in the pyramid
#     total_numbers = len(number_word_dict)
#     levels = int(((-1 + (1 + 8 * total_numbers) ** 0.5) / 2))

#     # Step 3: Find the key numbers corresponding to the end of each pyramid level
#     key_numbers = [(n * (n + 1)) // 2 for n in range(1, levels + 1)]

#     # Step 4: Extract the words corresponding to these key numbers
#     decoded_words = [number_word_dict[number] for number in key_numbers]

#     # Step 5: Construct and return the decoded message
#     return ' '.join(decoded_words)

# # This line below would be used to test the function:
# decoded_message = decode("message.txt")
# print(decoded_message)

def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    decoded_message = []
    for i, line in enumerate(lines):
        words = line.strip().split()[1:]  # Assuming we always have at least two words per line
        decoded_message.append(words[-1])  # This will fail if a line has no spaces (i.e., one word)
    return ' '.join(decoded_message)

# Test the function
decoded_message = decode("message.txt")
print(decoded_message)