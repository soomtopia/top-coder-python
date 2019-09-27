## chap04 시뮬레이션

### 시뮬레이션이란

초기상태와 수행해야 할 작업을 제공해주고, 최종 결과를 답하는 문제. 

#### 키위주스

요약

> 키위주스를 담은 병이 N 개가 있음. 해당 N 개의 병에는 bottles[i] 용량 만큼의 키위 주스가 담겨져 있음. 이걸 재분배 하려고함 from_id[i] 의 병에 있는 주스를 to_id[i]에 옮겨야한다. 이때 from_id[i] 병이 비어있거나, to_id[i]의 병이 꽉 차면, 키위주스를 옮기지 않는다. 

##### 클래스와 함수 정의 - python 

```
class_name - KiwiJuiceEasy:
method_name - thePouring
input - (capacities, bottles, from_id, to_id)
```

내가 짠 코드

```python
class KiwiJuiceEasy:
    def thePouring(self, capacities, bottles, from_id, to_id):
        # capa, bottle, from, to 다 같은 N 값을 가진다
        for i in range(len(from_id)):
            
            index_from = from_id[i]
            index_to = to_id[i]
            # 용량 담아놓기 
            full_bottles = capacities[index_to]
            # 비어있을 때 진행하지 않는다. 
            if (bottles[index_from] == 0):
                continue
            elif (bottles[index_to] + bottles[index_from] > full_bottles):
                bottles[index_from] -= full_bottles - bottles[index_to]
                bottles[index_to] = full_bottles        
            else:
                bottles[index_to] += bottles[index_from]
                bottles[index_from] = 0
            print(bottles)

            

```

##### code 4-1 python

```python
# 예시로 나온 코드 ..ㅎ 깔끔하다..내코드 눈감아. 
# 여기서는 빈 공간을 체크하고 그만큼 부어주는 방식으로 했다. 이게 맞는듯 실생활에서도
for i in range(len(from_id)):
    f = from_id[i]
    t = to_id[i]
    space = capacities[t] - bottles[t] # to  병의 빈 공간 
    if (space >= bottles[f]): # 빈공간이 from 용량보다 큰 경우 다 때려붓기 
        vol = bottles[f] # 옮길 용량
        bottles[t] += vol
        bottles[f] = 0    
    else:
        vol = space
        bottles[t] += vol
        bottles[f] -= vol 
print(bottles)

# 파이썬 문법을 사요해 한줄로 만든 코드. 가독성은 떨어지는 것 같다. 
for i in range(len(from_id)):
    f = from_id[i]
    t = to_id[i]
    space = capacities[t] - bottles[t]  
    if (space >= bottles[f]):  
        bottles[t], bottles[f] = bottles[t] + bottles[f], 0
    else:
        bottles[t], bottles[f] = bottles[t] + space, bottles[f] - space        
print(bottles)
```

#### 응용기술 1

조건문을 조금 사용하는 방법

> 조건문이 많아지면 코드 양이 많아지고, 입력에 따라 처리되지 않는 부분이 발생한다. 최솟값 함수를 통해 줄여보자

##### 최솟값 메서드 사용방법

기존 병에서 옮길 주스의 양을 구해보자.

###### 기존 병이 cap 10 bottle 5, 옮길 병이 cap 10, bottle 8 일경우

옮길 병의 빈 공간은 2, 기존 주스의 양은 5이다. 해당 최솟값을 비교해보면, __2__ 가 나오고, 이게 총 옮길 양이다. 

###### 기존 병이 cap 10 bottle 3, 옮길 병이 cap 10, bottle 5 일경우

옮길 병의 빈 공간은 5, 기존 주스의 양은 3이다. 해당 최솟값을 비교해보면, __3__ 이 나오고 이게 총 옮길 양이 된다.

##### code 4-2 python 

```python
for i in range(len(from_id)):
    f = from_id[i]
    t = to_id[i]

    vol = min(bottles[f], capacities[t] - bottles[t])
    bottles[f] -= vol
    bottles[t] += vol

print(bottles)
```

조건문 없이 코드가 깔끔해졌다! 



#### 응용기술 2

> 필자는 이동량 생각시, 조건 분기에서 실수할 수 있다고 생각했다. 이동량을 무시하고 __옮길 주스, 기존 주스 양의 총합이 일정하다는것__. 옮길 주스는 주스 총량과 기존 주스의 병의 용량 중에 작은 값이 된다는 것을 이용했다
>
> - to bottles : 옮길 주스 + 기본주스 , 옮길 주스 병 용량 중 작은 값
> - from bottles: 옮길 주스와 기존 주스의 총합 중 위의 값을 제외한 값  

sample

```
to bottles: to + from bottle = 13, to_cap 10 
= min > 10
from bottles: 13 - cap 
```

##### code 4-3 python

```python
for i in range(len(from_id)):
    sum = bottles[from_id[i]] + bottles[to_id[i]]
    bottles[to_id[i]] = min(sum, capacities[to_id[i]])
    bottles[from_id[i]] = sum - bottles[to_id[i]]
print(bottles)
```



####  전후 비교

```python
# before
for i in range(len(from_id)):
	index_from = from_id[i]
	index_to = to_id[i]
	full_bottles = capacities[index_to]
	if (bottles[index_from] == 0):
		continue
	elif (bottles[index_to] + bottles[index_from] > full_bottles):
		bottles[index_from] -= full_bottles - bottles[index_to]
		bottles[index_to] = full_bottles        
	else:
		bottles[index_to] += bottles[index_from]
		bottles[index_from] = 0
print(bottles)

# after
for i in range(len(from_id)):
    sum = bottles[from_id[i]] + bottles[to_id[i]]
    bottles[to_id[i]] = min(sum, capacities[to_id[i]])
    bottles[from_id[i]] = sum - bottles[to_id[i]]
print(bottles)
```

----



궁금한 것

- 저번에 찾아본건, range(len(arr)) 방식보다 enumerate(len)방식이 좋다고하는데, 그럴경우에 index, value 값을 다 뽑아준다. 하지만 여기서는 굳이 필요없어보이는데 어떤 방식이 좋은지 모르겠음. 시간테스트 해봤으나 테스트 값이 간단하여 비슷비슷하게 나온당