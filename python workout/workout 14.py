# restaurant 

MENU = {'sandwich': 10, 'tea': 7, 'salad': 9, 'juice':20}

def restaurant():
    total_bill = 0; 

    while True:
        order_item = input('Order:')

        if order_item in MENU:
            total_bill = total_bill + MENU[order_item]
            print(f'{order_item} costs {MENU[order_item]}, your total is {total_bill}.')
        elif not order_item:
            print(f'Your total is {total_bill}.')
            break
        else:
            print(f'Sorry, We are out of {order_item} at this moment :(')
        

restaurant()