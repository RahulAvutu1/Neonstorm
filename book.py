import random as r
import pandas as pd

class Book:
 def __init__(self):
   self.c=None
   while(1):
    try:
      n=int(input("Please enter the number of books in the library : "))
      if isinstance(n,int):
        break
      else:
        raise ValueError
    except:
        print("Please enter a number")
        continue
   self.mydict={}
   self.i=0
   for self.i in range(n):
      self.out_key="Book"+str(self.i+1)
      self.indict={}
      self.indict['Name']=input("Please enter the book name here : ")
      self.indict['Author']=input("Please enter the name of the author : ")
      self.isbn=987
      self.isbn1=r.randint(1,10)
      self.isbn2=r.randint(14568,74792)
      self.isbn3=r.randint(0,100)
      self.isbn4=r.randint(100,1000)
      self.mylist=[self.isbn1,self.isbn2,self.isbn3,self.isbn4]
      self.isbn5 = "-".join(map(str, self.mylist))
      self.indict['ISBN code']=self.isbn5
      self.mydict[self.out_key]=self.indict
      self.df = pd.DataFrame(self.mydict).T[['Name', 'Author', 'ISBN code']] 
   print(self.df)
 def add(self):
      self.out_key = "Book" + str(len(self.mydict) + 1)
      self.indict={}
      self.indict['Name']=input("Please enter the book you want to add to the library : ")
      self.indict['Author']=input("Please enter the name of the author : ")
      print("Generating an ISBN code for the book")
      self.isbn=987
      self.isbn1=r.randint(1,10)
      self.isbn2=r.randint(14568,74792)
      self.isbn3=r.randint(0,100)
      self.isbn4=r.randint(100,1000)
      self.mylist=[self.isbn1,self.isbn2,self.isbn3,self.isbn4]
      self.isbn5 = "-".join(map(str, self.mylist))
      self.indict['ISBN code']=self.isbn5
      self.mydict[self.out_key]=self.indict
      self.df = pd.DataFrame(self.mydict).T[['Name', 'Author', 'ISBN code']]
      print(self.df)
 def remove(self):
  while bool(1):
    try:
         r=int(input("Please enter the number of books you want to remove : "))
         if isinstance(r,int) and r<=len(self.df):
          break
         else:
          raise ValueError
    except:
      print("Please enter a number or which is in range of data")
  i=0
  for i in range(r):
   while bool(1):
      try:
       self.r=input("Please enter the book you want to remove : ")
       if self.df['Name'].isin([self.r]).any():
        break
       else:
        raise ValueError
      except ValueError:
        print("Please enter the book which is present in the data")

   removed=self.df.loc[self.df['Name']==self.r]
   self.df=self.df.drop(self.df[self.df['Name']==self.r].index,axis=0)
   print("The Removed book data is")
   print(removed)   
   print("The updated library is : ")
   print(self.df)
 def checkout(self):
  if not self.df.empty:
    while True:
        try:
            self.c = input("Please enter the book you want to check out: ")
            date = input("Please input the date: ")
            if self.df['Name'].isin([self.c]).any() and isinstance(date, str):
                break
            else:
                raise ValueError
        except ValueError:
                 print("please enter a book which is there in data")
    self.remov = self.df.loc[self.df['Name'] == self.c]
    print("The checked out book on the date of {} is: ".format(date))
    print(self.remov)
    self.df = self.df.drop(self.df[self.df['Name'] == self.c].index, axis=0)
    print("The updated library is: ")
    print(self.df)
  else:
    print("There is no book to check out")
 def ret(self):
   if self.c!=None:  
     while True:
        try:
            self.re = input("Please enter the book you want to return: ")
            date = input("Please input the date: ")
            if isinstance(self.re, str) and isinstance(date, str):
                break
        except Exception as e:
            continue
     if self.c == self.re:
        print("The returned book on the date of {} is:".format(date))
        print(self.remov)
        ad = self.remov
     else:
        print("Sorry, the book doesn't exist or it hasn't been checked out")
        ad = pd.DataFrame(columns=['Name', 'Author', 'ISBN code'])
     self.df = pd.concat([self.df, ad], axis=0).sort_index()
     print("The updated library is:")
     print(self.df)
   else:
        print("There is no book checked out to return")
   self.c=None
  
 def display(self):
           print("The total books in the library are : ")
           print(self.df)
      
b=Book()
mydict1={
    1:'add',
    2:'remove',
    3:'checkout',
    4:'retur',
    5:'display',
}
print("1.Adding a book")
print("2.Removing a book")
print("3.Checking out the book")
print("4.returning the book")
print("5.Displaying the library")
print("6.Enter 0 for exit")
while True:
 while True:
   try:
     print("Please enter your option")
     item=int(input())
     if isinstance(item,int) and item in range(0,6):
             break
   except ValueError:
         print("Please enter a valid option")
 if item in range(1,6):
  if mydict1[item]=='add':
    b.add()
  elif mydict1[item]=='remove':
    b.remove()
  elif mydict1[item]=='checkout':
    b.checkout()
  elif mydict1[item]=='retur':
    b.ret()
  elif mydict1[item]=='display':
    b.display()
 elif item==0:
  break

