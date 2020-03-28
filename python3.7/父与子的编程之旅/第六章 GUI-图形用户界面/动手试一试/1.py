import easygui as e
e.msgbox('This programe converts Fahrenheit to Celsius')
e.msgbox('Type in temperature in Fahrenheit')
fahrenheit=float(e.enterbox('输入温度值：'))
celsius=str((fahrenheit-32)*5.0/9)
e.msgbox("That is "+celsius+' degrees Celsius')

