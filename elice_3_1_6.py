'''
에러와 제출
이번 프로그래밍 과제에서는 에러에 어떻게 대처하고 과제를 완료하는 방법에 대해 알아보겠습니다.

먼저 준비된 소스 코드를 보고 어떤 오류가 발생할지 생각해 보고, 준비가 되면 제출을 클릭합니다.

소스를 제출하고 나면 다음과 같은 결과를 받게 될 것입니다:

Traceback (most recent call last):
File "animals.py", line 10, in
print(capitalize_animals(['cheetah', 'hare', 'reindeer', 'calf']))
File "animals.py", line 4, in capitalize_animals
for animal in Animals:
NameError: name 'Animals' is not defined
이 메시지는 Python 인터프리터에서 제공하는 메시지와 같습니다. 
두 번째 줄을 보면, line 2에서 문제가 발생했고, 
세 번째와 네 번째 줄을 보면 for animal in Animals: 라는 줄에서 Animals라는 이름이 정의되어 있지 않다는 오류가 발생했다는 결과를 보여줍니다.

문제
에러에 표시된 대로 소스코드의 두 번째 줄을 고쳐서, animals에 있는 동물 이름들이 첫 번째 글자만 대문자로 치환되어 출력되도록 바꿔서 제출하기 바랍니다.
'''

def capitalize_animals(animals):
    new_animals = []

    for animal in Animals:
        new_animals.append(animal[0].upper() + animal[1:])

    return new_animals

if __name__ == "__main__":
    print(capitalize_animals(['cheetah', 'hare', 'reindeer', 'calf']))