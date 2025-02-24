import random as rd
class PIG:
    lis=list(range(1,7))
    flag=None
    def __init__(self):
        self.score1=0
        self.score2=0
        self.q=None
    def roll(self,count,n,p):
        s=0
        while True:
            if count==n:
                print('you rolled the dice {0} time(s)'.format(n))
                break
           
            c=input('Press enter to roll the dice or enter "hold" to hold the score or q to quit')
            
            if c.lower()=='q':
                self.q='q'
                s=0
                break
            if c.lower()=='hold':
                print(f'{p} holds the turns')
                break
            d=rd.choice(PIG.lis)
            if d==1:
                print(f'{p} rolled a 1,chance lost')
                s=0
                break
            if self.score1==100 or self.score2==100:
                print(f'{p} wins')
                break
            print('{0} rolled a {1}'.format(p,d))
            s=s+d
            count=count+1
        if self.q=='q':
            if p=='player_1':
             print(f'{p} quits and player_2 wins')
            else:
              print(f'{p} quits and player_1 wins')
            PIG.flag=2
            
        if p=='player_1':
         self.score1=self.score1+s
        else: 
           self.score2=self.score2+s
        print('Score of  player 1:',self.score1)
        print('Score of player 2:',self.score2)
        if self.score1>=100:
           print(f'{p} wins')
        elif self.score2>=100:
           print(f'{p} wins')
        return
        
    def roll1(self):
        while True:
          try:
             n=int(input('how many times does player_1 wants to roll?'))
             if n<0:
                 print('Try again')
                 continue
             break
          except ValueError:
           print('Try again please')
        count=0
        self.roll(count,n,'player_1')
        if PIG.flag==2:
           return
        else:
          PIG.flag=1
    def roll2(self):
         while True:
          try:
             n=int(input('how many times does player_2 wants to roll?'))
             if n<0:
                 print('Try again')
                 continue
             break
          except ValueError:
           print('Try again please')
         count=0
         self.roll(count,n,'player_2')
         if PIG.flag==2:
          return
         else:
            PIG.flag=0
p=PIG()
def fun(flag):
    match flag:
        case None:
            p.roll1()
        case 0:
            p.roll1()
        case 1:
            p.roll2()
        case _:
            return
def print_pig_rules():
    print("""
    Welcome to the Pig Dice Game!

    Rules:
    1. The game is played with a single six-sided die.
    2. Players take turns to roll the die as many times as they wish.
    3. On each roll:
       a. If the player rolls a 1, they score nothing for that turn and their turn ends.
       b. If the player rolls any other number, it is added to their turn total.
    4. A player can choose to 'hold' at any time:
       a. Holding adds their turn total to their overall score.
       b. The player's turn ends and passes to the other player.
    5. The first player to reach or exceed 100 points wins the game.
    6. If a player chooses to quit, the other player automatically wins.

    Enjoy the game and may the best roller win!
    """)
print_pig_rules()

while p.score1<100 and p.score2<100 :
  if PIG.flag!=2:
    fun(PIG.flag)  
  else:
     break 
