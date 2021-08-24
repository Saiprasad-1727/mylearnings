rawstar = input("ENter a number:")
try:
    ival = int(rawstar)
except:
    ival = -1
print("first",ival)

if ival > 0:
    print('nice work')
    if ival < 0:
        print('negative number')
elif ival == 0:
    print('Zero')
else:
    print("not a number")    