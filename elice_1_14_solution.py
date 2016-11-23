'''
Linear Regression for Class Data
이번 주의 마지막 과제는 실제 대학교 수업 데이터에 선형회귀법을 적용하는 것입니다. 지난 과제에서 연습했던 단순선형회귀법의 확장판인 다중선형회귀법을 사용하겠습니다. 단순선형회귀법과 다중선형회귀법은 약간의 차이가 있습니다. 단순선형회귀법은 독립변수 XX가 스칼라 값인 반면, 다중선형회귀법은 여러 차원을 가진 벡터값, 이를테면 ii번째 데이터 포인트에 대해 (X_{i1}, X_{i2}, ..., X_{ip})(X​i1​​,X​i2​​,...,X​ip​​) 을 가집니다. 이 차이로 인해, 단순선형회귀법과 다중선형회귀법은 데이터 포인트를 모델링하는데에 약간의 차이가 있습니다. p = 1p=1일 경우에 단순선형회귀법과 다중선형회귀법은 완전히 같습니다.

단순선형회귀법: y_i = \beta_1 X_i + \beta_0 + \epsilon_iy​i​​=β​1​​X​i​​+β​0​​+ϵ​i​​
다중선형회귀법: y_i = \beta_1 X_{i1} + \beta_2 X_{i2} + ... + \beta_p X_{ip} + \beta_0 + \epsilon_iy​i​​=β​1​​X​i1​​+β​2​​X​i2​​+...+β​p​​X​ip​​+β​0​​+ϵ​i​​
이제 다중선형회귀법을 대학교 수업 데이터에 적용해 분석하는 연습을 진행하겠습니다. 사용할 데이터는 다트머스 대학교 (Dartmouth) 의 Rui Wang이 학생의 행동 분석을 위해 제작/사용한 StudentLife 데이터의 일부입니다. StudentLife는 48명의 다트머스 학생들의 10주동안의 행동 패턴과 해당 학기에 획득한 성적 정보를 포함합니다. 이 데이터는 학생들이 어떤 생활을 했는지에 대한 정보들을 포함하고 있습니다. 예를 들어,

수면 시간 및 기상 시간
하루 중 나누는 대화의 수와 시간
운동 (걷기, 앉아있기, 달리기, 서있기)
학생의 위치 정보 (기숙사, 수업, 파티, 운동)
학생 주변에 있었던 사람들
스트레스 레벨
식습관
이외 여러가지를 포함하고 있습니다. 이번 과제에서는 StudentLife에서 일차적으로 뽑아낸 데이터를 다중선형회귀법을 이용하여 분석한 뒤에 학생의 어떤 생활 패턴이 GPA에 가장 큰 영향을 끼치는지 알아보겠습니다. 과제를 시작하기 전에, 다중선형회귀법을 사용하는 방법에 대해 살펴보겠습니다. 다중선형회귀분석을 위해 이전 과제와 같이 Python Statsmodels 라이브러리를 사용하겠습니다.

결과 해석하기

회귀분석을 수행하고 나면 각 독립변수에 대한 계수 (coefficient) 및 P-value 값을 확인할 수 있습니다. 이 두 가지의 값을 통해 각 변수들이 종속변수에 어떻게 관계되어있는지를 확인할 수 있습니다.

계수 (coefficient): 만약 계수가 양이라면 해당하는 변수가 종속변수에 양으로 연관되어 있으며 (positively correlated), 음이라면 해당 변수가 종속변수에 음으로 연관되어 있음을 나타냅니다. 예를 들어, 일반적으로 섭취하는 음식의 칼로리 라는 독립변수는 비만율 라는 종속변수에 양으로 연관되어 있다고 예측할 수 있습니다. 반대로, 운동 시간 이라는 독립변수는 비만율 에 음으로 연관되어 있다고 생각할 수 있습니다.

P-value: 각 독립변수가 얼마나 종속변수에 영향을 미치는지를 나타냅니다. 정확히 말하면, 회귀분석에서 수행하는 테스트에서 P값은 독립변수의 계수가 0일 확률을 나타냅니다. 즉, P값이 작을수록 해당 독립변수가 모델에서 의미를 가지며, P값이 높을수록 해당 독립변수는 종속 변수에 영향을 끼치지 못하게 됩니다. 일반적으로, P값이 0.05 미만일 때 통계적으로 유의하다고 합니다.

Statsmodels의 regression 라이브러리에서 제공하는 summary와 함께 같이 살펴보겠습니다.

                 Results: Ordinary least squares
=================================================================
Model:              OLS              Adj. R-squared:     0.990
Dependent Variable: y                AIC:                9.1215  
Date:               2015-07-19 19:19 BIC:                10.0292
No. Observations:   10               Log-Likelihood:     -1.5607
Df Model:           2                F-statistic:        444.9
Df Residuals:       7                Prob (F-statistic): 4.20e-08
R-squared:          0.992            Scale:              0.11429
-------------------------------------------------------------------
            Coef.    Std.Err.      t      P>|t|     [0.025   0.975]
-------------------------------------------------------------------
const      -0.4000     0.2726   -1.4676   0.1857   -1.0445   0.2445
x1          1.1000     0.0378   29.1033   0.0000    1.0106   1.1894
x2         -0.3000     0.2171   -1.3817   0.2096   -0.8134   0.2134
-----------------------------------------------------------------
Omnibus:              1.347        Durbin-Watson:           1.700
Prob(Omnibus):        0.510        Jarque-Bera (JB):        0.704
Skew:                 0.000        Prob(JB):                0.703
Kurtosis:             1.700        Condition No.:           18
=================================================================
위 Summary를 살펴보면 변수 세 개 (const, X_1, X_2)(const,X​1​​,X​2​​) 에 대해 분석이 이루어졌음을 알 수 있습니다. 이제 Coef. 및 P>|t| 이 두 컬럼에 집중해서 결과를 해석하겠습니다.

계수 (Coef.): const, x1, x2의 계수는 각각 -0.4, 1.1, -0.3 입니다. x1을 제외한 나머지 두 독립변수들은 종속변수와 음의 상관관계를 가지고 있다고 해석할 수 있습니다.
P값 (P>|t|): x1 만이 0.05 미만의 값을 가지고 있으므로, x1을 제외한 나머지 두 독립변수들은 종속변수와 유의미한 상관관계를 가지고 있지 않습니다.
과제
데이터는 students.dat 에 준비되어 있으며, 30명의 학생이 한 학기동안 어떤 활동을 했으며 결과적으로 몇 점의 GPA (Grade Point Average) 를 받았는지 나타냅니다. students.dat 의 일부는 페이지의 맨 밑에 예시로 나와 있습니다.

파일의 첫 줄은 각 column 에 대한 설명입니다.
1 - 5번째 column 은 XX, 마지막 column은 yy 를 의미합니다.
5 개의 독립변수들은 다음과 같습니다.
평균 수면시간 (X_1X​1​​)
수업 외 공부하는데 사용한 총 시간 (X_2X​2​​)
학기 중의 평균 스트레스 지수 (1 - 5) (X_3X​3​​)
운동에 사용한 총 시간 (X_4X​4​​)
평균 social 지수 (1 - 5), 지수가 높을수록 사회적 활동을 많이 함 (X_5X​5​​)
숫자들은 space 로 나뉘어져 있습니다.
파일로 데이터를 입력받는데에 어려움이 있다면 print_students_data() 함수를 참조하기 바랍니다.
do_multivariate_regression(): 다중선형회귀법을 적용합니다. 본 과제에서는 다음 모델을 사용하겠습니다. Constant (\beta_0β​0​​) 가 없는 점에 유의하시기 바랍니다.

GPA = \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \beta_4 X_4 + \beta_5 X_5GPA=β​1​​X​1​​+β​2​​X​2​​+β​3​​X​3​​+β​4​​X​4​​+β​5​​X​5​​
get_effective_variables(): 유의미한 독립변수 (p < 0.05p<0.05) 들을 Python list로 리턴합니다. 만약 X_1X​1​​, X_3X​3​​ 두 개의 변수가 유의미하다면 다음 리스트를 리턴하면 됩니다.

['x1', 'x3']
students.dat 의 일부

sleep_time study_time stress_level exercise_activity social_activity GPA
6.09589041096 292 2.41635687732 41 4.24050632911 3.519
5.125 54 1.84 11 2.125 3.719
7.92307692308 78 2.06666666667 24 2.8 3.505
8.3 61 2.49090909091 44 2.48275862069 3.889
7.5 6 3.375 0.0 4.33333333333 3.679
'''
import statsmodels.api
import numpy

def main():
    (N, X, Y) = read_data()

    results = do_multivariate_regression(N, X, Y)

    effective_variables = get_effective_variables(results)
    print(effective_variables)

def read_data():
    # 1

    file = []
    X = []
    Y = []

    with open("students.dat") as f:
        for line in f:
            file.append(line.split())

    [*X_names , Y_names] = file[0]
    for i in range(1, len(file)):
        [*x_ele, y_ele] = file[i]
        X.append([float(x) for x in x_ele])
        Y.append(float(y_ele))

    # X must be numpy.array in (30 * 5) shape.
    # Y must be 1-dimensional numpy.array.
    X = numpy.array(X)
    Y = numpy.array(Y)
    return ([X_names, Y_names], X, Y)

def do_multivariate_regression(N, X, Y):
    # 2

    results = statsmodels.api.OLS(Y, X).fit()

    return results

def get_effective_variables(results):

    # 3
    eff_vars = [ "x%d" % i for i in range(len(results.pvalues)) if results.pvalues[i] < 0.05 ]

    return eff_vars

def print_students_data():
    with open("students.dat") as f:
        for line in f:
            print(line)

if __name__ == "__main__":
    main()
