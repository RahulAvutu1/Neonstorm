import random as r
def rock_paper_scissors():
  count1=0
  count2=0
  try:
   n=int(input("Please enter the number of points required to win : "))
  except ValueError:
     print("Invalid. Input enter a valid number.")
  mylist=["Rock","Scissors","Paper"]
  while count1!=n and count2!=n:
    rand=r.choice(mylist)
    mydict={
        1:"Scissors",
        2:"Paper",
        3:"Rock"
    }
    print(mydict)
    try:
     ite=int(input("please enter your choice:"))
     if ite not in mydict:
       raise KeyError
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue
    except KeyError:
      print("Invalid input. Please enter a valid number.")
      continue
  
    if mydict[ite]=="Scissors" and rand=="Paper":
        count1=count1+1
        print("your choice:",mydict[ite])
        print("My choice:"+str(rand))
        print("Your score=",count1)
        print("My score=",count2)
    elif mydict[ite]=="Rock" and rand=="Scissors":
        count1+=1
        print("your choice:",mydict[ite])
        print("My choice:"+str(rand))
        print("Your score=",count1)
        print("My score=",count2)
    elif mydict[ite]=="Paper" and rand=="Rock":
        count1+=1
        print("your choice:",mydict[ite])
        print("My choice:"+str(rand))
        print("Your score=",count1)
        print("My score=",count2)
    elif mydict[ite]=="Paper" and rand=="Scissors":
        count2+=1
        print("your choice:",mydict[ite])
        print("My choice:"+str(rand))
        print("Your score=",count1)
        print("My score=",count2)
    elif mydict[ite]=="Rock" and rand=="Paper":
        count2+=1
        print("your choice:",mydict[ite])
        print("My choice:"+str(rand))
        print("Your score=",count1)
        print("My score=",count2)
    elif mydict[ite]=="Scissors" and rand=="Rock":
        count2+=1
        print("your choice:",mydict[ite])
        print("My choice:"+str(rand))
        print("Your score=",count1)
        print("My score=",count2)
    else:
      count1+=1
      count2+=1
      print("your choice:",mydict[ite])
      print("My choice:"+str(rand))
      print("Your score=",count1)
      print("My score=",count2)
  if count1>count2:
    print("Congratulations! you won")
  elif count1<count2:
    print("Sorry, you have lost the game")
  else:
    print("It's a Draw")
rock_paper_scissors()
