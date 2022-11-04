a = int(input('birinchi sonni kiriting: '))
amal1 = input("Amallardan birini tanlang +,*,/,-:        ")
b = int(input('ikkinchi sonni kiriting: '))
amal2 = input("Amallardan birini tanlang +,*,/,-:        ")
c = int(input('uchinchi sonni kiriting: '))

if amal1 == '+' and amal2 == '+':
    print("Natijangiz: " , a+b+c)
elif amal1 == '+' and amal2 =='-':
    print("Natijangiz: " , a+b-c)
elif amal1 == '+' and amal2 == '*':
    print("Natijangiz: " , (a+b)*c)
elif amal1 == '+' and amal2 == '/':
    print("Natijangiz: " , (a+b)/c)
elif amal1 == '-' and amal2 =='+':
    print("Natijangiz: " ,a-b+c)
elif amal1 == '-'and amal2 =='-':
    print("Natijangiz: " , a-b-c)
elif amal1 == '-' and amal2 == '*':
    print("Natijangiz: " , (a-b)*c)
elif amal1 == '-' and amal2 == '/':
    print("Natijangiz: " , (a-b)/c)
elif amal1 == '*' and amal2 == '+':
    print("Natijangiz: " ,a*b+c)
elif amal1 == '*' and amal2 =='-':
    print("Natijangiz: " , a*b-c)
elif amal1 == '*' and amal2 == '*':
    print("Natijangiz: " , a*b*c)
elif amal1 == '*' and amal2 == '/':
    print("Natijangiz: " , a*b/c)
elif amal1 == '/' and amal2 == '+':
    print("Natijangiz: " ,a/b+c)
elif amal1 == '/' and amal2 =='-':
    print("Natijangiz: " , a/b-c)
elif amal1 == '/' and amal2 == '*':
    print("Natijangiz: " , a/b*c)
elif amal1 == '/' and amal2 == '/':
    print("Natijangiz: " , a/b/c)
else:
    print("siz kiritgan amal tizimda mavjud emas")




