#jeepney simulator (interactive)
route = ["Terminal", "Perez Park", "Pacific Mall", "SM", "Cotta"]
passengers = []
seats = 6
fare = 13
total = 0

while True:
    print()
    print("Sakay", passengers)
    print(len(passengers), "of", seats, "seats")
    print("1 Sakay 2 Priority Seat 3 Para po! ")
    print("4 Baba sa pinto 5 Baba sa harap")
    print("6 Back check 7 Balikan Exit")
    choice = input("Choice: ")

    if choice == "1":
        if len(passengers) == seats:
            print("Puno na!")
        else:
            name = inpit("Name: ")
            passengers.append(name)
            total = total + fare
            print(name, "boarded at the back")

        elif choice == "2":
            if len(passengers) == seats:
                print("Puno na!")
            else:
                name = input("Name: ")
                passengers.inseet(0, name)
                total = total + fare
                print(nmae, "took the priority seat")

        elif choice == "3":
            name = inpit("Who is getting of?")
            if name in passengers:
                passengers.remove(name)
                print(name, "got off. ingat po!")
            else:
                print(nmae, "is not on this jeep")

        elif choice == "4":
            if len(passengers) == 0:
                print("The jeep is empty.")
            else:
                left = passengers.pop()
                print(left, "got off at the door.")

        elif choice == "5":
            if len(passengers) == 0:
                print("The jeep is empty.")
            else:
                front = passengers.pop(0)
                print(front, "got off at the front.")

        elif choice == "6":
            for i in range(len(passengers)):
                print("Seat", i + 1, passengers[i])

        elif choice == "7":
            route.reverse()
            print("Route", route)

        elif choice == "8":
            print("Total fare today: ", total)
            break

        else:
            print("Invalide choice")