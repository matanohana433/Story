def elevator_prog():
    elevator = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    current_floor = 0
    elevator_in = True

    while elevator_in:
        print(f"Available floors: {elevator}")
        wanted_floor = int(input(
            f"Welcome to the elevator. You are on floor {current_floor}. What floor do you want to go to? (Press -3 to leave) "))

        if wanted_floor == -3:
            elevator_in = False
        elif wanted_floor in elevator:
            if wanted_floor > current_floor:
                for floor in range(current_floor + 1, wanted_floor + 1):
                    print(f"Passing floor: {floor}")
                current_floor = wanted_floor
                print(f"Welcome to floor: {current_floor}")

            elif wanted_floor < current_floor:
                for floor in range(current_floor - 1, wanted_floor - 1, -1):
                    print(f"Passing floor: {floor}")
                current_floor = wanted_floor
                print(f"Welcome to floor: {current_floor}")

        else:
            print("Invalid floor selected. Please try again.")

    print("Bye Bye")


elevator_prog()
