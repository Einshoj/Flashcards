import random

terms = {"1" : "def 1", #Dictionary of 'terms' and 'definitions'
         "2" : "def 2",
         "3" : "def 3"}

menu = None
while menu != "4":
    print("""

    DIGITAL FLASHCARDS!

    1 - List Terms
    2 - Add Term
    3 - Guess Random Definition
    4 - Exit

    """)
    menu = input("\t\t\tEnter Menu option: ")
    if menu == "1":  # List Terms
        print("\n")
        for term in terms:
            print("\t\t\t", term)
        input("\n\tPress 'Enter' to return to Main Menu.\n")

    elif menu == "2":  # Add Term
        term = input("\n\tEnter the new term: ").upper()
        if term not in terms:
            definition = input("\tWhat is the definition? ")
            terms[term] = definition
            print("\n\t" + term, "has been added.")
        else:
            print("\n\tThat term already exists!")
            input("\n\tPress 'Enter' to return to Main Menu.\n")

    elif menu == "3": # Guess Random Definition. Once correct, choose new random definition
        print("\n\t\t\tType 'Exit' to return to Menu\n")
        choice = random.choice(list(terms.values()))
        print("\n\t" + choice + "\n")

        guess = None
        while guess != "EXIT":
            guess = str(input("\tWhat is the term? ")).upper()