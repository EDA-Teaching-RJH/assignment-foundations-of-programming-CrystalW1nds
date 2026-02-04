def main():
    names, ranks, divisions, ids = init_database()
    op = display_menu()

    if op == "1":
        display_roster(names, ranks, divisions, ids)
    
    elif op == "2":
        add_member(names, ranks, divisions, ids)

    elif op == "3":
        remove_member(names, ranks, divisions, ids)

    elif op == "4":
        update_rank(names, ranks, ids)

    elif op == "5":
        search_crew(names, ranks, divisions, ids)

    elif op == "6":
        filter_by_division(names, divisions)

    elif op == "7":
        payroll = calculate_payroll(ranks)
        print("Cost for full crew: ", payroll)

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
    print("4) Update Rank")
    print("5) Search Crew Name")
    print("6) Filter By Division")
    print("7) Calculate Payroll")
    print("8) Count Officers")

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

def display_roster(n, r, d, i):
    print(f"{'ID':<5} {'Name':<10} {'Rank':>20} {'Division':>20}")
    print("---------------------------------------------------------------------------")

    for id, name, rank, division in zip(i, n, r, d):
        print(f"{id:<5} {name:<10} {rank:>20} {division:>20}")
    
def search_crew(n, r, d, i):
    term = input("Please enter a search term: ")

    for int in range(len(n)):
        if term == n[int]:
            print(n[int], " ", r[int], " ", d[int], " ", i[int])

def filter_by_division(n, d):
    op = input("Please enter a division (Command, Operations, Sciences, Security): ")

    if op == "Command" or op == "Operations" or op == "Sciences" or op == "Security":
        for i in range(len(n)):
            if d[i] == "Command" and op == "Command":
                print(n[i], " ", d[i])

            elif d[i] == "Operations" and op == "Operations":
                print(n[i], " ", d[i])

            elif d[i] == "Sciences" and op == "Sciences":
                print(n[i], " ", d[i])

            elif d[i] == "Security" and op == "Security":
                print(n[i], " ", d[i])

    else:
        print("Invalid.")

def calculate_payroll(ranks):
    payroll = 0
    for i in range(len(ranks)):
        if ranks[i] == "Commodore" or ranks[i] == "Rear Admiral" or ranks[i] == "Vice Admiral":
            payroll = payroll + 2000

        elif ranks[i] == "Commander" or ranks[i] == "Captain":
            payroll = payroll + 1000

        elif ranks[i] == "Ensign" or ranks[i] == "Lieutenant":
            payroll = payroll + 500

        elif ranks[i] == "Crewman Third Class" or ranks[i] == "Crewman Second Class" or ranks[i] == "Crewman First Class":
            payroll = payroll + 200

    return(payroll)



main()