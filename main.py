def get_number_words(string):
    return len(string.split())


def get_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_chars(text):
    char_dict = {}
    for c in text:
        
        if c.isalpha():
            c = c.lower()
            if c in char_dict:
                char_dict[c]+=1
            else:
                char_dict[c] = 1
    
    return char_dict



def main():
    
    path_to_file = "books/frankenstein.txt"
    file_contents = get_text(path_to_file)

    print("--- Begin report of books/frankenstein.txt ---")

    print(f"{get_number_words(file_contents)} words found in the document\n")
    char_dict = get_num_chars(file_contents)

    for c,n in sorted(char_dict.items(), key = lambda x : x[1], reverse=True):
        print(f"The '{c}' character was found {n} times")


    print("--- End report ---")



'''if __name__ == "__main__":
    main()'''
main()