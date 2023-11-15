#Akire Cormier, CIS261, Invoice Line Item Calculator
def item_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("That decimal is invalid, try again.")
            
def item_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("That integer is invalid, try again.")
            
if __name__ == "__main__":
    print("The Invoice Line Item Calculator\n")
          
    answer = "yes"
    while answer.lower() == "yes":
        price = item_price()
        quantity = item_quantity()
        
        total = price * quantity
        
        print()
        print("PRICE:  ", f"{price: .2f}")
        print("QUANTITY:  ", quantity)
        print("TOTAL:  ", f"{total: .2f}")
        answer = input("Enter another item? (yes/no): ")
        print()
        
print("See ya!")

    
                
