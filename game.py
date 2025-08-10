from main import my_list
from test import SM



class Brain():
    def __init__(self):
        self.tx = my_list
        self.stick_man = SM
        self.result = len(self.tx) * ["_"]
        self.wrong_count = 0
        
     
             
    def player_quest(self,letter): #player input
            letter_found = False
            for index, i in enumerate(self.tx):
                if i == letter:
                    self.result[index] = letter
                    letter_found = True       
            if not letter_found:
                self.wrong_count +=1
                print(self.wrong_count)
            return f'word is : {self.result}'
                        

                
                
    def board(self):
        h = ''
        b = ''
        l1 = ''
        r1 = ''
        l2 = ''
        r2 = ''
        
        if self.wrong_count >= 1:
            h = SM.head
        if self.wrong_count >= 2:
            b = SM.body
        if self.wrong_count >= 3:
            l1 = SM.hand_left
        if self.wrong_count >= 4:
            r1 = SM.hand_right
        if self.wrong_count >= 5:
            l2 = SM.foot_left
        if self.wrong_count >= 6:
            r2 = SM.foot_right


        print(f'   _____\n'
              f'  |     |\n'
              f'  |     |\n'
              f'  |     |\n'
              f'  |     {h}\n'
              f'  |    {l1}{b}{r1}\n'
              f'  |    {l2} {r2}\n'
              f'__|__ \n')    

         


    
b = Brain()
b.board()
while True:

    play_inp = input('plese add latter: ')
    print(b.player_quest(play_inp))
    b.board()
    
    
    

