'''
Advanced Matrix Processing
이제 본격적으로 행렬 데이터를 입력받고 처리하는 방법에 대해 배우겠습니다. 만약 선형대수학 (linear algebra) 에 익숙하지 않으신 분들이라면 이번 과제를 약간 어렵게 느끼실 수도 있습니다. 텍스트를 통한 행렬의 입력은 이번 여름캠프 중 계속 사용될 것이므로 꼭 숙지하시기 바랍니다.

배열 입력
이번 기계학습 여름캠프에서는 다음과 같은 방법으로 배열을 입력받겠습니다.

먼저 행렬의 크기를 입력받습니다. 두 개의 숫자를 입력받으며, 각각 행의 수와 열의 수를 의미합니다. 두 개의 숫자는 space 로 나뉘어집니다.

[행의 수] [열의 수]

그 다음 한 줄에 [열의 수] 만큼의 숫자가 입력됩니다.

[행의 수] 만큼의 줄이 입력되어, 총 [행의 수] \times× [열의 수] 만큼의 숫자를 입력받게 됩니다.

예제:

3 5
1 2 6 3 8
11 0 -1 3 1
9 0 7 -3 4
numpy.ndarray.transpose
Transpose는 전치행렬을 구하는 메소드입니다. 배열의 (i, j)(i,j) 번째 원소를 (j, i)(j,i)번째 원소로 바꾼 뒤 리턴합니다. 전치행렬에 대한 자세한 설명은 위키피디아 (영문) 혹은 위키피디아 (한국어) 를 참고하세요.

A = numpy.array([[1, 2, 3], [4, 5, 6]])
print(A.transpose())
numpy.linalg.inv
행렬의 역행렬 (inverse) 를 구할 때 쓸 수 있습니다. 이전과는 달리, numpy의 linalg 라는 선형대수학 관련 세부 패키지를 사용하기 때문에, 조금 더 긴 명령어를 사용합니다. 예제와 함께 살펴보겠습니다.

A = numpy.array([[1, 2], [3, 4]])
print(numpy.linalg.inv(A))
numpy.dot
두 행렬의 곱셈, 혹은 두 벡터의 dot product (내적)을 구하는 데에 사용됩니다. 행렬의 곱셈을 수행할 때, 두 행렬의 shape에 주의해야 합니다. 밑의 예제를 수행하다 보면 에러가 발생할 것입니다. 에러가 왜 발생하는지, 그리고 에러를 어떻게 수정해서 두 행렬을 곱할 수 있게 되었는지 생각해 보기 바랍니다.

A = numpy.array([[1, 2, 3], [1, 2, 1]])
B = numpy.array([[2, 1, 3], [-1, 0, 5]])
C = numpy.dot(A, B) # Error!
B = B.transpose()
C = numpy.dot(A, B)
print(C)
과제
이제 지금까지 배운 행렬 사용방법을 모두 이용해서 약간 어려운 문제를 풀어보겠습니다.

텍스트 입력을 통해 행렬을 입력받아 A로 저장합니다. 이번 과제에서는 이미 구현되어 있으나, 앞으로의 과제에서의 사용을 위해 사용법을 숙지하기 바랍니다.

A의 전치행렬 (transpose) B 를 생성합니다.

B의 역행렬을 구하여 C로 저장합니다.

만약 역행렬을 구하는 것이 불가능하다면 not invertible 을 리턴합니다.
C 안에 들어있는 0보다 큰 원소 (positive) 들의 개수를 리턴합니다.

0보다 큰 원소를 셀 수 있는 좋은 방법은, C > 0 과 같은 연산을 취한 뒤에, np.sum을 적용하는 것입니다. 만약 어렵다면, 팀원들 혹은 조교와 상의해보기 바랍니다.
'''
import numpy

def main():
    A = get_matrix()
    print(matrix_tutorial(A))

def get_matrix():
    mat = []
    [n, m] = [int(x) for x in input().strip().split(" ")]
    for i in range(n):
        row = [int(x) for x in input().strip().split(" ")]
        mat.append(row)
    return numpy.array(mat)

def matrix_tutorial(A):
    # 2

    # 3

    # 4
    return ...

if __name__ == "__main__":
    main()
