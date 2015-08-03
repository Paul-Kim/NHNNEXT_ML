'''
Introduction to Numpy
Numpy와 Scipy는 Python 언어에서 사용되는 라이브러리입니다. Numpy는 Python 언어에서 기본으로 지원하지 않는 array (배열) 혹은 matrix (행렬) 의 계산을 쉽게 할 수 있도록 도와줍니다. Numpy는 이 외에도 많은 수학 함수들을 포함하고 있어 Numpy를 사용하면 기계학습에서 많이 사용되는 해석학 및 선형대수학에 관련된 수식들을 Python 위에서 쉽게 프로그래밍 할 수 있습니다.

Scipy는 Python의 라이브러리임과 동시에 계산과학을 위한 시스템을 총칭합니다. Scipy는 Numpy를 포함하며 앞으로 우리가 사용할 Matplotlib (그래프를 그리는 데에 주로 사용됨) 외에도 IPython (Web에서 작동하는 Python의 인터랙티브 쉘) 및 Pandas (데이터 저장 및 분석을 위한 라이브러리) 와 같은 훌륭한 패키지들로 이루어져 있습니다. 본 여름캠프에서는 Scipy에 포함된 머신 러닝 패키지를 몇 개 사용할 것입니다. Numpy를 포함한 Scipy 전체는 오픈소스 패키지이며 누구든지 소스에 접근하고 기여할 수 있습니다.

Numpy는 대단히 큰 패키지이기 때문에 배우는 데에 시간이 많이 소요될 수도 있습니다. 본 여름캠프에서는 Numpy의 모든 부분을 다루지는 않을 것입니다. 만약 더 깊이 배우시고 싶은 분께서는 Numpy 공식 사이트의 튜토리얼을 참조하시는 것이 도움이 될 수 있습니다. 지금부터 Numpy에 익숙해지기 위한 과정을 한 단계씩 진행하도록 하겠습니다.

numpy.ndarray
Numpy는 기본적으로 n차원 배열을 만들 수 있도록 설계되었습니다. Python에서 주로 사용하는 리스트는 1차원 배열에 해당하며, 우리는 주로 2에서 3차원 배열을 사용하겠지만 복잡한 데이터의 경우 그 이상도 사용할 수 있습니다. Numpy에서 배열을 생성하는 방법은 여러 가지가 있지만 제일 쉬운 방법은 배열에 들어갈 데이터를 직접 넣는 것입니다. 예를 들어,

\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}(​1​3​​​2​4​​)
와 같은 2 \times 22×2 배열 (또는 행렬) 을 만들기 위해서는 다음과 같은 명령어를 사용할 수 있습니다. ndarray를 만들기 위해서 array() 명령어를 사용합니다.

numpy.array([[1, 2],
             [3, 4]])
[ 나 ] 와 같은 괄호의 수, 그리고 , (comma) 의 위치에 주의하기 바랍니다. [1, 2] 와 [3, 4]는 다른 줄에 있을 필요는 없으며 가독성을 위해서 위와 같이 코드를 작성했습니다. 이제 배열을 선언하는 것을 연습하겠습니다.

과제
이제 2차원 numpy.array A를 선언하겠습니다. A는 3 \times 43×4 의 크기를 가진 2차원 배열이어야 합니다.

A = \begin{pmatrix} 1 & 4 & 5 & 8 \\ 2 & 1 & 7 & 3 \\ 5 & 4 & 5 & 9 \end{pmatrix}A=​⎝​⎛​​​1​2​5​​​4​1​4​​​5​7​5​​​8​3​9​​​⎠​⎞​​
A를 준비된 코드 안의 matrix_tutorial() 함수 안에 선언하여, 만들어진 A가 리턴될 수 있도록 합니다.
'''import numpy

def main():
    print(matrix_tutorial())

def matrix_tutorial():
    # Create the matrix A here...

    return A

if __name__ == "__main__":
    main()
