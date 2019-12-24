## chap05 전체탐색

### 전체탐색이란?

모든 패턴을 조사해야 하는 것과 그것을 필요로 하는 문제

##### 대표적인 형태

> 1. 모든 패턴을 찾고 가장 좋은 답을 찾는 것 
>
>    ex)  배열 [3, 5, 8, 7] 중 가장 큰 숫자를 답하세요
>
> 2. 모든 패턴을 찾고 조건을 충족하는 패턴이 몇 개인지 찾는 것
>
>    ex) 배열 [3,5,8,7] 중 짝수가 몇 개 있는지 답하세요. 



#### 1. 즐거운 파티 

화이트의 파티 초대. 다들 즐거울 수 있는 파티를 열고싶음. 각자 흥미 있는 주제를 가진 사람이 많은 사람들을 초대하고싶음. 초대할 수 있는 친구가 최대 몇명인지 구해야한다

##### 클래스와 함수 정의 - python

```
InterestingParty
bestInvitation(self, first, second)
```

내가 짠 코드

```python
class InterestingParty:
    def bestInvitation(self, first, second):
        topic_count = dict()
        for i,v in enumerate(first):
            if (v not in topic_count):
                topic_count[v] = 1
            else:
                topic_count[v] += 1
            
            if (second[i] not in topic_count):
                topic_count[second[i]] = 1
            else:
                topic_count[second[i]] += 1
                
	print(max(topic_count.values()))
```

##### 문제 해설 

- 화제를 순서대로 선택한다
- 해당 화제에 몇명이 흥미가 있는지 조사한다

##### code 5-1 python

```python
# 전체를 다 비교해서 값을 더하는듯? 
for i in range(len(first)):
    f = 0
    s = 0
    for j in range(len(first)):
        if (first[i] == first[j]):
            f+=1
        if (first[i] == second[j]):
            f+=1
        if (second[i] == first[j]):
            s+=1
        if(second[i] == second[j]):
            s+=1
        ans = max(f, ans)
        ans = max(s, ans)
    return ans 
```

#### 응용 기술

연관 배열을 사용해서 불필요한 반복문을 삭제 

##### code 5-2 python

```python
# key 값 지정. 중복된 값은 알아서 스루함
for i in range(len(first)):
    topic_count[first[i]] = 0
    topic_count[second[i]] = 0
# value +1 
for i in range(len(first)):
    topic_count[first[i]] += 1
    topic_count[second[i]] += 1
print(max(topic_count.values()))
```

> 나는 조건문을 사용해서 for문 하나를 썼는데, 여기에서는 for 두번 써서 사용했다. 훨씬 코드가 깔끔해 보이는듯. 이전 chap03 에서 조건문을 덜 사용하게 써보라고했는데, 그 부분을 고려해야할 것 같다. 





#### 2. 암호

- 입력된 배열의 값 중, 한 값만 더해서 바꾼다. 
- 그 중 모든 값을 곱한 값이 가장 최댓값이 되게 return 하면된다. 

내가 짠 코드

```python
def solution(nums):
    nums.sort()
    nums[0] += 1
    result = reduce(lambda x, y: x * y, nums)
    return result
```

##### code 5-3 python 

```python 
    ans = 0
    for i in range(len(numbers)):
        temp = 1
        for j in range(len(numbers)):
            if i == j:
                temp *= numbers[j] + 1
            else:
                temp *= numbers[j]
        print(temp)
        ans = max(ans, temp)
    return ans
```

#### 응용기술

제일 작은 값에 +1 하면 곱하면 되는문제. 간단하게 증며하면 +1 하면 곱의 증가율이 (n+1)/n 이기 때문에, n이 작을수록 같이 커진다. 

##### code 5-4 python

```python
def solution(numbers):
    ret = 1
    numbers.sort()
    numbers[0] += 1
    for i in numbers:
        ret *= i
    return ret
```

> 내 코드가 응용 기술의 접근방식이라 기분이 좋았다. lambda를 써서 사용했는데 반복문을 써도 두줄이니, 모듈을 불러와서 reduce 를 쓰는것보다 간결한 것 같다. 



#### 3. 재미있는 수학

각 배수마다 각자리의 수를 합하면 그 배수로 나눠떨어지는 수가 있는데, 3 ~ 30진법 중 그런 배수 찾기

> 와 엄청 오래걸렸는데 못풀었다. 10자리수를 받아 나눠서 값을 체크하고 나머지가 생기면 배열에서 remove 해주는 방식으로 진행했는데, 10진수 이상의 값을 어떻게 처리할지 감도 안왔다.  ㅠㅠ

내가짠 코드

```python
def solution(base):
    arr = []
    for i in range(2, base):
        arr.append(i)
        j = i
        while j < 1000:
            result = change_base_10_to_number(j, base)
            j += i
            if (result % i) != 0:
                arr.remove(i)
                break
    return arr

def change_base_10_to_number(number, base):
    """
    10진법의 숫자를 n 진법으로 바꾼후 각각의 값을 더한다.
    """
    result = 0
    while number > 0:
        result += (number % base)
        number //= base

    return result
```

##### python  5-5

```python 
def solution(base):
    arr = []
    for n in range(2, base):
        ok = True
        for n1 in range(base):
            for n2 in range(base):
                for n3 in range(base):
                    if (n1 + n2 * base + n2 * base * base) % n == 0 and (n1 + n2 + n3) % n != 0:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            arr.append(n)
    return arr
```

#### 응용기술

1과 base 의 차가 n 으로 나누어 떨어지면, 어떤 자릿수라도 base 로 나누어 떨어진다. 

10진수의 경우 10-1 = 9 

1~9까지 9를 나눴을 때 나누어 떨어지는 수는 3,9

> 헐 답이 3과 9이다....엄청어렵게풀었네.. 수학을 잘해야되나보다.

```python 
def solution(base):
    arr = []
    for i in range(2, base):
        if (base - 1) % i == 0:
            arr.append(i)
    return arr
```

