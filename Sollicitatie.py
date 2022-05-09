print('ill ask you some question if i dont like it you are out. ')
q1 = input('what is your name ?')
if q1 == 'tony' :
    raise AttributeError ('I dont like you :) ', q1)
q2 = input('How old are u ?')
if q2 == '20':
    raise ValueError ('oof you are to old ')
q3 = input('How tal are you in cm ?')
if q3 == '170':
    raise ZeroDivisionError ('to short way to short ')
print(' You are good ')