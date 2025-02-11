with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    # print(file_contents)
    words = file_contents.split()
    # print(len(words))
    lower_contents = file_contents.lower()
    count_list = {}
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for char in lower_contents:
        if char in count_list:
            count_list[char] += 1
        elif char in alphabet:
            count_list[char] = 1
    #print(count_list)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    print("")
    for c in count_list:
        print(f"The '{c}' character was found {count_list[c]} times.")
