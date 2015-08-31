#elice_3_3_25.py
'''
Importing Python Modules

Python에는 모듈을 가져오는 방법에는 여러 가지가 있습니다. 우리가 이전 과제에서 사용했던 import numpy 혹은 import scipy 와 같은 명령어들이 그 중에 하나입니다.

import X: 모듈 X 를 가져와서 현재 namespace (이름 공간) 에 reference를 만듭니다. 이 명령어를 실행하면 X.name 으로 X 에 정의된 것들을 사용할 수 있습니다.
import X as Y: import X 와 같지만 X.name 대신 Y.name 을 사용하여 X 에 정의된 것들을 사용합니다. 예를 들어, import numpy as np 의 명령어를 사용하면 np.array 가 import numpy 를 실행한 후의 numpy.array 와 같은 효과를 냅니다.
from X import *: 모듈 X 를 가져온 뒤에 현재 namespace 에 X 에 있는 모든 public object 들을 가져와 reference를 만듭니다. 이것을 실행하면, X 안에 있는 모든 것들을 X. 없이 사용할 수 있습니다. 예를 들어, from numpy import * 을 실행했다면 array([1, 2, 3, 4]) 와 같은 명령어를 사용할 수 있습니다.
from X import a, b, c: 위의 명령어와 같지만, X의 모든 public object 를 가져오는 것이 아니라 a, b, c 만 가져옵니다.
X = __import__('X'): 이것은 모듈 이름을 string 형식을 써서 부를 수 있고, 이것을 특정한 변수 X 에 할당할 수 있습니다. 모듈을 동적으로 부르고자 할 때 사용합니다.
첫 번째와 두 번째 방법 (혹은 마지막) 이 일반적으로 권장되는 방법입니다. 세 번째나 네 번째 방법을 쓸 경우에는 모듈에 있는 모든 public object 들을 현재 namespace로 가져오면서 원치 않는 결과를 낼 수 있기 때문입니다. 예를 들어,

from numpy import *
를 실행할 경우 다음 모듈들이 현재 namespace에 모두 들어오게 됩니다.

['ALLOW_THREADS', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity', 'MAXDIMS', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'PackageLoader', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO',
...
'triu_indices', 'triu_indices_from', 'true_divide', 'trunc', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode', 'unicode_', 'union1d', 'unique', 'unpackbits', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0', 'vsplit', 'vstack', 'warnings', 'where', 'who', 'zeros', 'zeros_like']
만약 BUFSIZE 라는 변수를 이미 쓰고 있었거나, array 라는 다른 개체가 있었을 경우 이 명령어로 인해 새로운것으로 덮어씌워져 프로그램에서 문제가 발생할 확률이 높아집니다.

과제

지금부터 import numpy 대신 import numpy as np 와 같은 명령어를 사용하겠습니다. 이것을 연습해 보겠습니다.

지금 프로그램에는 에러가 있습니다. 에러가 나지 않게, import 부분만을 수정해서 제출해 보세요.
'''

# import this module as 'np'
import numpy
# import this module as 'pd'
import pandas

def main():
    A = np.array(['a', 'b', 'c', 'd', 'e'])
    idx = np.array([1, 2, 3, 4, 5])
    s = pd.Series(A, index=idx)

    return 0

if __name__ == "__main__":
    main()
