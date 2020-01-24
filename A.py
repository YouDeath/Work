
def StoVandt_dec(AtoVandt):
    def StoVandt(v1,v2,t):
        a = AtoVandt(v1,v2,t)
        S = v1*t+(a*t*t)/2
        print(S)
        return S
    return StoVandt

def AtoVandt(v1,v2,t):
    a = (v2-v1)/t
    return a
try:
    v1 = int(input("Введите значение начальной скорости"))
    v2 = int(input("Введите значение конечной скорости"))
    t = int(input("Введите время разгона"))
    a = AtoVandt(v1,v2,t)
    StoVandt_dec(AtoVandt)(v1,v2,t)
except ZeroDivisionError:
    print("Сеньёр, вы дибил, время должно быть больше 0!")
except ValueError:
    print("Ещё раз ты введёшь не число, когда тебя об это не просёт и тебе будет очень плохо!")
else:
    print("Так пойдёт!")
    print("Ускорение = ",a)


