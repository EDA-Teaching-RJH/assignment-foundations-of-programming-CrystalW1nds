def init_database():
    name = ["Picard", "Riker", "Data", "Worf", "Kirk"]
    rank = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Captain"]
    division = ["Command", "Command", "Operations", "Security", "Command"]
    id = ["01", "02", "03", "04", "05"]

    return name, rank, division, id

def display_menu():
    uName = input("Please enter your full name: ")

    print(uName, " logged in!")
    print("\n--- MENU ---")
    print("1) View Crew Members")
    print("2) Add Crew Member")
    print("3) Remove Crew Member")
    print("4) Analyse Data")
    print("5) Exit")

    opt = input("Select option: ")

    return opt

