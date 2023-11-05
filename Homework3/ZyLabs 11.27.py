# Will Buckner Jr#
# PSID: 2101260#
def soccer_team_roster(storage):

    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")

    choice = input("Choose an option:\n").lower()

    while choice != "q":

        if choice == 'a':
            jersey_num = int(input("Enter a new player's jersey number:\n"))
            player_rating = int(input("Enter the player's rating:\n"))
            storage[jersey_num] = player_rating

            print("\nMENU")
            print("a - Add player")
            print("d - Remove player")
            print("u - Update player rating")
            print("r - Output players above a rating")
            print("o - Output roster")
            print("q - Quit\n")
            choice = input("Choose an option:\n").lower()

        elif choice == 'd':
            jersey_remove = int(input("Enter a jersey number:\n"))
            del storage[jersey_remove]

            print("\nMENU")
            print("a - Add player")
            print("d - Remove player")
            print("u - Update player rating")
            print("r - Output players above a rating")
            print("o - Output roster")
            print("q - Quit\n")
            choice = input("Choose an option:\n").lower()

        elif choice == 'u':
            jersey_update = int(input("Enter a jersey number:\n"))
            rating_update = int(input("Enter a new rating for player:\n"))
            storage[jersey_update] = rating_update

            print("\nMENU")
            print("a - Add player")
            print("d - Remove player")
            print("u - Update player rating")
            print("r - Output players above a rating")
            print("o - Output roster")
            print("q - Quit\n")
            choice = input("Choose an option:\n").lower()

        elif choice == 'r':
            sort_rating = int(input("Enter a rating:\n"))
            print(f"\nABOVE {sort_rating}")

            print("\nMENU")
            print("a - Add player")
            print("d - Remove player")
            print("u - Update player rating")
            print("r - Output players above a rating")
            print("o - Output roster")
            print("q - Quit\n")
            choice = input("Choose an option:\n").lower()

        elif choice == 'o':
            print("ROSTER")
            sorted_jersey_number = sorted(storage.keys())
            for jersey_num in sorted_jersey_number:
                print(f"Jersey number: {jersey_num}, Rating: {storage[jersey_num]}")

            print("\nMENU")
            print("a - Add player")
            print("d - Remove player")
            print("u - Update player rating")
            print("r - Output players above a rating")
            print("o - Output roster")
            print("q - Quit\n")
            choice = input("Choose an option:\n").lower()

        elif choice == 'q':
            break
        else:
            choice = input("Choose an option:\n").lower()


if __name__ == "__main__":
    storage1 = {}

    for x in range(1, 6):
        player_jersey = int(input(f"Enter player {x}'s jersey number:\n"))
        player_rate = int(input(f"Enter player {x}'s rating:\n"))
        print("")
        if (-1 < player_jersey < 100) and (0 < player_rate < 10):
            storage1[player_jersey] = player_rate
        else:
            player_jersey = int(input(f"Enter player {x}'s jersey number:\n"))
            player_rate = int(input(f"Enter player {x}'s rating:\n"))

    print("ROSTER")

    sorted_jersey_numbers = sorted(storage1.keys())
    for jersey in sorted_jersey_numbers:
        print(f"Jersey number: {jersey}, Rating: {storage1[jersey]}")

    soccer_team_roster(storage1)
