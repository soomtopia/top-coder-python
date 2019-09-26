## chap03 기본 프로그래밍 지식

모든 지식을 세세하게 알지 않아도, 아래만 알면 짤 수 있다.

### 반드시 필요한 프로그래밍 지식

```
1. if / else
2. for
3. array
```

#### if / else

조건에 따라 분기가 달라짐

```python
def is_even(a):
    if a%2 == 0:
        return 1
    else:
        return 0
```

#### for

같은 처리를 몇번 반복. 다양한 for 문을 지원하는 다른 프로그래밍과는 달리, python 은 `for in` 하나의 문법만 지원한다.

```python
for i in iterable:
    print(i)
```

`iterable` 안에는 __iterable(반복 가능한객체)__가 들어와야한다. iterable 객체는 collections.Iterable에 속한다. 대표적으로 아래와 같은 type 이 있다. 

- _range_
- _list_
- _dictionary_ - 이 경우 key 값만 출력된다. 
- _tuple_
- _set_
- _string_
- _bytes_

##### dictionary & for

dictionary 의 경우, 반복문을 돌리면 key 값이 반환된다. 아래 참고

###### example

```python
# default - key
for val in dict:
    print(val) # key
# value 뽑고 싶은 경우. 
for val in dict.values():
    print(val) # value
# 둘다 뽑고 싶은 경우
for val in dict.items():
     print("{key}, {value}".format(key=key,value=val))
```

##### for 사용시 주의할 점 

 ```python
arr = [1, 2, 3, 4, 5]
# bad
for i in range(len(arr)):
	print(a[i])
    
# good
for i in arr:
	print(i)
 ```

이러면 index 를 알 수 없잖아요!  -> enumerate 를 사용합니다. tuple 로 반환해 줍니다.

```python
# good
arr = [1, 2, 3, 4, 5]
for i in enumerate(arr):
    print(i) 

# result 
(0, 1)
(1, 2)
(2, 3)
(3, 4)
(4, 5)

# 변수에 담아 반환 
for i, v in enumerate(arr):
    print(i, v)
```



> 최근 네이버, 라인 온라인 코딩테스트를 파이썬으로 봤다. 배열의 인덱스를 뽑고 싶었으나, 객체로 이터러블이 `for i in range(len(arr))` 이런식으로 구문을 작성했는데 권장하지 않는 패턴이었음. 잘 알고간다..



#### Array

여러개의 데이터를 한번에 관리할 때 사용한다

##### code 3-1 python

```python
# 배열 값 중 가장 큰 숫자 찾기 
def get_max_num(arr):
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num = i  
    return max_num
```



#### 제출 형식 

###### 문제

```
문제 : int 형의 매개변수 a, b가 주어질 때, a+b 를 리턴하세요
class: AplusBProblem
method: public int calc(int a, int b)
```

##### code 3-2 python

```python
class AplusBproblem:
    def calc(a, b):
        return a + b
```



### 추가적인 프로그래밍 지식

알고 있으면 편리한 지식

#### 정렬

##### code 3-3 python

```python
arr = [1, 10, 5, 7, 6]
arr.sort()

>>> arr
# [1, 5, 6, 7, 10]
```



#### 문자열 처리

```python
str = "python"

# 동일 판정
if (str == "python"):
    print("equal")

# 문자 하나 추출
a = str[1]
print(a)

# 문자열 연결

str = "abc" + "def"

# 문자열 잘라내기 [start_index:last_index+1]
str[0:3]
```



#### 연관 배열 

순서대로 데이터를 관리하는게 아닌 경우 연관배열을 사용한다. 숫자가 아닌 문자열로 값을 받을 수 있다. dictionary

##### code 3-5 python

```python
# 문자열을 매개 변수로 받고, 각 문자가 몇번 사용 되었는지 출력 
def count_strings(s):
	dic = dict()
	for i in s:
    	if(i not in dic):
        	dic[i] = 1
    	else:
        	dic[i] += 1
	print(dic)
```



### 정리

꼭 알고 넘어가자