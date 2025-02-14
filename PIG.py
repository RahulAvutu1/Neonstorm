import random as rd
class PIG:
    lis=list(range(1,7))
    flag=None
    def __init__(self):
        self.score1=0
        self.score2=0
        self.q1=None
        self.q2=None
    def roll1(self):
        s=0
        n=int(input('how many times does player 1 wants to roll?'))
        count=0
        print('Player 1 turn to roll the dice')
        while True:
            if count==n:
                print('you rolled the dice {0} times'.format(n))
                break
            c=input('Press enter to roll the dice or enter "hold" to hold the score or q to quit')
            if c.lower()=='q':
                self.q1='q'
                s=0
                break
            if c.lower()=='hold':
                print('player 1 holds the turns')
                break
            d=rd.choice(PIG.lis)
            if d==1:
                print('player 1 rolled a 1 chance lost')
                s=0
                break
            if self.score1==100:
                print('player 1 wins')
                break
            print('player 1 rolled a {0}'.format(d))
            s=s+d
            count=count+1
        if self.q1=='q':
            print('player 1 quits and player 2 wins')
            PIG.flag=2
            return
        self.score1=self.score1+s
        print('player 1 score is:')
        print(self.score1)
        PIG.flag=1
    def roll2(self):
         s=0
         n=int(input('how many times does player 2 want to roll?'))
         count=0
         print('Player 2 turn to roll the dice')
         while True:
            if count==n:
                print(f'you rolled the dice {n} times')
                break
            c=input('Press enter to roll the dice or enter "hold" to hold the score or q to quit')
            if c.lower()=='q':
                self.q2='q'
                s=0
                break
            if c.lower()=='hold':
                print('player 2 holds the turns')
                break
            d=rd.choice(PIG.lis)
            if d==1:
                print('player 2 rolled a 1 chance lost')
                s=0
                break
            if self.score2==100:
                print('player 2 wins')
                break
            print('player 2 rolled a {0}'.format(d))
            s=s+d
            count=count+1
         if self.q2=='q':
            print('player 2 quits and player 1 wins')
            PIG.flag=2
            return
         self.score2=self.score2+s
         print('player 2 score is:')
         print(self.score2)
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

while p.score1<100 and p.score2<100 and PIG.flag!=2:
    fun(PIG.flag)   