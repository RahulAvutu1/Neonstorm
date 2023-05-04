limit=200
class Bank:
 def __init__(self):
    while bool(1):
      try:
       print("Enter the number of persons: ")
       self.num=int(input())
       if self.num==1 or self.num==2:
         break
       else:
         raise ValueError
      except ValueError:
       print("Please enter either 1 or 2")

    while bool(1):
     try:
      self.name1=input("enter the name of first person : ")
      self.name1=self.name1.replace(" ","")
      if self.name1.isalpha():
       break
      else:
        raise ValueError
     except ValueError:
      print("Please input the valid input")
     except KeyError:
       print("Please input the valid input")
    while bool(1):
     try:
      self.acc1=int(input("enter the firt person account number : "))
      break
     except ValueError:
      print("Please input the valid input")
     except KeyError:
      print("Please input the valid input")
    while bool(1):
     try:
      self.balance1=int(input("enter the balance of first person : "))
      break
     except ValueError:
      print("Please input the valid input")
     except KeyError:
      print("Please input the valid input")
 def person1(self):
    while True:
      print("If you want to deposit the money type 'd' or if you want to withdraw type 'w'")
      try:
       choice=input()
       if choice =='d' or choice =='w':
         break
       else:
         raise ValueError
      except ValueError:
       print("invalid, Please enter the correct value")
    while True:
      if choice=='d':
       self.dep=int(input("enter the deposit was: "))
       self.rem=self.balance1+self.dep
       print("The money which was deposited : ",self.dep)
       if self.rem<limit:
        print("Your bank has low balance")
        print(self.rem)
        break
       else:
        print("Your bank balance")
        print(self.rem)
        break
      else:
       self.wit=int(input("enter the withdraw value : "))
       if self.wit>self.balance1:
        print("No sufficient money")
        break
       else:
        self.rema=self.balance1-self.wit
        print("The money withdrawn is : ",self.wit)
        if self.rema<limit:
         print("Your bank has low balance")
         print(self.rema)
         break
        else:
         print("Your bank balance")
         print(self.rema)
         break
 def person2(self):
    while True:
        try:
            self.name2 = input("Enter the name of the second person: ")
            self.acc2 = int(input("Enter the second person's account number: "))
            self.balance2 = int(input("Enter the balance of the second person: "))
            self.name2 = self.name2.replace(" ","")
            if self.name2.isalpha() and isinstance(self.acc2, int) and isinstance(self.balance2, int):
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid input")
            continue
    while True:
      print("If you want to deposit the money type 'd' or if you want to withdraw type 'w'")
      try:
       choice=input()
       if choice=='d' or choice=='w':
        break
       else:
        raise ValueError
      except ValueError:
       print("invalid, Please enter the correct value")
    while True:
      if choice=='d':
       self.dep=int(input("enter the deposit: "))
       self.rem=self.balance1+self.dep
       print("The money which was deposited : ",self.dep)
       if self.rem<limit:
        print("Your bank has low balance")
        print(self.rem)
        break
       else:
        print("Your bank balance")
        print(self.rem)
        break
      else:
       self.wit=int(input("enter the withdraw value : "))
       if self.wit>self.balance1:
        print("No sufficient money")
        break
       else:
        self.rema=self.balance1-self.wit
        print("The money withdrawn is : ",self.wit)
        if self.rema<limit:
         print("Your bank has low balance")
         print(self.rema)
         break
        else:
         print("Your bank balance")
         print(self.rema)
         break
    while True:
      print("If you want to deposit the money type 'd' or if you want to withdraw type 'w'")
      try:
       choice=input()
       if choice=='d' or choice=='w':
        break
       else:
        raise ValueError
      except ValueError:
       print("invalid, Please enter the correct value")
    while True:
      if choice=='d':
       self.dep1=int(input("enter the deposit was: "))
       self.remaining=self.balance2+self.dep1
       print("The money which was deposited : ",self.dep1)
       if self.remaining<limit:
        print("Your bank has low balance")
        print(self.remaining)
        break
       else:
        print("Your bank balance")
        print(self.remaining)
        break
      else:
       self.wit1=int(input("enter the withdraw value : "))
       if self.wit1>self.balance2:
        print("No sufficient money")
        break
       else:
        self.remaining2=self.balance2-self.wit1
        print("The money withdrawn is : ",self.wit1)
        if self.remaining2<limit:
          print("Your bank has low balance")
          print(self.remaining2)
          break
        else:
         print("Your bank balance")
         print(self.remaining2)
         break

b=Bank()
my_value=b.num
if my_value==1:
  b.person1()
else:
  b.person2() 
