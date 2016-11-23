'''
Probability
확률이란 무엇일까요?
확률 및 통계학에서 확률이란 어떤 사건 (event) 이 일어날 것인지에 대한 정도 혹은 믿음의 측도 (measure) 입니다. 확률은 숫자 0부터 1의 값으로 표시됩니다. 0은 이 사건이 결코 일어날 수 없음을 (impossibility) 1은 사건이 확실히 일어남을 (certainty) 의미합니다. 
특정 사건에 대한 확률이 높을수록, 이 사건이 일어남을 조금 더 높은 정도로 확신할 수 있습니다.
사건 A에 대한 확률은 P(A)P(A), Pr(A)Pr(A), 또는 p(A)p(A) 로 표시됩니다. 사건 A 가 일어나지 않을 여사건의 확률 (opposite 또는 compliment) 는 1 - P(A)1−P(A) 와 같습니다. 예를 들어, 완벽한 주사위가 있다고 할 때 주사위를 한 번 굴려서 1이 나오는 사건에 대한 확률은 \frac{1}{6}61입니다. 그리고 1이 나오는 사건의 여사건, 즉 1이 나오지 않는 사건에 대한 확률은 1 - \frac{1}{6} = \frac{5}{6}1−61=65 이 됩니다.
사건 A 와 B 가 한 번의 실험에서 동시에 발생할 확률은 P(A \cap B)P(A∩B) 로 표현됩니다. 예를 들어, 주사위를 던져 1-6의 숫자 중 하나를 뽑았을 때
•   A: 뽑은 숫자가 2의 배수일 확률
•   B: 뽑은 숫자가 3의 배수일 확률
일 경우 P(A \cap B) = \frac{1}{6}P(A∩B)=61 입니다. 사건 A 또는 B 가 발생할 확률, 즉 뽑은 숫자가 2의 배수 또는 3의 배수일 확률은 P(A \cup B) = \frac{4}{6}P(A∪B)=64 입니다. 지금부터 확률의 성질을 간단하게 설명하겠습니다.
•   독립 사건 (independent events): 두 사건 A, B가 독립적일 경우 A, B의 결합 확률 (joint probability) 는 P(A \cap B) = P(A)P(B)P(A∩B)=P(A)P(B)이며, 예를 들어 동전 두 개를 던졌을 때 두 개 모두 앞이 나올 확률은 \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}21×21=41 입니다.
•   상호 배타적 사건 (mutually exclusive events): 만약 두 사건 A, B 가 상호 배타적인 경우, 즉 A와 B가 동시에 일어날 수 없는 경우, P(A \cap B) = 0P(A∩B)=0 이며, P(A \cup B) = P(A) + P(B)P(A∪B)=P(A)+P(B) 가 됩니다.
•   상호 배타적이지 않은 사건 (not mutually exclusive events): 만약 두 사건 A, B가 같이 일어날 수 있는 경우 P(A \cup B) = P(A) + P(B) - P(A \cap B)P(A∪B)=P(A)+P(B)−P(A∩B)입니다.
조건부확률 (conditional probability)
조건부확률은 B 사건이 일어나는 경우의 A 사건이 일어날 확률입니다. 조건부확률은 P(A|B)P(A∣B) 로 쓰여지며, "B 가 주어졌을 때 A 의 확률" 의 의미를 가집니다. 이것은 다음과 같이 정의됩니다. 조건부 확률은 이번 주 프로그래밍 문제에 앞으로 모두 사용되므로 확실히 익혀두기 바랍니다.
P(A|B) = \frac{P(A \cap B)}{P(B)}P(A∣B)=P(B)P(A∩B)
P(B)P(B) 가 0일 경우 조건부 확률은 성립하지 않습니다. 예를 들어, 위의 예쩨를 다시 생각해 보면, 주사위를 던져 1-6의 숫자 중 하나를 뽑았을 때
•   A: 뽑은 숫자가 2의 배수일 확률
•   B: 뽑은 숫자가 3의 배수일 확률
P(A | B)P(A∣B) 는 이미 뽑은 숫자가 3의 배수일 경우 그 중에 뽑은 숫자가 2의 배수일 확률입니다. 즉, 뽑은 숫자가 {3, 6} 둘 중의 하나일 때 숫자가 2의 배수일 확률이며, \frac{1}{2}21 가 됩니다. 이것을 조건부 확률 공식에 다시 적용해 보면
P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{\frac{1}{6}}{\frac{2}{6}} = \frac{1}{2}P(A∣B)=P(B)P(A∩B)=6261=21
가 됩니다.
과제
간단한 동전 던지기 시뮬레이터를 만들어 보겠습니다!
동전을 한 번 던지면 {head, tail} 둘 중 하나가 나올 것입니다. 동전의 앞면 head 가 나올 확률을 입력받고, 동전을 수차례 계속 던지면 동전을 던진 결과를 통해 동전의 앞이 나올 확률을 유추할 수 있습니다.
이 방법을 몬테 카를로 방법 (Monte Carlo method) 라고 부릅니다. 몬테 카를로 방법은 임의의 샘플링 (실험을 수행하는 것) 을 계속 반복하여 특정 함수의 값을 알아내는 방법을 의미합니다. 예를 들어, 우리가 동전의 앞면이 나올 정확한 확률은 모르고 있지만 동전을 계속해서 던지게 되면 동전의 앞면이 나올 정확한 확률에 점점 더 가깝게 알 수 있습니다.
나머지 코드는 모두 작성되어 있습니다. 이제 간단하게, 동전을 던지는 실험 코드를 만들어 보겠습니다. 함수 flip_a_coin 에서, 다음 코드를 작성하세요.
임의의 숫자 random_num 에 대해
•   random_num 이 prob_head 보다 작으면"head" 를 리턴,
•   아니라면 "tail" 을 리턴합니다.
입력
두 개의 숫자가 입력됩니다. 첫 줄은 동전을 던지는 실험의 횟수, 두 번째는 동전의 앞면이 나올 확률입니다.
출력
그래프가 나타납니다. 실험을 반복하면서, 실험적으로 알게 된 동전의 확률과 입력된 진짜 확률을 비교해보기 바랍니다. 동전을 던지는 실험의 횟수가 많아질수록 실제 확률과 실험을 통한 확률의 차이가 어떻게 되는지 살펴보세요.
테스트 데이터
테스트 입력 1
300 0.45 
테스트 입력 2
10000 0.28


'''

import numpy
import matplotlib.pyplot as plt

def main():
    num_flips = int(input())
    prob_head = float(input())

    coin_results = flip_multiple_times(num_flips, prob_head)
    print(visualize(coin_results))

def flip_a_coin(prob_head):
    random_num = numpy.random.random()
    if random_num < prob_head:
        return "head"
    else :
        return "tail"

    # exercise

def flip_multiple_times(num_flips, prob_head):
    if num_flips > 100000:
        print("[num_flips] should be less than 100000")
        num_flips = 100000

    coin_results = []
    for i in range(0, num_flips):
        coin_results.append(flip_a_coin(prob_head))

    return coin_results

def visualize(coin_results):
    heads = []
    tails = []
    count_heads = 0
    count_tails = 0
    for coin in coin_results:
        if coin is "head":
            count_heads += 1
        elif coin is "tail" :
            count_tails += 1
        else :
            print("wrong")
        heads.append(count_heads)
        tails.append(count_tails)

    num_heads = coin_results.count("head")
    num_tails = coin_results.count("tail")
    heads_percentage = num_heads / (num_heads + num_tails)
    tails_percentage = num_tails / (num_heads + num_tails)

    heads = numpy.array(heads)
    tails = numpy.array(tails)

    plt.plot(heads, tails, "r-")
    plt.xlabel("heads")
    plt.ylabel("tails")
    plt.title("Coin Flip : %d times" % (num_heads + num_tails))
    return plt.show()
    #
    # return elice_utils.visualize_boxplot("Coin Flip: %d times" % (num_heads + num_tails),
    #     [heads_percentage, tails_percentage],
    #     ["heads (%)", "tails (%)"])

if __name__ == "__main__":
    main()
