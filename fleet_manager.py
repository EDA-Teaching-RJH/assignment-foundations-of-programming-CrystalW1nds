def main():
    names, ranks, divisions, ids = init_database()
    op = display_menu()

    if op == "1":
        print("Unfinished")
    
    elif op == "2":
        add_member(names, ranks, divisions, ids)

def init_database():
    n = ["Picard", "Riker", "Data", "Worf", "Kirk"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Captain"]
    d = ["Command", "Command", "Operations", "Security", "Command"]
    i = ["1", "2", "3", "4", "5"]

    return n, r, d, i

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

def add_member(n, r, d, i):
    name = input("Enter name to be added:")
    rank = input("Enter rank: ")
    
    if rank == "Crewman Third Class" or rank == "Crewman Second Class" or rank == "Crewman First Class":
        r.append(rank)

    elif rank == "Ensign" or rank == "Lieutenant":
        r.append(rank)

    elif rank == "Commander" or rank == "Captain" or rank == "Lt. Commander":
        r.append(rank)

    elif rank == "Commodore" or rank == "Rear Admiral" or rank == "Vice Admiral":
        r.append(rank)

    else:
        print("Invalid.")
        add_member(n, r, d, i)

    division = input("Enter division: ")
    d.append(division)
    
    id = input("Enter new ID: ")
    
    for int in range(len(id)):
        if id == i[int]:
            print("Invalid.")
            add_member(n, r, d, i)
        
        else:
            i.append(id)

def remove_member(n, r, d, i):
    opt = input("Enter the ID you wish to remove: ")

    idx = i.index(opt)
    n.pop(idx)
    r.pop(idx)
    d.pop(idx)
    i.pop(idx)

def update_rank(n, r, i):
    id = input("Enter the ID of the member whose rank you wish to change: ")
    new_rank = input("Enter the new rank: ")

    for int in range(len(i)):
        if i[int] == id:
            r[int] = new_rank




main()