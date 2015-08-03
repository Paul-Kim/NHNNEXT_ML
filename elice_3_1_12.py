'''
Simple Linear Regression
Linear Regression (선형회귀법) 은 스칼라로 표현되는 종속변수 yy와 벡터 형식으로 표현되는 독립변수 XX 간의 관계를 표현하기 위한 알고리즘을 나타냅니다. 독립변수 XX가 스칼라 값일 경우 (즉 1차원 벡터일 경우) 는 특별히 단순회귀분석 (simple linear regression) 이라고 부릅니다. 단순회귀분석에서 데이터는 XX와 yy의 쌍의 집합으로 표현되며, 독립변수 XX가 스칼라값이기 때문에 데이터는 2차원 평면에 표시할 수 있습니다.

회귀분석은 관찰된 변수들에 대해 독립변수와 종속변수 사이의 관계를 나타내는 선형 관계식을 구하는 알고리즘입니다. 다시 말하면, 회귀분석은 독립변수가 바뀜에 따라 종속변수가 어떻게 변하는지를 분석하는 것입니다. 그러므로 시간과 관계된 데이터, 예측, 그리고 인과관계를 분석하는데에 자주 사용됩니다.

다른 기계학습 알고리즘과 마찬가지로, 회귀분석법으로 데이터를 분석하는 것은 다음과 같은 과정을 따릅니다.

모델링: 분석하고자 하는 데이터가 어떤 모형을 따를지 데이터에 대해 이미 가지고 있는 지식 (prior knowledge) 을 활용하여 모형을 선택하거나 새로이 제작하는 과정입니다. 이 과제에서 우리는 분석할 데이터에 있는 종속변수 및 독립변수가 이미 선형적 관계를 가지고 있다고 가정합니다.
학습: 데이터를 설명하기 위한 모형 (model) 은 여러 데이터를 설명할 수 있도록 일반적이어야 하며, 일반적인 모델을 수학적으로 표현하기 위해 여러 개의 매개변수 (parameter) 를 가지게 됩니다. 학습이란, 학습 데이터를 가장 잘 설명하는 매개변수의 발견을 통해 모델을 구체화시키는 과정을 말합니다. 일반적으로 모델의 성능을 측정하기 위해, 전체 데이터를 학습 데이터/테스트 데이터 두 개로 나누어 학습 데이터로 파라미터 발견을 진행하고, 테스트 데이터로 학습한 모델이 테스트 데이터를 얼마나 잘 설명하는지 테스트하는 것이 일반적입니다. 만약 데이터의 수가 충분히 크지 않은 경우, 그리고 모델이 데이터를 잘 설명하지 못할 경우 모델이 데이터에 대해 과적합 (overfit) 하게 되는 경우가 있습니다.
모델 검증: 학습 과정에서 발견된 모델과 매개변수가 얼마나 데이터를 잘 설명하는지 검증하는 단계입니다. 위에 서술한 대로, 데이터의 과적합 문제를 방지하기 위해 학습 데이터와 테스트 데이터는 분리해서 사용하는 것이 중요하며, 일반적으로 학습 데이터를 9, 테스트 데이터를 1만큼의 크기로 나누어 여러 번 반복합니다 (10-fold cross validation). 하지만 이번 회귀분석법에서 이 방법은 사용하지 않겠습니다.
이번주에는 이미 선형회귀법을 사용하기로 결정하였으므로, 학습 과 모델 검증 단계를 진행해보도록 하겠습니다.

회귀분석은 여러 기계학습 알고리즘 중 이해하기 쉬운 알고리즘입니다. 먼저 회귀분석의 사용을 통해 기계학습이 어떻게 이루어지는지 이해해 보겠습니다. 먼저 이 과제를 통해 회귀분석을 이론적으로 이해한 뒤에 대학교 수업 데이터를 실제로 사용해 회귀분석을 진행햐겠습니다.

과제
선형회귀분석을 사용하기 전에 먼저 데이터를 입력받는 연습을 다시 진행하겠습니다. 데이터는 간단한 포맷으로 표현됩니다. 첫 줄에는 데이터의 개수 N이 입력되며, N줄에 걸쳐 데이터 포인트들이 입력됩니다. 한 데이터 포인트는 XX 와 yy 로 이루어져 있으며 space 로 나뉘어집니다. 데이터 포인트는 실수를 포함합니다. 예를 들어, 3개의 데이터 포인트로 이루어진 예제는 다음과 같습니다.

3
1 5.1
1.7 8
3 10.4
위의 예제는 3개의 데이터 포인트 (1, 5.1)(1,5.1), (1.7, 8)(1.7,8), (3, 10.4)(3,10.4) 로 이루어진 데이터를 표시합니다. 즉, N = 3, X = [1, 1.7, 3], Y = [5.1, 8, 10.4] 가 됩니다.

이제 실제로 데이터를 입력받는 연습을 진행하겠습니다. 데이터를 입력받아, (N, X, Y) 를 리턴하세요. N은 숫자, X 및 Y 는 Python 리스트여야 합니다. 테스트 입력/출력이 완료되면 제출을 클릭하고 다음으로 넘어갑니다.

테스트 입력

3
1 5.1
1.7 8
3 10.4
테스트 출력

3
[1.0, 1.7, 3.0]
[5.1, 8.0, 10.4]
'''
import numpy

def main():
    (N, X, Y) = read_data()
    print(N)
    print(X)
    print(Y)

def read_data():
    # 1


    # 2

    return (N, X, Y)

if __name__ == "__main__":
    main()