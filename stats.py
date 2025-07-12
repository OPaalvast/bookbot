def get_num_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    characters_in_text = list(set(text))
    character_dictionary = {}
    for character in characters_in_text:
        character_dictionary[character] = len([f for f in text if f == character])

    return character_dictionary

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    dictionary_list = []
    for key in dictionary.keys():
        if key.isalpha():
            dictionary_list.append({"char": key, "num": dictionary[key]})
    
    dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list