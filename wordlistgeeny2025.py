import random
import string
import os

# Function to print the intro message
def print_intro():
    intro_text = """
**********************************************
*             Welcome to Wordlistgeeny       *
*   A simple and interactive headless geeny  *
*           2025                             *
*          Written by Lathusan G.            *
***********************************************

                            ___====-_  _-====___
                       _--^^^#####//      \\####^^^--_
                    _-^##########// (    ) \\##########^-_
                   -############//  |\^^/|  \\############-
                 _/############//   (@::@)   \\############\_
                /#############((     \\//     ))#############\\
               -###############\\    (oo)    //###############-
              -#################\\  / UUU \\  //#################-
             -###################\\/  (   )  \//###################-
            _/|##########/\######(   /   \   )######/\##########|\_
           |/ |#/\#/\#/\/  \#/\##\  |  (   )  |  /##/\#/\/\#/\#/\| \
           `  |/  V  |/      |  |   |   |   |   |  |   |  |  |  |   `
             `   |   |       |   |  |   |   |   |   |   |  |   |  
                (   |       |   |  |   |   |   |   |   |  |   |   
                 \  |       |   |  |   |   |   |   |   |  |   |  
                  \ |_______|   |  |   |   |   |   |   |  |   |  
                   `         _/    |   |   |   |   |   |  |   |  
                            (      /   |   |   |   |   |   |  |  
                             \_____/    |   |   |   |   |   |  
                                          |   |   |   |   |   |  
                                          |___|   |___|___|   |  
"""
    print(intro_text)

# Function to generate a single wordlist entry
def generate_wordlist_entry(target_infos, password_length, include_numbers, include_special_chars, randomness_level):
    word = ''
    
    while len(word) < password_length:
        if randomness_level == 'low':
            # More target-based (less random)
            choice = random.choice([0, 0, 1])  # Prefer target-based over random characters
        elif randomness_level == 'high':
            # More random characters
            choice = random.choice([0, 1, 2])
        else:
            choice = random.choice([0, 1, 2])
        
        if choice == 0:  # Add random word
            word += random.choice(target_infos)
        elif choice == 1:  # Add random digit
            if include_numbers:
                word += random.choice(string.digits)
        else:  # Add random special character
            if include_special_chars:
                word += random.choice(string.punctuation)

    return word

# Function to generate the wordlist
def generate_wordlist(target_info, password_length_range, output_file, include_numbers, include_special_chars, randomness_level, num_entries):
    wordlist = []

    # Split target information into multiple pieces
    target_infos = target_info.split(',')

    # Add variations of each piece of target information
    for info in target_infos:
        wordlist.extend([
            info.lower(),
            info.upper(),
            info.capitalize(),
            info[::-1],
            info.replace('a', '@').replace('e', '3').replace('i', '!').replace('o', '0').replace('s', '$')
        ])

    # Generate random strings for wordlist
    min_length, max_length = password_length_range
    for _ in range(num_entries):
        password_length = random.randint(min_length, max_length)
        word = generate_wordlist_entry(target_infos, password_length, include_numbers, include_special_chars, randomness_level)
        wordlist.append(word)

    # Save wordlist to a file
    with open(output_file, 'w') as file:
        for word in wordlist:
            file.write(word + '\n')

    print(f"Wordlist saved as {output_file}.")

# Main function to handle user inputs step-by-step
def main():
    # Display the introduction
    print_intro()

    print("Welcome to the Wordlist Generator!")
    print("Let's walk through the steps to create your custom wordlist.")

    # Step 1: Ask for target information
    target_info = input("Step 1: Enter the target information (comma-separated, e.g., username, company, etc.): ")

    # Step 2: Ask for the password length range
    while True:
        password_length_range = input("Step 2: Enter the password length range (e.g., '8-12'): ")
        try:
            min_length, max_length = map(int, password_length_range.split('-'))
            if min_length <= 0 or max_length <= 0 or min_length > max_length:
                raise ValueError
            break
        except ValueError:
            print("Invalid range. Please enter a valid range (e.g., '8-12').")

    # Step 3: Ask if the user wants to include numbers
    include_numbers = input("Step 3: Do you want to include numbers in the wordlist? (y/n): ").strip().lower() == 'y'

    # Step 4: Ask if the user wants to include special characters
    include_special_chars = input("Step 4: Do you want to include special characters in the wordlist? (y/n): ").strip().lower() == 'y'

    # Step 5: Ask for randomness level
    while True:
        randomness_level = input("Step 5: Select the randomness level ('low', 'medium', 'high'): ").strip().lower()
        if randomness_level in ['low', 'medium', 'high']:
            break
        else:
            print("Invalid option. Please select 'low', 'medium', or 'high'.")

    # Step 6: Ask for the number of entries to generate
    while True:
        try:
            num_entries = int(input("Step 6: How many entries do you want to generate?: "))
            if num_entries <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive number.")

    # Step 7: Ask for output filename
    output_file = input("Step 7: Enter the output filename (e.g., wordlist.txt): ")

    # Check if the output file already exists
    if os.path.exists(output_file):
        overwrite = input(f"File {output_file} already exists. Do you want to overwrite it? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Exiting without overwriting the file.")
            return

    # Generate the wordlist
    generate_wordlist(target_info, (min_length, max_length), output_file, include_numbers, include_special_chars, randomness_level, num_entries)

if __name__ == "__main__":
    main()
