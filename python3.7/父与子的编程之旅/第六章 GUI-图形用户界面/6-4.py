import easygui
flavor=easygui.enterbox("What is your facorite ice cream flavor?",
                        default='Vanilla')
easygui.msgbox('You entered '+flavor)
