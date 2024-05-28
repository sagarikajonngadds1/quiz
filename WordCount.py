def get_user_input():
    '''
    Prompt the user to enter a sentence or paragraph.
    Returns the user input as a string.
    '''
    user_input = input("Please enter a sentence or paragraph: ").strip()
    return user_input

def count_words(text):
    '''
    Count the number of words in the given text.
    text (str): The input text to be processed.
    
    int: The number of words in the text.
    Split the text by whitespace to get words
    '''
    words = text.split()
    return len(words)

def display_word_count(count):
    #Display the word count to the user.
    print(f"The number of words in the given text is: {count}")

def main():
    '''
    Main function to run the word counter program.
    Get user input
    '''
    text = get_user_input()
    
    # Error handling for empty input
    if not text:
        print("Error: No input provided. Please enter a valid sentence or paragraph.")
        return
    
    # Count the words in the input text
    word_count = count_words(text)
    
    # Display the word count
    display_word_count(word_count)
if __name__ == "__main__":
    #double underscore helps to determine if the script is run directly or imported as module
    main()