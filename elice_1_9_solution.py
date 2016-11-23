'''
Introduction to Numpy
이전 프로그래밍 과제에 이어서 이제 행렬의 모양을 바꾸고, 나누고, 붙이는 방법에 대해 연습하겠습니다.

numpy.ndarray.shape
Numpy의 배열에서 shape는 쉽게 말하면 배열의 모양과 같은 것입니다. 이를테면 \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} (​1​3​​​2​4​​) 는 (2, 2)(2,2) 의 모양을, \begin{pmatrix} 1 & 2 & 3 & 4 \end{pmatrix}(​1​​​2​​​3​​​4​​) 는 (1, 4)(1,4) 의 모양을 가지게 됩니다. 만약 3차원 3 \times 3 \times 33×3×3 array의 경우 (3, 3, 3)(3,3,3) 의 모양도 가질 수 있습니다.

Numpy.array 배열의 모양을 확인하려면 다음과 같은 코드를 사용할 수 있습니다. (2, 3)의 결과가 나오는 것을 볼 수 있습니다.

A = numpy.array([[1, 2, 3], [4, 5, 6]])
print(A.shape)
numpy.ndarray.reshape
Numpy의 재미있는 기능 중 하나는 배열의 모양을 원하는 대로 바꿀 수 있다는 것입니다. 이를테면, 2 \times 42×4 배열을 4 \times 24×2 또는 1 \times 81×8 과 같은 모양으로 원하는 대로 바꿀 수 있습니다. 다만, 이 때 바뀐 모양에 있는 원소의 수가 같지 않다면 (이를테면 2 \times 22×2 에서 4 \times 44×4로) 에러가 발생하게 됩니다.

다음 명령어를 실행하면서 numpy가 배열 내의 원소의 순서를 어떻게 지키면서 모양을 바꾸는지 테스트해보기 바랍니다. reshape() 안에 들어가는 파라미터는 튜플 (tuple) 이기 때문에 괄호의 개수에 주의하기 바랍니다.

A = numpy.array([[1, 2, 3], [4, 5, 6]])
print(A)
B = A.reshape((3, 2))
print(B)
numpy.concatenate
Numpy를 통해 여러 개의 배열을 한 개로 쉽게 합칠 수 있습니다. 합치는 방법에는 두 가지가 있는데 X축 방향으로 합치는 것과 Y축 방향으로 합치는 것입니다. 이것은 numpy.concatenate에 들어가는 axis 라는 파라미터를 통해 제어할 수 있습니다.

axis = 0: Y축 (세로 방향) 으로 설정합니다.
axis = 1: X축 (가로 방향) 으로 설정합니다.
다음 예제를 통해 살펴보겠습니다. 이전처럼 괄호에 주의하기 바랍니다.

A = numpy.array([[1, 2], [3, 4]])
B = numpy.array([[5, 6], [7, 8]])
C_Y = numpy.concatenate((A, B), axis = 0)
print(C_Y)
C_X = numpy.concatenate((A, B), axis = 1)
print(C_X)
numpy.split
마지막으로 split 함수에 대해 배우겠습니다. numpy.split은 배열을 여러 개의 크기로 나누어줍니다. 나누는 방법은 X축, 그리고 Y축을 기준으로 나누는 두 가지의 방법이 있으며 numpy.concatenate의 axis와 동일하게 작동합니다. 또한 두 번째 파라미터에 * 숫자 N을 넣으면 배열을 N개 동일한 크기의 배열들로 나누고 * 리스트를 넣으면 리스트 안의 숫자들 번째 인덱스에서 배열을 나눕니다. 예를 들어 [2, 3]이 입력될 경우 다음과 같이 나뉘게 됩니다.

 0   1   2   3   4   5   6 ...
[  X   X | X | X   X   X   ...
         ^   ^
         split!
마찬가지로 예제와 함께 배우겠습니다.

A = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13 ,14 ,15, 16]])
print(A)
slice_Y_equal_size = numpy.split(A, 2, axis = 0)
print(slice_Y_equal_size[0])
print(slice_Y_equal_size[1])
slice_X_different_sizes = numpy.split(A, [2, 3], axis = 1)
print(slice_X_different_sizes[0])
print(slice_X_different_sizes[1])
print(slice_X_different_sizes[2])
과제
이번 과제는 위에서 배운 4개의 명령어를 모두 사용해 보겠습니다. 먼저 이전 과제에서 만든 A에서부터 시작합니다. A를 만드는 코드는 이미 준비되어 있습니다.

A = \begin{pmatrix} 1 & 4 & 5 & 8 \\ 2 & 1 & 7 & 3 \\ 5 & 4 & 5 & 9 \end{pmatrix}A=​⎝​⎛​​​1​2​5​​​4​1​4​​​5​7​5​​​8​3​9​​​⎠​⎞​​
A의 shape을 (3, 4)(3,4) 에서 (6, 2)(6,2) 로 변환하여, 이것을 B로 저장합니다.

B의 밑에 \begin{pmatrix} 2 & 2 \\ 5 & 3 \end{pmatrix}(​2​5​​​2​3​​) 을 붙입니다. numpy.concatenate 를 사용하세요.

길이가 늘어난 B를 세로로 두 개로 쪼개고, 이것을 위-아래 순서대로 C, D로 저장합니다.

B = \begin{pmatrix} C \\ D \end{pmatrix}B=(​C​D​​)
C와 D를 가로로 붙여 E를 만듭니다.

E = \begin{pmatrix} C & D \end{pmatrix}E=(​C​​​D​​)
E 를 리턴합니다.
'''

import numpy

def main():
    print(matrix_tutorial())

def matrix_tutorial():
    A = numpy.array([[1,4,5,8], [2,1,7,3], [5,4,5,9]])

    B = A.reshape((6,2))
    B = numpy.concatenate((B, [[2, 2], [5, 3]]), 0)

    [C, D] = numpy.split(B, 2, axis = 0)

    E = numpy.concatenate((C, D), axis = 1)

    return E

if __name__ == "__main__":
    main()
