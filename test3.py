import numpy as np

a = np.arange(10)**3
print("1부터 10까지 3자승 한 배열 a =",a)
print("a 배열의 두번째 인덱스 값 = ", a[2])
print("a 배열의 2:5 인덱스 값 = ", a[2:5])
a[0:6:2] = -1000    # from start to position 6, exclusive, set every 2nd element to -1000
print("a 배열의 0번째 부터 6번째 까지 모든 두번째 값에 -1000을 대입한 값 = ", a)
print("a 배열을 뒤집은 값  = ", a[ : :-1])          # reversed a
 #각 행마다 10씩 증가하는 배열 생성
def f(x,y):
    return 10*x+y

ab = np.fromfunction(f,(5,4),dtype=int)
print("각 행마다 10씩 증가하는 배열 생성\n",ab)
print("생성된 배열의 2행 3열 값 = ",ab[2,3])
print("생성된 배열 각행 2열 값 = ",ab[0:5, 1])
print("생성된 배열 각행 1행~2행 값 \n ",ab[1:3, : ])