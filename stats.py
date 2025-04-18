
def get_num_words(text):
    """
    Accepts text as a string and returns the number of words in the string.
    """
    words = text.split()
    return len(words)

def get_chars_dict(text):
    """
    Accepts text as a string and returns a dictionary with each character and 
    the number of times it appears in the text.
    """
    text = text.lower()
    chars_dict = {}
    for char in text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def chars_dict_to_sorted_list(chars_dict):
    """
    Takes a dictionary of characters and their counts and returns a sorted list
    of dictionaries ordered by count (greatest to least).
    """
    sorted_list = []
    for char, count in chars_dict.items():
        char_dict = {"character": char, "count": count}
        sorted_list.append(char_dict)
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list