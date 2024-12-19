def char_count(text):
    words = text.split()
    dict = {}

    for word in words:
        lowercase = word.lower()
        for c in lowercase:
            if (c in dict):
                dict[c] += 1
            else:
                dict[c] = 1

    return dict

def word_count(text):
    split = text.split()
    return len(split)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Report on Frankenstein by Mary Shelley ---")
        count = word_count(file_contents)
        print(f"Frankenstein contains {count} words")

        dict = char_count(file_contents)
        print("\nFrankenstein Character Count:\n")
        for key in dict:
            print(f"The character {key} appears {dict[key]} times\n")

        print("--- End of report ---")

        

main()