import easygui

name=str(easygui.enterbox('What is your name?'))
roomnum=str(easygui.enterbox('What is your room number?'))
street=str(easygui.enterbox('What is your street number?'))
city=str(easygui.enterbox('Where are you from?'))
postnum=str(easygui.enterbox('What is your post number?'))
whole_addr=name+'\n'+roomnum+'\n'+street+'\n'+city+'\n'+postnum
easygui.msgbox(whole_addr)
