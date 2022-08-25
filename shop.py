def shopping():
    cart = {}
    yes = True
    while yes:
        x = input("Name your product? ")
        y = int(input("How many? "))
        if x in cart:
            print(f'That is already in your cart.')
            u = input('Update quantity? ')
            if u.lower() == 'yes' or u.lower() == 'y':
                uq = int(input("What is the new amount? "))
                cart[x] = uq
                print(f'so far you have {cart}')
            else:
                continue
        cart[x] = y
        q = input("Anything else?")
        if q.lower()== 'no' or q.lower()== "quit" or q.lower()== 'n':
            break
        print(f'so far you have {cart}')

    edit = input('Would you like to edit your cart? or remove an item?')
    if edit == "y" or edit == "yes":
        newit= input(" what item would you like to edit?")
        newitnum = input("How many? ")
        cart[newit] = newitnum
    elif edit.lower() == 'del' or edit.lower() == 'delete':
        delitem = input('What would you like to remove? ')
        del cart[delitem]
        print(f'so far you have {cart}')
    else:
        print(f'okay! This is your cart. {cart}.')




shopping()