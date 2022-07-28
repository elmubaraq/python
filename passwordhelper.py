
class Helper(object):
    def __init__(self, password):
        self.password = password

    def passwordCheck(self):
        password = self.password
        length=len(password)
        print('length=',length, 'of 8')
        if True in[Num.isdigit() for Num in password]:
        
                Num=True
        else:
            Num=False
        print('Num=',Num)

        if True in [Upper.isupper() for Upper in password]:
                Upper=True
        else:
            Upper=False
        print('Upper=',Upper)

        if True in [Lower.islower() for Lower in password]:
                Lower=True
        else:
            Lower=False
        print('Lower=',Lower)
        
        if True in [Char.isalpha() for Char in password]:
                Char=True
        else:
                Char=False
        print('Char=',Char)
        if ( length>=8 and Num and Char and Upper and Lower):
            return 'Password Strength is Strong'
        else:
            return 'Password Strength is Weak'
    
#print(passwordCheck('fdshjhLhdjhj5'))


'''def test(case):
    for i in case:
      if  i.isdigit():
        return True
    else:
        return False

print(test('gdj1hkjgdb'))'''