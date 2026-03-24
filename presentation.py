# Presentation Layer

def show_menu(score):
    print("\n--- Clicker Game ---")
    print(f"Score: {score}")
    print("1. Click")
    print("2. Buy Upgrade (+1 per click) [Cost: 10]")
    print("3. Exit")

def get_input():
    return input("Choose: ")