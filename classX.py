import random

def display_menu():
    print("\n=== JOKE GENERATOR APP ===")
    print("1. Get a random joke")
    print("2. Get multiple jokes")
    print("3. Add your own joke")
    print("4. View all jokes")
    print("5. Exit")
    print("==========================")

def get_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they are made up of everything!",
        "Why did the computer go to therapy? It had too many bytes!",
        "Why do programmers prefer dark mode? Because the light attracts bugs!",
        "Why did the student eat his homework? Because the teacher said it's a piece of cake!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why don't eggs tell jokes? They'd crack each other up!"
    ]
    return random.choice(jokes)

def add_joke():
    new_joke = input("Enter your joke: ")
    if new_joke.strip():
        jokes.append(new_joke)
        print("Joke added successfully!")
    else:
        print("Please enter a valid joke!")

def main():
    print("Welcome to the Joke Generator App!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            print("\n" + get_random_joke())
        elif choice == "2":
            count = int(input("How many jokes do you want? "))
            print("\nHere are your jokes:")
            for i in range(count):
                print(f"{i+1}. {get_random_joke()}")
        elif choice == "3":
            add_joke()
        elif choice == "4":
            print("\nAll available jokes:")
            for i, joke in enumerate(jokes, 1):
                print(f"{i}. {joke}")
        elif choice == "5":
            print("Thanks for using the Joke Generator App!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()