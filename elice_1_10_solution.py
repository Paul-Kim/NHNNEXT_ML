'''
Introduction to Numpy
조금 지루했나요? 마지막으로 가장 중요한 부분인 Numpy를 이용한 기초 통계처리에 대해 배우겠습니다.

numpy.sum
배열에 있는 모든 원소의 합을 계산해서 리턴합니다.

A = numpy.array([1, 2, 3, 4])
print(numpy.sum(A))
사칙연산
재미있게도 Numpy의 배열에 사칙연산을 그대로 적용할 수 있습니다. 수학에서는 행렬에 숫자를 더하고, 빼고, 곱하고, 나누는 것을 허용하지 않지만 편의를 위해 만들어진 기능입니다. 실제로 큰 데이터를 다루는 통계분석 시에 굉장히 유용한 기능입니다. 배열 A와 스칼라 (scalar) 숫자 n 에 대해 다음과 같은 룰이 적용됩니다:

A + n: 배열의 모든 원소에 n만큼을 더합니다.
A - n: 배열의 모든 원소에 n만큼을 뺍니다.
A * n: 배열의 모든 원소에 n만큼을 곱합니다.
A / n: 배열의 모든 원소에 n만큼을 나눕니다.
다음 예제를 통해 실제로 실습해 보겠습니다.

A = numpy.array([[1, 2], [3, 4]])
print(A + 2)
print(A - 3)
print(A * 2)
print(A / 5)
numpy.mean, median, std, var
통계 처리시 가장 많이 쓰이는 세 가지 기능들입니다. 만약 데이터가 numpy.array로 주어졌다면 코드 한 줄로 데이터의 평균값, 중간값, 표준 편차, 분산을 구할 수 있습니다. 이 외에도, numpy는 통계를 위한 다양한 함수를 제공하고 있으므로 전체 리스트가 궁금하신 분은 Numpy - Statistics를 참조하시기 바랍니다.

A = numpy.array([1, 2, 4, 5, 5, 7, 10, 13, 18, 21])
print(numpy.mean(A))
print(numpy.median(A))
print(numpy.std(A))
print(numpy.var(A))
쉽지요? :)

과제
이제 위에서 배운 함수 중의 일부를 사용하는 연습을 진행해볼까요? 마찬가지로 이전 과제의 마지막 부분부터 시작하겠습니다.

E를 normalize (표준화) 하여 E 안의 모든 원소의 합이 1이 되도록 합니다.

통계처리시에 표준화작업은 매우 중요합니다. 어떤 사건에 대한 관찰 횟수를 가지고 있을때 이것을 확률 분포로 변환하는 것이 필요할 때 표준화를 사용합니다. 예를 들어, 동전이 어떻게 생겼는지에 대한 지식이 없지만 동전을 100번 던졌을 때 앞/뒷면이 나온 횟수를 알고 있다면, 이것을 통해 이 동전에서 앞면 혹은 뒷면이 나올 확률을 유추해 볼 수 있습니다. 확률을 구하는 가장 쉬운 방법은 횟수를 표준화하는 것입니다. 이를테면, 앞/뒷면에 대한 개수 [42, 58][42,58] 를 표준화하면 [0.42, 0.58][0.42,0.58] 이 되므로 실험을 통해 앞면이 나올 확률이 0.420.42, 뒷면이 나올 확률이 0.580.58이라고 설명할 수 있습니다.
위에서 설명한 sum과 사칙연산만을 이용해 표준화를 할 수 있습니다.
함수 matrix_tutorial 에서 표준화한 배열 E의 분산 (variance) 를 리턴합니다.
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

    return (A - numpy.mean(A))/numpy.std(A)

if __name__ == "__main__":
    main()