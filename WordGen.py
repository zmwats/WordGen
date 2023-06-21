import random

def main():
    
    def intro(): 
        print("Welcome to the random word Generator!")
        print("This program will generate a list of random words.")
        print("Please enter the number of words that you would like to generate.")
    intro() 

    num_words = int(input("Number of words: "))       
 
    with open('words.txt') as wordlist_file:
        words = wordlist_file.read().split()
    
    if 1 <= num_words <= 100:
        random_words = random.sample(words, k=num_words)
        print("Random Words: ")
        for word in random_words:
            print(word)
    else:
        print("Please enter a number between 1 and 100.")

    def export():
        print("Would you like to export these words to a text file?")
        if input("Y/N: ").lower() == "y":
            with open('word_export.txt', 'w') as export_file:
                for word in random_words:
                    export_file.write(word + "\n")
            print("Words have been exported to wordlist_export.txt")
        else:
            print("Random words were not exported.")
    export()


main()

    
        

    

    
