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

    while True:
        try:
            self.name1 = input("Enter the name of the first person : ")
            self.acc1 = int(input("Enter the {}'s account number : ".format(self.name1)))
            self.balance1 = int(input("Enter the balance of the {}: ".format(self.name1)))
            self.name1 = self.name1.replace(" ","")
            if self.name1.isalpha() and isinstance(self.acc1, int) and isinstance(self.balance1, int):
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid input")
            continue
 def person1(self):
    while True:
      print("If you want to deposit the money type 'd' or if you want to withdraw type 'w' if you dont want anything enter 'no'")
      try:
       choice=input()
       if choice =='d' or choice =='w' or choice=='no':
         break
       else:
         raise ValueError
      except ValueError:
       print("invalid, Please enter the correct value")
    while True:
      if choice=='d':
       self.dep=int(input("enter the deposit was: "))
       self.rem=self.balance1+self.dep
       print("The money which was deposited to {} was : ".format(self.name1),self.dep)
       if self.rem<limit:
        print("{} bank has low balance".format(self.name1))
        print(self.rem)
        break
       else:
        print("{} bank balance".format(self.name1))
        print(self.rem)
        break
      elif choice=='w':
       self.wit=int(input("enter the withdraw value : "))
       if self.wit>self.balance1:
        print("No sufficient money")
        break
       else:
        self.rema=self.balance1-self.wit
        print("The money withdrawn which was withdrawn from {} account was: ".format(self.name1),self.wit)
        if self.rema<limit:
         print("{} bank has low balance".format(self.name1))
         print(self.rema)
         break
        else:
         print("{} bank balance".format(self.name1))
         print(self.rema)
         break
      else:
        break
 def person2(self):
    while True:
        try:
            self.name2 = input("Enter the name of the second person : ")
            self.acc2 = int(input("Enter the {}'s account number : ".format(self.name2)))
            self.balance2 = int(input("Enter the balance of the {}: ".format(self.name2)))
            self.name2 = self.name2.replace(" ","")
            if self.name2.isalpha() and isinstance(self.acc2, int) and isinstance(self.balance2, int):
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid input")
            continue
    while True:
      print("If you want to deposit the money type 'd' or if you want to withdraw type 'w' if you dont want anything enter 'no'")
      try:
       choice=input()
       if choice=='d' or choice=='w' or choice=='no':
        break
       else:
        raise ValueError
      except ValueError:
       print("invalid, Please enter the correct value")
    while True:
      if choice=='d':
       self.dep=int(input("enter the deposit: "))
       self.rem=self.balance1+self.dep
       print("The money which was deposited to {} account was : ".format(self.name1),self.dep)
       if self.rem<limit:
        print("{} account has low balance".format(self.name1))
        print(self.rem)
        break
       else:
        print("{} account balance".format(self.name1))
        print(self.rem)
        break
      elif choice=='w':
       self.wit=int(input("enter the withdraw value : "))
       if self.wit>self.balance1:
        print("No sufficient money")
        break
       else:
        self.rema=self.balance1-self.wit
        print("The money withdrawn from {} account was : ".format(self.name1),self.wit)
        if self.rema<limit:
         print("{} account has low balance".format(self.name1))
         print(self.rema)
         break
        else:
         print("{} account balance:".format(self.name1))
         print(self.rema)
         break
      else:
       break
    while True:
      print("If you want to deposit the money type 'd' or if you want to withdraw type 'w' if you dont want anything enter 'no'")
      try:
       choice=input()
       if choice=='d' or choice=='w' or choice=='no':
        break
       else:
        raise ValueError
      except ValueError:
       print("invalid, Please enter the correct value")
    while True:
      if choice=='d':
       self.dep1=int(input("enter the deposit was: "))
       self.remaining=self.balance2+self.dep1
       print("The money which was deposited to {} was : ".format(self.name2),self.dep1)
       if self.remaining<limit:
        print("{} account has low balance:".format(self.name2))
        print(self.remaining)
        break
       else:
        print("{} account balance:".format(self.name2),self.remaining)
        break
      elif choice=='w':
       self.wit1=int(input("enter the withdraw value : "))
       if self.wit1>self.balance2:
        print("No sufficient money")
        break
       else:
        self.remaining2=self.balance2-self.wit1
        print("The money withdrawn from {} account was : ".format(self.name2),self.wit1)
        if self.remaining2<limit:
          print("{} account has low balance".format(self.name2))
          print(self.remaining2)
          break
        else:
         print("{} account balance".format(self.name2))
         print(self.remaining2)
         break
      else:
        break
    while True:
      while bool(1):
       try:
        print("Do you want to do transactions. if yes enter 'y' if no enter 'n':")
        tr=input()
        if isinstance(tr,str) and (tr=='y' or tr=='n'):
          break
        else:
          raise ValueError
       except ValueError:
         print("Please enter a valid input")
         continue
      if tr=='y':
        while bool(1):
          try:
             print("If you want to transact from person one to person two enter 'p1' or if you want to transact from person two to person one enter 'p2'")
             inp=input()
             if isinstance(inp,str) and (inp=='p1' or inp=='p2'):
               break
             else:
               raise ValueError
          except ValueError:
           print("Please enter a valid input")
        if inp=='p1':
            while True:
              try:
                self.transaction=int(input("Enter the amount to be transacted : "))
                if type(self.transaction)==int:
                  break
                else:
                  raise ValueError
              except ValueError:
                print("Please enter a valid input")
            self.a=self.balance1-self.transaction
            self.b=self.balance2+self.transaction
            if self.balance1<=limit:
              print("The money transferred from first person account is : ",self.transaction)
              print("The account number {}, owner {} has low balance".format(self.acc1,self.name1))
              print(self.b)
              break
            else:
              print("The money transferred from {} account is : ".format(self.name1),self.transaction)
              print("The money recieved by {} is total of ".format(self.name2),self.b)
              break
        else:
            while True:
              try:
                self.transaction1=int(input("Enter the amount to be transacted : "))
                if type(self.transaction1)==int:
                  break
                else:
                  raise ValueError
              except ValueError:
                print("Please enter a valid input")
            self.a=self.balance2-self.transaction1
            self.b=self.balance1+self.transaction1
            if self.balance2<=limit:
              print("The money transferred from second person account is : ",self.transaction1)
              print("The account number {}, owner {} has low balance".format(self.acc2,self.name2))
              print(self.b)
              break
            else:
              print("The money transferred from {}'s account is : ".format(self.name2),self.transaction1)
              print("The money recieved by {} is total of ".format(self.name1),self.b)
              break
      else:
        break

b=Bank()
my_value=b.num
if my_value==1:
  b.person1()
else:
  b.person2() 
