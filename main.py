book_path = "books/frankenstein.txt"

def main():
    with open(book_path) as f:
        file_contents = f.read()
        print(f"--- Begin report of {book_path} ---")
        print(f"{count_words(file_contents)} words found in the document\n")
        characters_dict = count_chars(file_contents)
        characters_list = dict_to_list(characters_dict)
        characters_list.sort(reverse=True, key=sort_on)
        
        for c in characters_list:
            print(f"The {c['char']} character appears {c['num']} times")
        print("--- End report ---")

def count_words(file_contents):
    return len(file_contents.split())

def count_chars(file_contents):
    lowered = file_contents.lower()
    chars_dict = {}
    for char in lowered:
        if char.isalpha() == False:
            continue
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_on(dict):
    return dict["num"]

def dict_to_list(dict):
    list = []
    for char, num in dict.items():
        list.append({"char": char, "num": num})
    return list

main()