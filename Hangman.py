import getpass
def hangman():
 choice=getpass.getpass("enter the name:").lower()
 print("If you want to quit the game enter 'esc'")
 for i in range(len(choice)):
  alpha=input("please enter the alphabet number {0} from the given string: ".format(i))
  if alpha==choice[i]:
     print("Yes you are correct!")
     continue
  elif alpha=='esc':
    break
     
  else:
       while alpha!=choice[i]:
         alpha=input("enter the alphabet again please: ")
         if alpha=='esc':
           break
       if alpha==choice[i]:
         print("Yes you are correct!")
         continue
  if alpha=='esc':
    break
 if i==len(choice)-1:
    print("Congratulation! you are correct.The string is",choice)
hangman()
