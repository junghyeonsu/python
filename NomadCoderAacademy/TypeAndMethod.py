a_string = "like this"
a_number = 3
a_float = 3.12
a_boolean = False
a_none = None
print(type(a_string))

a = [] #리스트 (수정가능)
a = () #튜플 (수정불가능)
a = {} #dictionary

# 포지션된 인자들말고 더 넣고싶으면 *args 를 쓰고
# key = value 로 된 인자도 넣고싶으면 **kwargs

# positional arguments 와 keyword arguments 로 나뉜다.
#   *args                     **kwargs
def plus(a,b , *args, **kwargs):
    print(args , kwargs)
    return a+b

plus(1,2,3,4,5,6,6,7,8,hello=True,id="22")

def plusAll(*args):
    a = 0
    for i in args:
        a += i
    print(a)

plusAll(1,2,3,4,5,6,7,8,9,10)