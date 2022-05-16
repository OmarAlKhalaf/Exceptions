# ================ code here onder =================#

def question1():

 question = int(input ('Give me a number between 1/10 '))
 if question  <=5 :
    print('Good one')

 elif question >=5 :
    print('Not good...')


try :
   question1()

except ValueError :
    print('I think somthing went wrong pleas try again. ')


else:
    while True :
        question2 = int(input('If you see Go up go up if you see Lower go Lower if you dont see anything that mean you are close\nGive me a number betwwen 50/100 : '))
        if question2 <=50:
            print('GO up ')
        elif question2 >=100:
            print('Lower')
        elif question2 == 76:
            print('Good nice jop')
            break


finally:
    print(' :D ')