stop = 1
ls = 0
shopping_list = []

while stop == 1:
        another = input("Input what you want on your shopping list")
        shopping_list.append(another)
        stop = int(input("Would you like to continue with your shopping list? (0 or 1)"))
        if stop == 1:
            print(shopping_list)
        if stop == 0:
            print(shopping_list)



