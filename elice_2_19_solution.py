'''
Bag-of-Words

기계학습, 정보 검색, 그리고 데이터 마이닝

기계학습 (Machine Learning), 정보 검색 (Information Retrieval), 그리고 데이터 마이닝 (Data Mining) 은 서로 비슷해 보이지만 약간씩 다른 의미를 가집니다. 먼저 기계학습은 데이터에서 의미있는 패턴을 찾아내는 알고리즘 을 의미하며, 이 알고리즘들은 정보 검색이나 데이터 마이닝에서 사용될 수도 있습니다. 정보 검색은 정보의 집합에서 원하는 정보를 뽑아내는 기술을 의미하며, 여러 정의가 있으나 데이터의 일부분 을 빠르게 찾아내는 기술을 의미합니다. 데이터 마이닝은 데이터 내부에 숨겨진 것을 찾아내는 기술을 의미합니다.

자연어 처리

기계학습 알고리즘을 이용한 정보 검색 및 데이터 마이닝 작업에서는 자연어 텍스트의 표현을 위해 여러가지 방식을 사용합니다. 그 모델들 중 하나로 Bag-of-Words모델이 있습니다.

Bag-of-Words 모델은 텍스트를 단어의 집합으로 표현하는 것입니다. 자연어 텍스트는 단어별로 쪼개져 섞인 뒤에 같은 단어끼리 뭉치게 됩니다. 이 과정에서, 단어의 순서나 문장/문법 구조는 사라지며 최종적으로 단어 및 단어의 개수로 표현되게 됩니다. Bag-of-Words는 문서 및 텍스트를 단어로 쪼개 한 가방 (Bag) 에 넣고 흔들어 섞은 뒤에 단어를 재정렬하는것과 비슷한 개념으로 설명할 수 있습니다.

예제

다음 문장을 고려해 봅시다.

John likes to watch movies. Mary likes movies too.
John also likes to watch football games.
두 문장에서 다음과 같은 사전을 만들 수 있습니다. 이것을 단어 사전이라고 부릅니다. 단어 사전은 특정 단어 (word) 를 숫자 (index) 로 바꾸어 주는 역할을 합니다. 밑의 단어 사전에서, John은 0 번째 index에, likes는 1 번째 index에 대응하게 됩니다. John 은 0번째 index에만 대응해야 하며 다른 index로 할당되어서는 안 됩니다. 단어 사전은 Python의 Dictionary를 이용해서 쉽게 만들 수 있습니다.

{
"John": 0,
"likes": 1,
"to": 2,
"watch": 3,
"movies": 4,
"also": 5,
"football": 6,
"games": 7,
"Mary": 8,
"too": 9
}
그리고 두 문장은 다음과 같은 10차원 벡터로 표현됩니다. 이 벡터와 단어 사전을 합하여 bag-of-words 모델이라고 합니다. 각각의 문장 벡터는 Python의 리스트를 이용해서 만들 수 있습니다.

Index: 0  1  2  3  4  5  6  7  8  9
      [1, 2, 1, 1, 2, 0, 0, 0, 1, 1]
      [1, 1, 1, 1, 0, 1, 1, 1, 0, 0]
한 차원은 단어 사전에서의 한 단어를 의미하며 첫 번째 (0 번째) 차원은 "John", 두 번째 (1 번째) 차원은 "likes", ..., 열 번째 (9 번째) 차원은 "too" 를 가리킵니다. 즉, 첫 번째 문장에서는 "John"은 한 번, "likes"는 두 번 나타난다는 것을 표현합니다. 첫 번째 문장의

[1, 2, 1, 1, 2, 0, 0, 0, 1, 1]
은 다음과 같이 해석됩니다.

John likes likes to watch movies movies Mary too
순서와 문장 구조가 bag-of-words 표현에서 유지되지 않음을 확인할 수 있을 것입니다. 이번 프로그래밍 문제에서는 입력받은 문장에 대한 Bag-of-Words를 만드는 알고리즘을 작성해 보겠습니다.

Python Dictionary

Python 에서 dictionary 는 리스트와는 다른 자료구조이며, bag-of-words 단어 사전을 만드는 데에 매우 편리합니다. Dictionary 는 key-value 형식을 가진 자료구조로, list나 tuple처럼 순차적인 구조를 가지는 것이 아니라 key 를 통해 value 를 저장하고 불러올 수 있습니다. 여기서는 bag-of-words 를 사용하는데 필요한 중요한 예제만 간단히 설명하겠습니다.

다음과 같은 명령어로 쉽게 dictionary 를 만들 수 있습니다.

me = {'firstname': 'suin', 'lastname': 'kim'} # initialize
me['email'] = 'suinkim@elice.io' # add a key-value
print(me)
다른 언어와 다른 python 의 장점은 형 (type) 이 굉장히 자유롭다는 것입니다!

test_dict = {}
test_dict['key'] = 'value'
test_dict[1] = 0.5
test_dict['another_key'] = ['a', 'list']
print(test_dict)
for loop 혹은 keys() 를 이용하면 dictionary 안에 있는 key 들을 쉽게 가지고 올 수 있습니다.

for key in test_dict:
    print(test_dict[key])
print(test_dict.keys())
마지막으로 특정 원소가 dictionary에 있는지 없는지 테스트하려면 in 혹은 not in 을 쓰면 됩니다.

print(1 in test_dict)
print('hello' in test_dict)
print('world' not in test_dict)
과제

Bag-of-Words 모델을 Python으로 직접 구현하겠습니다. 주어진 문장에 대해 Bag-of-Words 모델과 단어 사전을 만든 뒤, 단어 사전과 만들어진 bag-of-words를 같이 리턴해야 합니다. 자연어 처리에 있어, 몇 가지 규칙이 필요한데, 다음 규칙을 정확히 따라주시기 바랍니다.

단어는 space로 나뉘어지며 모두 소문자로 치환되어야 합니다. Python의 .lower() 및 split() 함수를 사용할 수 있습니다.
단어는 영어 알파벳 (a-z) 만 허용되며 나머지는 space로 치환되어야 합니다. 이 부분은 일반적으로 regular expression (정규식) 으로 작성됩니다. 작성이 어려울 수 있으므로, 이번에는 준비된 replace_non_alphabetic_chars_to_space 함수를 사용하면 됩니다.
단어는 space 를 기준으로 잘라내어 만듭니다. Python의 split() 함수를 이용할 수 있습니다.
단어는 한 글자 이상 (>=1)이어야 합니다. 단어의 길이를 체크하기 위해 len() 함수를 이용할 수 있습니다.
단어 사전에 등록되는 단어의 순서는 관계 없지만, bag-of-words 내의 인덱스와 일치해야 합니다.
입력

문장 한 줄이 입력됩니다.

출력

단어 사전과 입력받은 문장에 대한 bag-of-words 표현을 순서대로 리턴합니다.

테스트 입력

John likes to watch movies. Mary likes movies too. Let's go!
테스트 출력

{'watch': 3, 'to': 2, 'let': 7, 'go': 9, 'too': 6, 's': 8, 'john': 0, 'movies': 4, 'likes': 1, 'mary': 5}
[1, 2, 1, 1, 2, 1, 1, 1, 1, 1]
설명

이제 create_BOW 함수 내에서 테스트 입력이 테스트 출력으로 바뀌는 과정을 예제와 함께 설명하겠습니다.

입력 문장은 다음과 같습니다.
'John likes to watch movies. Mary likes movies too. Let's go!'
입력 문장은 .tolower() 를 통해 다음과 같이 바뀝니다.
'john likes to watch movies. mary likes movies too. let's go!'
입력 문자는 이제 replace_non_alphabetic_chars_to_space 함수에 의해 변환됩니다.
'john likes to watch movies mary likes movies too let s go '
소문자로 바뀐 입력 문장은 split() 을 써서 space 로 나뉘어집니다.
['john', 'likes', 'to', 'watch', 'movies', 'mary', 'likes', 'movies', 'too', 'let', 's', 'go']
한 글자 미만의 단어 (빈 문자열) 는 없앱니다. 여기서는 한 글자 미만의 단어는 다행히 없습니다.
['john', 'likes', 'to', 'watch', 'movies', 'mary', 'likes', 'movies', 'too', 'let', 's', 'go']
이제 단어 사전을 만듭니다. Python의 dictionary 를 써서 만들면 쉽습니다. 위의 단어 리스트의 앞부터 뒤로 이동하면서, 단어 사전에 없는 (not in) 단어는 새로 추가하고, 이미 있는 (in) 단어는 skip 하면서 진행하면 됩니다.
{
  'john': 0,
  'likes': 1,
  'to': 2,
  'watch': 3,
  'movies': 4,
  'mary': 5,
  'too': 6,
  'let': 7,
  's': 8,
  'go': 9
}
이제 단어들을 단어 사전에 맞추어 대응시킵니다.
['john', 'likes', 'to', 'watch', 'movies', 'mary', 'likes', 'movies', 'too', 'let', 's', 'go']
가 다음과 같이 바뀝니다.

[0, 1, 2, 3, 4, 5, 1, 4, 6, 7, 8, 9]
마지막으로 단어의 개수들을 셉니다. 단어 0은 1번, 단어 1은 2번, ... 이므로
인덱스   0  1  2  3  4  5  6  7  8  9
      [1, 2, 1, 1, 2, 1, 1, 1, 1, 1]
가 됩니다.

'''
import re

def main():
    # example : John likes to watch movies. Mary likes movies too. John also likes to watch football games.
    sentence = input()
    BOW_dict, BOW = create_BOW(sentence)

    print(BOW_dict)
    print(BOW)

def create_BOW(sentence):
    # Exercise
    word_list = replace_non_alphabetic_chars_to_space(sentence.lower()).split()
    word_list = [ word for word in word_list if len(word) > 0]
    bow_dict = {}
    bow = [0]
    index = 0
    for word in word_list:
        if word in bow_dict:
            continue
        else :
            bow_dict[word] = index
            index += 1
    bow = bow * len(bow_dict)

    for word in word_list:
        bow[bow_dict[word]] += 1

    return bow_dict, bow

def replace_non_alphabetic_chars_to_space(sentence):
    return re.sub(r'[^a-z]+', ' ', sentence)

if __name__ == "__main__":
    main()
