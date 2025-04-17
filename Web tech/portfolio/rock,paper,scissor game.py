import random
rock='''
✊
'''
paper='''
✋
'''
scissor='''
✌️
'''
game_image=[rock,paper,scissor]
user_choice=int(input("enter ur choice:\n0 for rock\n1 for paper\n2 for scissor\n"))
print(game_image[user_choice])
computer_choice=random.randint(0,2)
print("computer choice")
print(game_image[computer_choice])
if computer_choice==user_choice:
    print('draw')
elif computer_choice>user_choice:
    print('computer win')
elif computer_choice<user_choice:
    print('you win')
elif computer_choice==0 and user_choice==2:
    print('computer win')
elif computer_choice==2 and user_choice==0:
    print('you win')
