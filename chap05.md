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