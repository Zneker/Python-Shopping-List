stop = 1
limit = int(input("Input your limit"))
ls = 0
shopping_list = []

while stop == 1:

    if ls==limit:
        print("You've reached the limit, restart the program and pay $0.00 for another go")

    else:
        another = input("Input what you want on your shopping list")
        shopping_list.append(another)
        ls = ls + 1
        stop = int(input("Would you like to continue with your shopping list? (0 or 1)"))
        if stop == 1:
            print(shopping_list)
        if stop == 0:
            print(shopping_list)



