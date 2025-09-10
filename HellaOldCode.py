Dist = input('How far are you running in km? ')
Dist = int(Dist)
if 0 <= Dist <= 10:
    Ask = input('Are you running the short distance event? (yes/no) ')
    if Ask.lower() == 'yes':
        print("ok noted")
    else:
        print('ok')
elif Dist <= 21:
    Ask = input('Are you running the medium distance event? (yes/no) ')
    if Ask.lower() == 'yes':
        print("ok noted")
    else:
        print("ok")
elif Dist <= 42:
    Ask = input('Are you running the long distance event? (yes/no) ')
    if Ask.lower() == 'yes':
        print("ok noted")
    else:
        print('ok')
elif Dist > 42:
    Ask = input('Are you running the Ultra distance event? (yes/no) ')
    if Ask.lower() == 'yes':
        print("ok noted")
    else:
        print('ok')