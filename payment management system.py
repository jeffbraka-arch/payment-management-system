from abc import ABC , abstractmethod
class Payment(ABC):
    def __init__(self,name,amount):

        
        if 0 >= amount:
            raise ValueError("invalid transaction amount !!!")
        
        self.name = name
        self.amount = amount
        


    def display_details(self):
        print(f"Name : {self.name}")
        print(f"Amount : {self.amount}")    


    @abstractmethod
    def process_payment(self):
        pass

class MpesaPayment(Payment):
    def __init__(self, name, amount,phone_number):

        if len(phone_number) == 10 and phone_number[:2]  in ("07", "01") and phone_number.isdigit():
          super().__init__(name, amount)
          self.phone_number = phone_number
        else:
            raise ValueError("invalid phone number")  

    def process_payment(self):
        print("Mpesa payment transaction is taking place....")

    def display_details(self):
        super().display_details() 
        print(f"Phone number : {self.phone_number}")   
        

class CardPayment(Payment):
    def __init__(self, name, amount,cardholder_name,expiry_date):
        super().__init__(name, amount)
        if len(expiry_date) != 5 or expiry_date[2] != "/" or not expiry_date[3:].isdigit() or not expiry_date[:2].isdigit():
          raise ValueError("incorrect card input detail") 
        month = int(expiry_date[:2])
        if month < 1 or month > 12 :
          raise ValueError("invalid expiry month")
        if not cardholder_name.strip():
            raise ValueError("Card holder name cannot be empty")
        self.cardholder_name = cardholder_name.strip()
        self.expiry_date = expiry_date

    def process_payment(self):
        print("Card payment is being processed....")

    def display_details(self):
        super().display_details()  
        print(f"Card holder's name : {self.cardholder_name}")
        print(f"Card expiry date : {self.expiry_date}")      

accounts = []
print("==== PAYMENT MANAGEMENT SYSTEM ====")
print("1.Mpesa")
print("2.Card")

choice = input("Enter your prefferd payment method : ")
if not choice.isdigit():
   print("please enter a digit to choose your prefferd payment option")
else:
 if choice == "1":
   #collect mpesa details and create mpesa object
   name = input("Enter your name : ")
   phone_number = input("enter your phone number : ")
  

   try:
     amount = int(input("Enter the amount you want to transact : "))
     mpesa1 = MpesaPayment(name,amount,phone_number)
     accounts.append(mpesa1)
   except ValueError as error:
     print(error) 

 elif choice == "2":
#collect card details and create card object
  name = input("Enter your name : ")
  cardholder_name = input("enter the name of the card : ")
  expiry_date = input("enter the expiry date of the card : ")

  try:
    amount = int(input("enter the amount you want to transact : " ))
    card1 = CardPayment(name,amount,cardholder_name,expiry_date)
    accounts.append(card1)
  except ValueError as error:
    print(error)
 else:
   print("please enter valid choice input")     
for account in accounts:
    account.display_details()
    account.process_payment()

