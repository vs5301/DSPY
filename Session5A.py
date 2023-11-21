# Model
# Data Structure for Covid-19 Cases

# Controller | Logical Processing on Data
# Filtering
#     filter by shoe size
#     filter by shoe color [black or green]
#   Searching
#         To loop up for some item in a collection
#   Sorting
#         may be ascending or descending based on an attribute

state1 = {
    "active": 881,
    "confirmed": 3497,
    "deaths": 78,
    "recovered": 2538,
    "state": "Punjab",
}

state2 = {
    "active": 51922,
    "confirmed": "116752",
    "deaths": 5651,
    "recovered": 59166,
    "state": "Maharashtra",
}

state3 = {
    "active": 21993,
    "confirmed": 50193,
    "deaths": 576,
    "recovered": 27624,
    "state": "Tamil Nadu",
}

state4 = {
    "active": 27741,
    "confirmed": 47102,
    "deaths": 1904,
    "recovered": 17457,
    "state": "Delhi",
}

state5 = {
    "active": 6149,
    "confirmed": 25148,
    "deaths": 1561,
    "recovered": 17438,
    "state": "Gujarat",
}

state6 = {
    "active": 5659,
    "confirmed": 15785,
    "deaths": 488,
    "recovered": 9638,
    "state": "Uttar Pradesh",
}

state7 = {
    "active": 2721,
    "confirmed": 13626,
    "deaths": 323,
    "recovered": 10582,
    "state": "Rajasthan",
}

state8 = {
    "active": 2308,
    "confirmed": 11426,
    "deaths": 486,
    "recovered": 8632,
    "state": "Madhya Pradesh",
}

state9 = {
    "active": 4528,
    "confirmed": 7944,
    "deaths": 134,
    "recovered": 4983,
    "state": "Haryana",
}

state10 = {
    "active": 2842,
    "confirmed": 3615,
    "deaths": 115,
    "recovered": 2570,
    "state": "Karnataka",
}

# List of Dictionaries
india = [state1, state2, state3, state4, state5, state6, state7, state8, state9, state10]
print("Length of India is: ", len(india))
print()

again_choice = "yes"

while again_choice == "yes":

    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Press 1 for filtering COVID-19 Data with 2 filters")
    print("Press 2 for Search By State")
    print("Press 3 for Sorting the Cases with 1 filter")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    choice = int(input("Whats Your Choice: "))

    if choice == 1:
        # 1. Filtering the data from Collection as expected by user
        filter1 = input("Please enter a filter 1st filter from [active | confirmed | deaths | recovered | state]: ")
        filter2 = input("Please enter a filter 1st filter from [active | confirmed | deaths | recovered | state]: ")

        for i in range(0, len(india)):
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("{}: {}\n{}: {}".format(filter1.upper(), india[i][filter1], filter2.upper(), india[i][filter2]))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()

    elif choice == 2:
        # 2. Searching from the data | Linear Search
        state = input("Enter the name of state to search: ")
        for i in range(0, len(india)):
            print("Matching {} with {}".format(state, india[i]["state"]))
            # if state == india[i]["state"]:
            if state.lower() == india[i]["state"].lower():
                print("State {} found, details below: ".format(state))
                print(india[i])
                break

    elif choice == 3:
        # 3. Sort the data | Bubble Sort
        sort_filter = input("Enter sorting field [active | confirmed | deaths | recovered ]: ")
        n = len(india)
        for i in range(0, n):
            for j in range(0, n - i - 1):
                if india[j]["active"] > india[j + 1]["active"]:
                    india[j], india[j + 1] = india[j + 1], india[j]

        print("Sorted as per {} cases: ".format(sort_filter))
        for i in range(0, len(india)):
            print("~~~~~~~~~~~~~~~~~~")
            print("{}: {}\n: {}".format("State", india[i]["state"], sort_filter.upper(), india[i][sort_filter]))
            print()


    else:
        print("Seems like you have not entered the correct choice")





