#1. create a function enterProducts()
def enterProducts():
    BuyingData = {} #store data in key_value dictionary format
    EnterDetails = True
    while EnterDetails==True:
        Choose = int(input('Press 1 or 2\n1.Add Product\n2.Quit\n'))
        if Choose==1:
            product = int(input('Select the item number you want to buy\n1.Biscuit  2500MMK\n2.Egg  400MMK\n3.Cake  15000MMK\n4.Apple   1000MMK\n5.Onion    3000MMK\n'))
            quantity = int(input('Enter Quantity: '))
            BuyingData.update({product:quantity})   # use update() dictionary function to store data
        elif Choose==2:
            EnterDetails = False
        else:
            print('Plese select the correct option!')
    return BuyingData


#2. create function to calculate the price (subTotal)
def getPrice(product,quantity):
    #assign price of each item
    priceData = {
        1:2500,
        2:400,
        3:15000,
        4:1000,
        5:3000
        }
    #match product_id with name
    product_name ={
        1:'Biscuit',
        2:'Egg',
        3:'Cake',
        4:'Apple',
        5:'Onion'
        }
    #calculate the subTotal price
    subTotal = priceData[product]*quantity
    print(f'{product_name[product]} : MMK {priceData[product]} x {quantity} = {subTotal} MMK')
    print(f'The Original Price= {subTotal} MMK')
    return subTotal


#3. create getDiscount() function
def getDiscount(billAmount,Membership):
    discount = 0
    if billAmount>=10000:
        if Membership=='Gold':
            discount=20       # get 20% discount for gold user
            billAmount *=0.8  # give 80% of the original amount
        elif Membership=='Silver':
            discount=10       # get 10% discount for silver user
            billAmount *=0.9  # give 90% of the original amount
        elif Membership=='Bronze':
            discount=5        # get 5% discount for silver user
            billAmount *=0.95 # give 95% of the original amount
        else:
            print('You are not a membership')
    
        print(f'For {Membership} Membership Customer, {discount} %  discount.')
        print(f'Total Price = {billAmount} MMK')
    else:
        print('Your Purchase must be at least 10000 MMK')
        print("You won't get any discount this time")
        print(f'Total Price = {billAmount} MMK')
    print('Thank you for your support')
  


#create a function for final bill payment
def makeBill(BuyingData,Membership):
    billAmount=0
    for x,y in BuyingData.items():
        billAmount+=getPrice(x,y)
    getDiscount(billAmount,Membership)
    #print(f'The total amount = {billAmount} MMK')

BuyingData = enterProducts() #new variable global scope
Membership=input('Enter Customer Membership:\nGold      Silver      Bronze\n')
makeBill(BuyingData,Membership)

'''
python accept both local and global scope  of the same variable_name
a function need to be returned and put the returned value to the variable_name if they want to reuse

'''

