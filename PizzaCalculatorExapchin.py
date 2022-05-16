#=========================== varibales =========================#
pizzasmall=6
pizzamedium=10
pizzalarge=12.90
# ========================= func ===============================#
def question():
    global smallpizza,mediumpizza,largepizza
    smallpizza=int(input("antaal small pizza : "))
    mediumpizza=int(input("antaal medium pizza : "))
    largepizza=float(input("antaal large pizza : "))

# ========================= code here onder ====================#

print('Welcome what piaaz size do you like to have\nThe large one for 12.90$\nThe medium one for 10$\nThe small one for 6$ ? ')
try:
    question()

except ValueError :
    print('I think somthing went wrong pleas try again. ',)

else:
    print(f'total prijs {largepizza*pizzalarge+mediumpizza*pizzamedium+smallpizza*pizzasmall:.2f}')
