import random as r
import getpass
class Shop:
  def __init__(self):
    pass
  def initialize(self):
                           print("The items we provide you with")
                           self.mydict={
                                  1:"Electronics",
                                  2:"Cosmetics",
                                  3:"Sporting goods",
                                  4:"Food",
                                  5:"Furninture",
                                  6:"Medics"
                           }
                           print(self.mydict)
                           while True:
                                      try:
                                          self.inpt=int(input("enter the type of the device you are looking for in numbers of 1-6: "))
                                          if self.inpt in self.mydict:
                                              break
                                          else:
                                            raise KeyError
                                      except ValueError:
                                               print("Invlaid. Please e\nte again")
                                               continue
                                      except KeyError:
                                               print("Invalid. Please enter again")
class Electronics(Shop):
       def __init__(self):
         super(). __init__()
       def Elec(self):
                      print("Enter the name of the appliance : ")
                      self.name=input()
                      print("If you want to buy the appliance please enter 'b' or if you want to enter to your cart 'c'")
                      while True:
                        try:
                          choice=input()
                          if choice=='b' or choice=='c':
                            break
                        except ValueError:
                          print("Please enter valid input")
                      if choice=='b':
                        print("Please enter the range of the devcice if it is small enter 's' if it is medium enter 'm' or large enter 'l'")
                        while True:
                          try:
                            range=input()
                            if range=='s' or 'm' or 'l':
                              break
                            else:
                              raise ValueError
                          except ValueError:
                                print("Please enter valid input")
                        if range=='s':
                          self.rand=r.randint(500,2000)
                          print(f"The cost of the item you want to buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,6)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                        elif range=='m':
                          self.rand=r.randint(1500,4000)
                          print(f"The cost of the item you want yto buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,8)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                        else:
                          self.rand=r.randint(4000,7000)
                          print(f"The cost of the item you want yto buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,10)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                      else:
                        print("The item had added to your cart")
                        self.cart=self.name
                        print(f"The item which was added is {self.cart}")
class Cosmetics(Shop):
       def __init__(self):
         super(). __init__()
       def Cosmo(self):
                      print("Enter the name of the Cosmetics : ")
                      self.name=input()
                      print("If you want to buy the cosmetic product please enter 'b' or if you want to add to your cart enter 'c'")
                      while True:
                        try:
                          choice=input()
                          if choice=='b' or choice=='c':
                            break
                        except ValueError:
                          print("Please enter valid input")
                      if choice=='b':
                        print("If you are buying one piece enter 1 or if you are buying in set enter 2")
                        while True:
                          try:
                            range=int(input())
                            if range==1 or 2:
                              break
                            else:
                              raise ValueError
                          except ValueError:
                                print("Please enter valid input")
                        if range==1:
                          self.rand=r.randint(500,1000)
                          print(f"The cost of the item you want to buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,6)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                        else:
                          self.rand=r.randint(4000,7000)
                          print(f"The cost of the item you want to buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,10)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                      else:
                        print("The item had added to your cart")
                        self.cart=self.name
                        print(f"The item which was added is {self.cart}")
class Sports(Shop):
       def __init__(self):
         super(). __init__()
       def Sport(self):
                      print("Enter the name of the sports goods : ")
                      self.name=input()
                      print("If you want to buy the sports goods please enter 'b' or if you want to enter to your cart 'c'")
                      while True:
                        try:
                          choice=input()
                          if choice=='b' or choice=='c':
                            break
                        except ValueError:
                          print("Please enter valid input")
                      if choice=='b':
                        print("Please enter the range of the sports good, if it is small enter 's' if it is medium enter 'm' or large enter 'l'")
                        while True:
                          try:
                            range=input()
                            if range=='s' or 'm' or 'l':
                              break
                            else:
                              raise ValueError
                          except ValueError:
                                print("Please enter valid input")
                        if range=='s':
                          self.rand=r.randint(1000,2000)
                          print(f"The cost of the item you want yto buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,6)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                        elif range=='m':
                          self.rand=r.randint(1500,4000)
                          print(f"The cost of the item you want to buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,8)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                        else:
                          self.rand=r.randint(5000,10000)
                          print(f"The cost of the item you want yto buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,10)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                      else:
                        print("The item had added to your cart")
                        self.cart=self.name
                        print(f"The item which was added is {self.cart}")

class Food(Shop):
       def __init__(self):
         super(). __init__()
       def fod(self):
                      print("Enter the name of the food item : ")
                      self.name=input()
                      print("If you want to buy the food item please enter 'b' or if you want to enter to your cart 'c'")
                      while True:
                        try:
                          choice=input()
                          if choice=='b' or choice=='c':
                            break
                        except ValueError:
                          print("Please enter valid input")
                      if choice=='b':
                        print("Please mention the range of pack. if it is small pack fro one member enter 's' if it is medium pack for 2-3 members enter 'm' or if it is large pack like for a whole family enter 'l'")
                        while True:
                          try:
                            range=input()
                            if range=='s' or 'm' or 'l':
                              break
                            else:
                              raise ValueError
                          except ValueError:
                                print("Please enter valid input")
                        if range=='s':
                          self.rand=r.randint(500,700)
                          print(f"The cost of the item you want to buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,6)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                        elif range=='m':
                          self.rand=r.randint(700,1000)
                          print(f"The cost of the item you want yto buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,8)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                        else:
                          self.rand=r.randint(1000,1500)
                          print(f"The cost of the item you want yto buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,10)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                      else:
                        print("The item had added to your cart")
                        self.cart=self.name
                        print(f"The item which was added is {self.cart}")
class Furniture(Shop):
       def __init__(self):
         super(). __init__()
       def Fur(self):
                      print("Enter the name of the furniture : ")
                      self.name=input()
                      print("If you want to buy the furniture please enter 'b' or if you want to enter to your cart 'c'")
                      while True:
                        try:
                          choice=input()
                          if choice=='b' or choice=='c':
                            break
                        except ValueError:
                          print("Please enter valid input")
                      if choice=='b':
                        print("Please enter the range of the furniture if it is small enter 's' if it is medium enter 'm' or large enter 'l'")
                        while True:
                          try:
                            range=input()
                            if range=='s' or 'm' or 'l':
                              break
                            else:
                              raise ValueError
                          except ValueError:
                                print("Please enter valid input")
                        if range=='s':
                          self.rand=r.randint(13000,16999)
                          print(f"The cost of the item you want to buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,6)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                        elif range=='m':
                          self.rand=r.randint(17000,29999)
                          print(f"The cost of the item you want yto buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,8)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                        else:
                          self.rand=r.randint(30000,45000)
                          print(f"The cost of the item you want yto buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,12)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                      else:
                        print("The item had added to your cart")
                        self.cart=self.name
                        print(f"The item which was added is {self.cart}")
class Medics(Shop):
       def __init__(self):
         super(). __init__()
       def Med(self):
                      print("Enter the name of the Medics : ")
                      self.name=input()
                      self.pra=input("Enter the type of Medic : ")
                      print("If you want to buy the product please enter 'b' or if you want to add to your cart enter 'c'")
                      while True:
                        try:
                          choice=input()
                          if choice=='b' or choice=='c':
                            break
                        except ValueError:
                          print("Please enter valid input")
                      if choice=='b':
                        print("If you are buying one piece enter 1 or if you are buying in set enter 2")
                        while True:
                          try:
                            range=int(input())
                            if range==1 or 2:
                              break
                            else:
                              raise ValueError
                          except ValueError:
                                print("Please enter valid input")
                        if range==1:
                          self.rand=r.randint(400,699)
                          print(f"The cost of the item you want to buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,6)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                        else:
                          self.rand=r.randint(700,1000)
                          print(f"The cost of the item you want to buy is {self.rand}, If you want to confirm buying it enter y or enter n")
                          while True:
                            try:
                              dec=input()
                              if dec=='y' or 'n':
                                break
                            except ValueError:
                              print("Invalid. Please enter a valid number")
                          if dec=='y':
                            print("Please enter the card details here : ")
                            self.acc_num=input("Enter the account number : ")
                            self.cvv=getpass.getpass("Enter the cvv number : ")
                            self.pin=getpass.getpass("enter the pin number : ")
                            rand1=r.randint(1,10)
                            print("Order is successfully placed the delivery will arrive in {} days".format(rand1))
                          else:
                            print("Buying of the item is failed")
                      else:
                        print("The item had added to your cart")
                        self.cart=self.name
                        print(f"The item which was added is {self.cart}")

s=Shop()
e=Electronics()
s.initialize()
c=Cosmetics()
sp=Sports()
fu=Furniture()
f=Food()
m=Medics()
my_value=s.inpt
if my_value==1:
  e.Elec()
elif my_value==2:
  c.Cosmo()
elif my_value==3:
   sp.Sport()
elif my_value==4:
  f.fod()
elif my_value==5:
    fu.Fur()
else:
    m.Med()


