secret_exit_word = "chupacabra"
your_word = input("enter a word: ")

while your_word != secret_exit_word:
    your_word = input("enter a word:")
    if your_word == secret_exit_word:
        print("You've successfully left the loop.")
        break