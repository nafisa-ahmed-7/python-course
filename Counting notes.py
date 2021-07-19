def countCurrency(amount):
    notes = [500, 200, 100,50, 20, 10, 5, 1]
    temp = [0, 0, 0, 0, 0, 0, 0, 0]
    print("Currency Count:\n")
    for i, j in zip(notes,temp):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print(i, " : ", j)
amount = int(input("Enter the amount:\n"))
countCurrency(amount)