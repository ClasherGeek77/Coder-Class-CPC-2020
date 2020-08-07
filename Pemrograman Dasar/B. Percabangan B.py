def type_condition(v):
    if type(v) is str:
        print('kata')
    elif type(v) is int:
        if v == 0:
            print('nol')
        elif v>0:
            print('bilangan bulat positif')
        else:
            print('bilangan bulat negatif')

checkData = input()
try:
    checkData = int(checkData)
except Exception:
    pass
type_condition(checkData)