def get_one_item (main_cart, person_cart): 
    item = person_cart.pop(0)#### remove last item from last cart
    main_cart.append(item)#### add item to main cart
    return main_cart, person_cart
    ##allows returning both lists since we modified both

Members = ('Billy', 'Bob', 'Thorton')

Billy = ['apple','bananna', 'pear', 'grapes']
Bob = ['orange', 'water', 'coconut', 'broccoli']
Thorton = ['snickers', 'twizzlers', 'crunch', 'skittles']

for lst in Billy:
    print (lst)

for lst in Bob:
    print (lst)

for lst in Thorton:
    print (lst)

cart = []

cart, Billy = get_one_item(cart, Billy)

Bob = get_one_item(cart, Bob)

Thorton  = get_one_item(cart, Thorton)
print (cart)

