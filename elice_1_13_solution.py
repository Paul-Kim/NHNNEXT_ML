'''
Simple Linear Regression (continued)
바로 이전 과제에 이어, 이제 직접 선형회귀분석 알고리즘을 실행해보겠습니다. Scipy에는 여러 가지의 기계학습 알고리즘이 있는데, 이번 과제에서는 linear regression 알고리즘을 사용하겠습니다.

statsmodels.api.OLS

statsmodels.api.OLS 는 Python 라이브러리 statsmodels 내에 있는 알고리즘으로, 다른 라이브러리와는 달리 summary를 제공해 훨씬 분석하기 쉽도록 정보를 표시해줍니다. 이 라이브러리는 데이터를 입력받은 뒤 회귀분석을 진행합니다. 이 함수는 두 개의 변수 x 와 y 를 입력받습니다.

이제 예제를 통해 살펴보겠습니다.

import statsmodels.api
import numpy
x = [1, 2, 3, 4, 5]
y = [2, 3.7, 3.9, 5, 7]
X = numpy.array(x).T
X = statsmodels.api.add_constant(X)
results = statsmodels.api.OLS(y, X).fit()
회귀분석 결과를 살펴보려면 .summary() 명령을 입력합니다.

results.summary()
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.940
Model:                            OLS   Adj. R-squared:                  0.920
Method:                 Least Squares   F-statistic:                     46.77
Date:                Sun, 19 Jul 2015   Prob (F-statistic):            0.00640
Time:                        19:24:15   Log-Likelihood:                -2.5719
No. Observations:                   5   AIC:                             9.144
Df Residuals:                       3   BIC:                             8.363
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
const          0.9300      0.548      1.697      0.188        -0.814     2.674
x1             1.1300      0.165      6.839      0.006         0.604     1.656
==============================================================================
Omnibus:                          nan   Durbin-Watson:                   2.378
Prob(Omnibus):                    nan   Jarque-Bera (JB):                0.634
Skew:                           0.125   Prob(JB):                        0.728
Kurtosis:                       1.274   Cond. No.                         8.37
==============================================================================
X 와 Y 를 바꿔서 회귀분석을 계속 진행하면서 어떤 결과가 나오는지 살펴보기 바랍니다. 이번 과제에서는 이제 선형회귀분석을 진행하고 matplotlib을 통해 결과를 그래픽으로 살펴보겠습니다. 자세한 분석 방법은 다음 과제에서 배우겠습니다.

Matplotlib

Matplotlib 은 Python의 라이브러리로 2D 혹은 3D 그래프를 그리는데에 사용되는 라이브러리입니다. Matplotlib를 통해 막대형, 꺾은선형, 원형, 분산형 등의 그래프를 쉽게 그릴 수 있습니다. Matplotlib은 R 혹은 Matlab에서 이용되는 그래픽 라이브러리와 비슷한 용법을 가지고 있기 때문에, R 혹은 Matlab을 통해 그래프를 그리는 것에 익숙하셨던 분들은 쉽게 적응하실 수 있을 것입니다. Matplotlib에서 만들어진 그래프는 논문 및 아티클에 직접 사용되는 경우가 많습니다. 여기에서 Matplotlib을 통해 그려진 그래프들의 예들을 살펴볼 수 있습니다.

본 과제에서는 Matplotlib을 이용해 그래프를 그리겠습니다. Numpy와 같이 Matplotlib 또한 굉장히 큰 라이브러리이기 때문에 앞으로 천천히 배우기로 하고, 이번 과제에서는 그래프를 그리는 코드는 이미 작성된 것을 사용하겠습니다.

과제
Standard Input 으로 주어지는 데이터를 입력받습니다. 입력받는 방법은 이전 과제와 같으며 이미 구현되어 있습니다.

statsmpdels.api.OLS 를 이용해 단순회귀분석을 진행합니다.

주어진 코드를 이용해 데이터 포인트들 및 회귀분석 결과를 그래프로 확인합니다.

입력
첫 줄에는 데이터의 개수가 입력됩니다 (N). 다음 줄부터 N개의 숫자가 XX, yy 로 나뉘어 입력됩니다. XX와 yy는 space로 나뉘어져 입력됩니다.

테스트 입력

5
1 -0.42606129
2 1.66488127
3 3.50637347
4 5.81247981
5 7.10695352
'''
import sys
import statsmodels.api
import numpy
import matplotlib.pyplot as plt
# import elice_utils

def main():
    (N, X, Y) = read_data()
    results = do_simple_regression(N, X, Y)

    plt.scatter(X, Y)
    X = numpy.array(X)
    plt.plot(X, X * results.params[1] + results.params[0], '-')

    plt.show()

    # elice_utils.visualize(X, Y, results)

def read_data():
    # 1
    N = int(input().strip())

    X = []
    Y = []
    for i in range(0, N):
        splitted = input().strip().split()
        x = float(splitted[0])
        y = float(splitted[1])
        X.append(x)
        Y.append(y)

    return (N, X, Y)

def do_simple_regression(N, X, Y):
    # 2
    X = numpy.array(X).T
    X = statsmodels.api.add_constant(X)
    results = statsmodels.api.OLS(Y, X).fit()

    return results

if __name__ == "__main__":
    main()
