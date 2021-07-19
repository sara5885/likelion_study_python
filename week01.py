from random import *

dice1=randint(1,6)
dice2=randint(1,6)
# dice=[dice1,dice2]
print('주사위 던지기')
print('주사위 1: {0}'.format(dice1))
print('주사위 2: {0}\n'.format(dice2))

print('실행할 연산의 종류를 입력하세요.')
print('1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.나머지 구하기') 
num=input('연산 종류 : ')

result=0
if(num=='1'):
    result=dice1+dice2
    print('덧셈 결과: '+str(result)+'\n')
elif(num=='2'):
    result=dice1-dice2
    print('뺄셈 결과: '+str(result)+'\n')
elif(num=='3'):
    result=dice1*dice2
    print('곱셈 결과: '+str(result)+'\n')
elif(num=='4'):
    result=dice1//dice2
    print('나눗셈 결과: '+str(result)+'\n')
elif(num=='5'):
    result=dice1%dice2
    print('나머지 결과: '+str(result)+'\n')

print('별찍기')
for i in range(result):
    print('*'*(i+1))