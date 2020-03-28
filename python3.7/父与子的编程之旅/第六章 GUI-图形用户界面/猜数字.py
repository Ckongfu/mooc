import easygui,random
secret=random.randint(1,99)
guess=0
tries=0
while guess!=secret and tries<8:
    guess=easygui.integerbox('Please guess a number:')
    if not guess:
        break
    elif guess<secret:
        easygui.msgbox(str(guess),'Your number is to low!')
    elif guess>secret:
        easygui.msgbox(str(guess),'Your number is to high!')
    tries=tries+1
if guess==secret:
    easygui.msgbox(guess,'Congratulation you guess the number!!!')
