import random
import time

# ASCII art for dice faces
DICE_ART = {
    1: (
        "┌─────────┐\n"
        "│         │\n"
        "│    ●    │\n"
        "│         │\n"
        "└─────────┘"
    ),
    2: (
        "┌─────────┐\n"
        "│  ●      │\n"
        "│         │\n"
        "│      ●  │\n"
        "└─────────┘"
    ),
    3: (
        "┌─────────┐\n"
        "│  ●      │\n"
        "│    ●    │\n"
        "│      ●  │\n"
        "└─────────┘"
    ),
    4: (
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│         │\n"
        "│  ●   ●  │\n"
        "└─────────┘"
    ),
    5: (
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│    ●    │\n"
        "│  ●   ●  │\n"
        "└─────────┘"
    ),
    6: (
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "└─────────┘"
    ),
}

def roll_dice():
    """
    Returns a random number between 1–6, simulating a dice roll.
    """
    return random.randint(1, 6)

def print_dice(rolls):
    """
    Takes a list of numbers and prints the ASCII dice faces side by side.
    """
    dice_rows = ["", "", "", "", ""]

    for number in rolls:
        art_lines = DICE_ART[number].split("\n")
        for i in range(5):
            dice_rows[i] += art_lines[i] + "   "

    for row in dice_rows:
        print(row)

def main():
    print("\n🎲 Welcome to the Python Dice Roller Game!")
    print("-----------------------------------------")

    while True:
        try:
            num_dice = int(input("\nHow many dice do you want to roll? (1-5): "))
            if num_dice < 1 or num_dice > 5:
                print("Please choose between 1 and 5 dice.")
                continue
        except ValueError:
            print("Invalid input. Enter a number between 1-5.")
            continue

        print("\nRolling the dice...")
        time.sleep(0.8)

        rolls = [roll_dice() for _ in range(num_dice)]

        print("\nYour dice:")
        print_dice(rolls)

        print("\nYou rolled:", rolls)

        choice = input("\nRoll again? (y/n): ").strip().lower()
        if choice != "y":
            print("\nThanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    main()