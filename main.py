import sys
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def get_book_text(filepath):
    """
    Takes a filepath as input and returns the contents of the file as a string.
    
    Args:
        filepath (str): Path to the file to be read
        
    Returns:
        str: The contents of the file
    """
    with open(filepath, 'r') as f:
        return f.read()

def main():
    """
    Reads the contents of frankenstein.txt, analyzes the text,
    and prints a report to the console.
    """
    # check if we have the right number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys-exit(1)
    
    # Get the book path from command line arguments
    book_path = sys.argv[1]

    # read the book text
    text = get_book_text(book_path)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    # Get and print word count
    word_count = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    # Get character counts
    chars_dict = get_chars_dict(text)
    
    # Sort character counts
    sorted_chars = chars_dict_to_sorted_list(chars_dict)
    
    # Print character counts
    print("--------- Character Count -------")
    for char_info in sorted_chars:
        char = char_info["character"]
        count = char_info["count"]
        
        # Skip non-alphabetical characters
        if not char.isalpha():
            continue
            
        print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()