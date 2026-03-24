# main.py (Monolithic)

score = 0
click_value = 1

def show_menu():
    print("\n--- Clicker Game ---")
    print(f"Score: {score}")
    print("1. Click")
    print("2. Buy Upgrade (+1 per click) [Cost: 10]")
    print("3. Exit")

def main():
    global score, click_value

    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            score += click_value

        elif choice == "2":
            if score >= 10:
                score -= 10
                click_value += 1
                print("Upgrade purchased!")
            else:
                print("Not enough points!")

        elif choice == "3":
            break

        else:
            print("Invalid input")

if __name__ == "__main__":
    main()