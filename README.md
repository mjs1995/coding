# 코딩 
## 알고리즘 이란?
- 좋은 알고리즘 이란?
	* 문제를 해결하는 것.  
	* 문제를 더 잘 해결하는 것. 
- 컴퓨터 알고리즘 이란?
	* 컴퓨터가 어떤 문제를 해결하기 위해서 컴퓨터가 이해할 수 있는 방식으로 정리되어 있는 해결 방법
- 팔린드롬
``` python 
def is_palindrome(word):
    # 코드를 입력하세요.
    for i in range(len(word) // 2):
        right = len(word) - i - 1
        if word[i] != word[right]:
            return False
    return True
```
- 선형 탐색 : 리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘 
```pytohn
def linear_search(element, some_list):
    # 코드를 작성하세요.
    res = ""
    for i in range(len(some_list)):
        if element == some_list[i] :
            return i
    return None
```

- 이진 탐색 
```python
def binary_search(element, some_list):
    # 코드를 작성하세요.
    some_list.sort()
    start = 0
    end = len(some_list) - 1
    
    while start <= end:
        mid = (start+end) // 2
        if some_list[mid] == element:
            return mid
        elif some_list[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    return None
```

- 정렬
	* 선택 정렬 
		* 가장 먼저 생각이 날 수 있는 자연스러운 정렬 알고리즘(각 위치에 어떤 값이 들어갈지 찾는다)
	* 삽입 정렬
		* 각 값이 어떤 위치에 들어갈지 찾는다

- 점근 표기법

![image](https://user-images.githubusercontent.com/47103479/128636010-412aba53-12f8-46eb-90bd-e58a9d39973e.png)
![image](https://user-images.githubusercontent.com/47103479/128636014-0447997d-37fa-44ef-b3cc-154c744c335d.png)
![image](https://user-images.githubusercontent.com/47103479/128636032-6b92431b-de65-4fb9-bc14-9939f14eb65e.png)
![image](https://user-images.githubusercontent.com/47103479/128636053-978868a7-2bc8-40e6-a808-5c9e76701640.png)
 
 - 재귀함수
 ```python
 # 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # base case
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list
 
    # recursive case
    return some_list[-1:] + flip(some_list[:-1])

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
[9, 8, 7, 6, 5, 4, 3, 2, 1]
```

```python
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    
    if start_index > end_index:
        return None
    
    mid = (start_index + end_index) // 2
    if element == some_list[mid]:
        return mid
    elif element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid-1)
    else:
        return binary_search(element, some_list, mid+1, end_index)
```

-  Brute Force : 가능한 모든 조합(비효율적)
	* 장점 :  직관적이고 명확하다, 답을 확실하게 찾을 수 있다
	* 단점 : 비효율적 
``` python
def max_product(left_cards, right_cards): 
    # 코드를 작성하세요.
    res = []
    for i in range(len(left_cards)):
        for j in range(len(right_cards)):
            res.append(left_cards[i]*right_cards[j])
    return max(res)
```

- Divide and Conquer(분할정복)  
```python
def consecutive_sum(start, end):
    mid = (start + end) // 2
    if start == end:
        return start
    else:
        return consecutive_sum(start, mid) +consecutive_sum(mid+1, end)
```
* 합병정렬
```python
def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1
    if i==len(list1):
        merged_list.extend(list2[j:])
    elif j == len(list2):
        merged_list.extend(list1[i:])
    return merged_list
```

- 합병 정렬
```python
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) < 2:
        return my_list
    else:
        left_half = my_list[:len(my_list) // 2]
        right_half = my_list[len(my_list) // 2:]
        return merge(merge_sort(left_half), merge_sort(right_half))	
```

- 퀵정렬  
	* pivot : 기준 
```python
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
    i = start
    b = start
    p = end

    # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
    while i < p:
        # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
    swap_elements(my_list, b, p)
    p = b

    # pivot의 최종 인덱스를 리턴해 준다
    return p

# 퀵 정렬
def quicksort(my_list, start, end):
    # base case
    if end - start < 1:
        return

    # my_list를 두 부분으로 나누어주고,
    # partition 이후 pivot의 인덱스를 리턴받는다
    pivot = partition(my_list, start, end)

    # pivot의 왼쪽 부분 정렬
    quicksort(my_list, start, pivot - 1)

    # pivot의 오른쪽 부분 정렬
    quicksort(my_list, pivot + 1, end)

def quicksort(my_list, start=0, end=None):
    if end == None:
        end = len(my_list) - 1

    # base case
    if end - start < 1:
        return

    # my_list를 두 부분으로 나누어주고,
    # partition 이후 pivot의 인덱스를 리턴받는다
    pivot = partition(my_list, start, end)

    # pivot의 왼쪽 부분 정렬
    quicksort(my_list, start, pivot - 1)

    # pivot의 오른쪽 부분 정렬
    quicksort(my_list, pivot + 1, end)
```

- Dynamic programming
	*  최적 부분 구조 + 중복되는 부분 문제 해결 -> 한 번 계산한 결과를 재활용하는 방식 
	*  Memoization : 중복되는 계산은 한 번만 계산 후 메모 (cache에 저장후 사용, 하향식 접근 Top-Down) - 재귀
		* 위에서부터 하기때문에 필요없는 계산 안해도되는 장점
	*  Tabulation : Table 방식으로 정리 (상향식 접근, bottom up) - 반복문
```python
def fib_memo(n, cache):
    if n < 3:
        return 1
    if n in cache:
        return cache[n]
        
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    
    return cache[n]

# Memoization
def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)

# Tabulation
def fib_tab(n):
    fib_table = [0,1,1]
    for i in range(3, n+1):
        fib_table.append(fib_table[i-2] + fib_table[i-1])
    return fib_table[n]

def fib_optimized(n):
    if n < 3 :
        return 1
    num1, num2 = 1, 1
    for i in range(3, n+1):
        num2, num1 = num2+num1, num2
    return num2
```

- Greedy Algorithm
	* 장점: 간단하고 빠르다
	* 단점: 최적의 답이 보장되지 않는다 
	* 최적 부분 구조(Optimal Substructure) - 부분 문제들의 최적의 답을 이용해서 기존 문제의 최적의 답을 구할 수 있다는 것
	* 탐욕적 선택 속성(Greedy Choice Property) - 각 단계에서의 탐욕스런 선택이 최종 답을 구하기 위한 최적의 선택 

# 1) Python 코딩 풀이
- 코딩 기초 상식을 위한 개인 연습지입니다.

## 그리디(greedy)
- 당장 좋은 것만 선택하는 그리디   
 
    * 거스름돈 문제
    * 큰 수의 법칙
    * 숫자 카드게임
    * 1이 될 때까지
    * 모험가 길드
    * 곱하기 혹은 더하기
    * 문자열 뒤집기
    * 만들 수 없는 금액
    * 볼링공 고르기 
    * 무지의 
    
## 구현(Implementation)
![image](https://user-images.githubusercontent.com/47103479/146678416-aaf50577-a9b7-4789-9855-4d5add5fa9c1.png)
![image](https://user-images.githubusercontent.com/47103479/146678778-6a9f234d-65e7-4c9d-860a-a55abf57f01a.png)

- 아이디어를 코드로 바꾸는 구현
  
    * 상하좌우
    * 시각
    * 왕실의 나이트
    * 게임 개발
    * 럭키 스트레이트
    * 문자열 재정렬
    * 문자열 압축
	
## DFS/BFS(DFS_BFS)
꼭 필요한 자료구조 기초

    * 탐색 알고리즘 DFS/BFS
    * 스택 구현 
    * 큐 구현 
    * 무한히 반복되는 재귀함수 
    * 재귀함수의 종료 조건 
    * 2가지 방식으로 구현한 팩토리얼 
    * 인접 행렬 
    * 인접 리스트 
    * DFS
    * BFS
    * 음료수 얼려 먹기
    * 미로 탈출
    * 특정 거리의 도시 찾기

## 트리
![image](https://user-images.githubusercontent.com/47103479/147673449-f2725103-2c0a-4798-9339-c2720eafdb37.png)
![image](https://user-images.githubusercontent.com/47103479/147673553-959c6539-2f55-495d-a3db-f4bb3719e49e.png)
![image](https://user-images.githubusercontent.com/47103479/147673839-5f344b5c-4611-43b4-8dec-97dfbb9dbda7.png)
![image](https://user-images.githubusercontent.com/47103479/147673891-2eaba4b8-9e68-4eaa-b821-3bdfbc58f552.png)
![image](https://user-images.githubusercontent.com/47103479/147673956-39d5ca17-47fe-4bcf-91f0-ab0e4d6b4792.png)
![image](https://user-images.githubusercontent.com/47103479/147761780-d060e24f-f690-43a0-a969-9ec34acac37e.png)
![image](https://user-images.githubusercontent.com/47103479/147761957-448d098f-b0fb-40ab-ad04-24b99be0e22e.png)
![image](https://user-images.githubusercontent.com/47103479/147762199-e278372a-3007-4a55-a3d3-bb5f1196c849.png)
![image](https://user-images.githubusercontent.com/47103479/147762309-fff2c145-e826-46bd-b8df-c23392ff5fe3.png)
![image](https://user-images.githubusercontent.com/47103479/147762328-ca464301-c955-427c-ac93-a09a367174ef.png)
![image](https://user-images.githubusercontent.com/47103479/147762518-3b2b3f83-825a-4e6f-8043-aedfac6333cd.png)
    
### DFS
![image](https://user-images.githubusercontent.com/47103479/146774983-92ffc2de-7861-48aa-9344-780cfaf8e39c.png)
![image](https://user-images.githubusercontent.com/47103479/146775096-0b21c759-a458-4d14-8f9c-bbd71d179e72.png)

### BFS
- 거리가 가까운 기준 / 최단거리 목적
![image](https://user-images.githubusercontent.com/47103479/146775281-e79cb061-9524-4a7b-bee4-63be282c1bb3.png)
![image](https://user-images.githubusercontent.com/47103479/146775545-f7b9e0c1-250e-4eca-ac8d-a7696bdab324.png)

## 정렬(Sorting)
기준에 따라서 데이터를 정렬
![image](https://user-images.githubusercontent.com/47103479/146783663-dc35a772-8ac3-40fa-8b12-32293a72d579.png)
![image](https://user-images.githubusercontent.com/47103479/146783975-c4073c17-3e7d-4411-90cd-e17110433b92.png)
![image](https://user-images.githubusercontent.com/47103479/146784799-7033e3a6-79a1-4f53-8910-83e1a317e250.png)
![image](https://user-images.githubusercontent.com/47103479/146785005-24fc4200-7538-47c7-957f-28c34a01fc60.png)
![image](https://user-images.githubusercontent.com/47103479/146785485-08fb44d3-1b6d-4461-8f2a-7cc3f4314f45.png)
![image](https://user-images.githubusercontent.com/47103479/146786142-cdcae3fa-eee9-41a9-ac4c-dbf1de186fde.png)
![image](https://user-images.githubusercontent.com/47103479/147762279-07137e08-1061-472f-b3e5-a4b5bbfe61fc.png)

    * 선택 정렬
    * 스와프(Swap)
    * 삽입 정렬
    * 퀵 정렬
    * 파이썬의 장점을 살린 퀵 정렬
    * 계수 정렬
    * 정렬 라이브러리 기본 예제
    * 정렬 라이브러리 키(Key) 기준 정렬 예제
    * 위에서 아래로
    * 성적이 낮은 순서대로 학생 출력하기
    * 두 배열의 원소 교체
    * 국영수
    * 안테나
    * 실패율
    * 카드 정렬하기

## 이진 탐색(Sequential Search)
범위를 반씩 좁혀가는 탐색
![image](https://user-images.githubusercontent.com/47103479/146942539-ff4dbca2-d413-4b7d-93b4-fb336f1d094c.png)
![image](https://user-images.githubusercontent.com/47103479/146942627-26a255e2-37f0-404e-96e6-9b067dc8fe28.png)
![image](https://user-images.githubusercontent.com/47103479/146942707-022e1ce5-f858-4f45-a020-d77614f77161.png)
![image](https://user-images.githubusercontent.com/47103479/146942776-8ccab5a3-128b-4242-9c47-91c3e4a5e23e.png)
![image](https://user-images.githubusercontent.com/47103479/146942866-c75b18cb-e068-4d32-8874-2f224ad986a5.png)
 
    * 순차 탐색
    * 재귀 함수를 이용한 이진 탐색
    * 반복문을 이용한 이진 탐색
    * 파이썬에서 빠르게 입력 받기
    * 부품 찾기
        * 이진 탐색으로 해결
        * 계수 정렬로 해결
        * 집합(Set) 자료형으로 해결
    * 떡볶이 떡 만들기
    * 정렬된 배열에서 특정 수의 개수 구하기
    * 고정점 찾기
    * 공유기 설치
    * 가사 검색

## 다이나믹 프로그래밍(Dynamic)
- 최적 부분 구조(Optimal Substructure) : 큰 문제를 작은 무제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있음
- 중복되는 부분 문제(Overlapping Subproblem) :  동일한 작은 문제를 반복적으로 해결 
![image](https://user-images.githubusercontent.com/47103479/147105909-9fbbf369-a2cb-4daf-89b3-049b19b64a60.png)
![image](https://user-images.githubusercontent.com/47103479/147108359-9c72446f-012b-4244-ab5f-c64bf00dfd62.png)
![image](https://user-images.githubusercontent.com/47103479/147109005-975650c9-1710-4121-a8aa-0e14c10ef343.png)
![image](https://user-images.githubusercontent.com/47103479/147108972-50b98dcc-9be4-42a8-8707-2c3b159d8b68.png)
![image](https://user-images.githubusercontent.com/47103479/147111238-c6bc4deb-4d93-43fe-9751-6dbc4533bf6e.png)
![image](https://user-images.githubusercontent.com/47103479/147111299-dfb8350c-d0c1-4d5d-8ab3-85b2cf64ad34.png)
![image](https://user-images.githubusercontent.com/47103479/147111398-95f0c25c-ac2c-4e20-a472-1f7cfaeabdf8.png)
![image](https://user-images.githubusercontent.com/47103479/147111413-05d2c1ad-2423-42d1-9c51-e405526b92af.png)
![image](https://user-images.githubusercontent.com/47103479/147111428-dd82143f-e189-4b3d-a016-c82a17865efc.png)
![image](https://user-images.githubusercontent.com/47103479/147111471-2344a074-25b2-47b9-9d2f-a518af22573e.png)
![image](https://user-images.githubusercontent.com/47103479/147111776-542f12fc-316b-407c-86e6-b97f25ffc469.png)
![image](https://user-images.githubusercontent.com/47103479/147111756-9fabb5bd-2272-4e6d-bcae-258decff4f64.png)
![image](https://user-images.githubusercontent.com/47103479/147111804-44630134-16eb-4c54-ae12-b65b231b268b.png)
![image](https://user-images.githubusercontent.com/47103479/147111842-25e3df92-ebaf-43e5-938f-2b8d630f0955.png)
![image](https://user-images.githubusercontent.com/47103479/147111859-ed571368-2960-48b9-ab1d-214963375d5d.png)

    * 비효율적인 피보나치 수열 구현
    * 피보나치 수열 (Top-bottom)
    * 피보나치 수열 (Bottom-top)
    * 1로 만들기
    * 개미 전사
    * 바닥 공사
    * 효율적인 화폐 구성

## 최단 경로(ShortestPath)
가장 빠른 길 찾기
![image](https://user-images.githubusercontent.com/47103479/147256239-4d478cf0-90a8-441b-b0e3-54eaa8499676.png)
![image](https://user-images.githubusercontent.com/47103479/147256383-58c25c7d-ecea-4885-a22f-caa2f34677ac.png)
![image](https://user-images.githubusercontent.com/47103479/147256649-8e40cfd5-f4da-4b0f-a2bc-4de78cf855cd.png)
![image](https://user-images.githubusercontent.com/47103479/147256671-86cb64ce-a906-4ff9-9e37-6502a0991576.png)
![image](https://user-images.githubusercontent.com/47103479/147256753-6ed9c37a-ddf8-4ea9-880f-e7fae994c457.png)
![image](https://user-images.githubusercontent.com/47103479/147256870-c84378f0-b185-4d7b-9a60-b562b323d09d.png)
![image](https://user-images.githubusercontent.com/47103479/147256967-3116ba3d-5db0-425f-8dfe-60713ebdc0fa.png)
![image](https://user-images.githubusercontent.com/47103479/147257081-d0774321-0dcc-4b96-8ac9-3ced685e0b07.png)
![image](https://user-images.githubusercontent.com/47103479/147257378-e5233d13-bbc6-440b-b511-a0ae4f5dbe22.png)
![image](https://user-images.githubusercontent.com/47103479/147257498-0ffe1ab9-474a-42b0-adda-f45f586b1c39.png)
![image](https://user-images.githubusercontent.com/47103479/147257648-e0e37fb8-1be2-47ef-81c4-a73cca6ba78c.png)
![image](https://user-images.githubusercontent.com/47103479/147257827-a9f3b50d-b8b8-4d95-b75e-9ea1a1a867cb.png)
![image](https://user-images.githubusercontent.com/47103479/147257852-50f25b5c-89bf-48a8-8f25-e5aa7b48d87e.png)
![image](https://user-images.githubusercontent.com/47103479/147258171-663d0f5c-64cb-42f4-96ac-bc6384df0afb.png)
![image](https://user-images.githubusercontent.com/47103479/147258270-11d7ac5c-6dc2-4c92-8711-9821df03d9eb.png)
![image](https://user-images.githubusercontent.com/47103479/147258283-40f3900d-5f17-44b1-84b8-7821d0403e42.png)
![image](https://user-images.githubusercontent.com/47103479/147258375-846f5bba-7e83-48ee-b90d-86360c1a2ae0.png)
![image](https://user-images.githubusercontent.com/47103479/147258418-e765eed5-002a-41a8-ae1d-4ae47e3cd1fe.png)
![image](https://user-images.githubusercontent.com/47103479/147410150-9d1a54a5-662c-4127-b3ee-4ea6d964f514.png)
![image](https://user-images.githubusercontent.com/47103479/147410157-92c11f05-c4be-4d9c-bd85-b26d5069c757.png)
![image](https://user-images.githubusercontent.com/47103479/147410173-c0db7539-9155-48d5-8310-628906f7fcfa.png)
![image](https://user-images.githubusercontent.com/47103479/147410192-7349f799-c1a9-4f76-8b89-a64bdc38ba02.png)
![image](https://user-images.githubusercontent.com/47103479/147410206-56962cd4-43cd-488f-b9f3-b6ffbc2ec3e5.png)
![image](https://user-images.githubusercontent.com/47103479/147410211-26808c69-eab7-40bf-af12-f279dbd0d38c.png)
![image](https://user-images.githubusercontent.com/47103479/147761541-7e7fb5e0-372d-4115-8593-b75e9b180ee0.png)
![image](https://user-images.githubusercontent.com/47103479/147761566-0b305a4d-7f8c-47a7-b18f-08fc5cf6d77d.png)
![image](https://user-images.githubusercontent.com/47103479/147761662-66f9e97c-1760-4d10-aafb-8340cf9bd337.png)

    * 간단한 다익스트라 알고리즘
    * 개선된 다익스트라 알고리즘 (우선순위 큐)
    * 플로이드 워셜 알고리즘
    * 미래 도시
    * 전보

## 기타 그래프 이론(graph/ETC)
- 다양한 그래프 알고리즘
![image](https://user-images.githubusercontent.com/47103479/147410466-8c440f19-52d3-499b-96b5-c5994cd78d8d.png)
![image](https://user-images.githubusercontent.com/47103479/147410486-e3c0db87-c400-437f-a340-068197f91e93.png)
![image](https://user-images.githubusercontent.com/47103479/147410538-a475036b-3908-432a-b31f-b0faa1621baf.png)
![image](https://user-images.githubusercontent.com/47103479/147410556-6e6cc0b8-bfa4-412b-a1fc-3edd85dd6fe2.png)
![image](https://user-images.githubusercontent.com/47103479/147410571-a3d31991-df1e-4452-82a8-2f4febba900d.png)
![image](https://user-images.githubusercontent.com/47103479/147480083-e3b2d9ac-598d-4ad1-ab08-d4bfe7f278cc.png)
![image](https://user-images.githubusercontent.com/47103479/147480143-c42355d3-a3d7-475b-a5f0-58ac4735db15.png)
![image](https://user-images.githubusercontent.com/47103479/147480230-db4867eb-f7e4-4aae-b7aa-b0f72020757a.png)
![image](https://user-images.githubusercontent.com/47103479/147480266-c2d890e9-7b72-49c3-bc82-49cc6eae5c37.png)
![image](https://user-images.githubusercontent.com/47103479/147480322-5ea65fe6-dbec-4394-aa48-d208fedba7c9.png)
![image](https://user-images.githubusercontent.com/47103479/147480373-afac0b92-1755-400b-8f9e-3f3fe6f9fcf9.png)
![image](https://user-images.githubusercontent.com/47103479/147480408-5b0f5278-648d-464a-ad16-5f548795c294.png)
![image](https://user-images.githubusercontent.com/47103479/147480420-b2e5ffdd-3e7a-4cba-82e9-209c784f88f1.png)
![image](https://user-images.githubusercontent.com/47103479/147480438-99e22d99-28b7-421b-917b-bc2742d054cd.png)
![image](https://user-images.githubusercontent.com/47103479/147480446-4e431118-59ef-4159-bb9a-5cca758bdc1c.png)
![image](https://user-images.githubusercontent.com/47103479/147480459-a269e125-7bae-42a6-a92e-6a1e940597c4.png)
![image](https://user-images.githubusercontent.com/47103479/147480470-d6c8668f-a460-439b-83af-86e5511ab90c.png)
![image](https://user-images.githubusercontent.com/47103479/147480490-ada8a5fe-00f6-4848-a29e-d832989daa67.png)
![image](https://user-images.githubusercontent.com/47103479/147480502-79f4470f-a928-4647-bcc3-589e5aaf5385.png)
![image](https://user-images.githubusercontent.com/47103479/147480517-0014f152-cbd1-417f-89c6-0d2dd3daa45f.png)
![image](https://user-images.githubusercontent.com/47103479/147480530-ca5e300d-7610-458b-a519-4d2e736bf046.png)
![image](https://user-images.githubusercontent.com/47103479/147480596-1d860327-2c4a-4909-82d7-4c96bb488955.png)
![image](https://user-images.githubusercontent.com/47103479/147480689-b6050e2e-e3a8-40e6-a2c6-ca5a1ec9f283.png)
![image](https://user-images.githubusercontent.com/47103479/147480727-ca46a2a7-2e4a-42b6-9efb-ba44d740fad3.png)
![image](https://user-images.githubusercontent.com/47103479/147480750-47b5064d-b482-45e2-979b-f6055bdb144a.png)
![image](https://user-images.githubusercontent.com/47103479/147480787-b0207036-6b4d-4928-a9f0-c7a5edd9c5f2.png)
![image](https://user-images.githubusercontent.com/47103479/147480794-13551007-ff13-49c2-98a8-39147920309e.png)
![image](https://user-images.githubusercontent.com/47103479/147480818-a8475b99-68ab-43f2-a684-7ffb0e97ea9c.png)
![image](https://user-images.githubusercontent.com/47103479/147480826-a95ac57e-a047-4955-af62-2c94b8accb44.png)
![image](https://user-images.githubusercontent.com/47103479/147480836-5b486442-8bd9-4192-b90b-9bf4ce0e2a28.png)
![image](https://user-images.githubusercontent.com/47103479/147480841-c854a8be-c07c-4657-9f68-ba15d3f6f97d.png)
![image](https://user-images.githubusercontent.com/47103479/147480853-80df4910-8f0a-4f6b-9a22-2343d4b14ea8.png)
![image](https://user-images.githubusercontent.com/47103479/147480861-e76ca606-512b-42b4-b65b-828dba8c64e3.png)
![image](https://user-images.githubusercontent.com/47103479/147480882-ee8851ab-ebe6-4576-a013-8da5dd2ca1d6.png)
![image](https://user-images.githubusercontent.com/47103479/147480926-b96f54b1-9abb-4476-827d-e60c54993fb1.png)

    * 간단한 서로소 집합 알고리즘
    * 개선된 서로소 집합 알고리즘 (경로 압축)
    * 서로소 집합을 활용한 사이클 판별
    * 크루스칼 알고리즘
    * 위상 정렬
    * 팀 결성
    * 도시 분할 계획
    * 커리큘럼
    * 소수의 판별
    * 투 포인터
    * 암호만들기
    * 소수구하기

## 기타 알고리즘
![image](https://user-images.githubusercontent.com/47103479/147481143-95f9067b-27bd-4a48-b0d0-d7d261ebf8f4.png)
![image](https://user-images.githubusercontent.com/47103479/147481214-064fa9d9-70e5-4c4c-90f9-c418056642f3.png)
![image](https://user-images.githubusercontent.com/47103479/147481260-3c91cbc4-dccd-4ce3-a67f-a092d1d3d9ba.png)
![image](https://user-images.githubusercontent.com/47103479/147481361-8191be0f-4cde-48c0-af93-5661dd2ef826.png)
![image](https://user-images.githubusercontent.com/47103479/147481416-8787cbb4-8a1b-4c11-95b7-a7bed484ffeb.png)
![image](https://user-images.githubusercontent.com/47103479/147481437-b25bb091-144e-4da1-a4b0-0303e82deef6.png)
![image](https://user-images.githubusercontent.com/47103479/147481450-42ac9b75-dd5a-47b2-bc9f-e26817f13593.png)
![image](https://user-images.githubusercontent.com/47103479/147481489-849f373e-3dd6-4a4b-890b-33004590ea52.png)
![image](https://user-images.githubusercontent.com/47103479/147481562-9ecca8b4-4292-4909-b8be-cd803f9e4b8e.png)
![image](https://user-images.githubusercontent.com/47103479/147481607-6571f57d-8754-44cc-abba-5c118df7facb.png)
![image](https://user-images.githubusercontent.com/47103479/147481672-c5f5af00-4838-4d84-adb6-60b9d19aaef4.png)
![image](https://user-images.githubusercontent.com/47103479/147481728-9b27c0d8-1a7b-481b-9b38-208309ed2039.png)
![image](https://user-images.githubusercontent.com/47103479/147481749-a21d25e0-f2a7-4450-b0b7-2156e037bce5.png)
![image](https://user-images.githubusercontent.com/47103479/147481764-cede558c-7ae2-4e5d-9cb9-70bd4eaab087.png)
![image](https://user-images.githubusercontent.com/47103479/147481777-08a250ce-b47d-4254-8a89-4ec82f3ae608.png)
![image](https://user-images.githubusercontent.com/47103479/147481843-cf405d44-c6c2-4550-8346-64a7951ec9ac.png)
![image](https://user-images.githubusercontent.com/47103479/147481913-1a3928a8-ef24-416d-bc27-efd1240578f2.png)
![image](https://user-images.githubusercontent.com/47103479/147481978-4d33583e-81e7-4135-a1d8-9b9a6ac30cb8.png)
![image](https://user-images.githubusercontent.com/47103479/147482094-d9c44b75-0ba6-4adf-90b9-9a0a9ef71941.png)

## 서버
![image](https://user-images.githubusercontent.com/47103479/147578900-291903ac-64fd-4ed0-b254-4566f825a40f.png)
![image](https://user-images.githubusercontent.com/47103479/147578925-d17433f0-ab34-4a83-8d5c-762e21d688bc.png)
![image](https://user-images.githubusercontent.com/47103479/147578941-737224a2-826f-4439-ae12-13c1a7beb823.png)
![image](https://user-images.githubusercontent.com/47103479/147578952-d2884bcd-0d84-4b02-b4ee-9a426bd60c6c.png)
![image](https://user-images.githubusercontent.com/47103479/147578991-eb69f29a-530b-4235-9b35-5bea60482d3f.png)
![image](https://user-images.githubusercontent.com/47103479/147578999-4834390e-5feb-4717-bc3b-eccf62e68e83.png)
![image](https://user-images.githubusercontent.com/47103479/147579013-adfa91ec-6ba1-497b-9fc5-a563c13c7e52.png)
![image](https://user-images.githubusercontent.com/47103479/147579023-8bdb5bec-ec67-4eaf-a7db-c801302906c3.png)
![image](https://user-images.githubusercontent.com/47103479/147579031-081c43f0-ba22-46cc-bee0-3e9c5f9cf421.png)
![image](https://user-images.githubusercontent.com/47103479/147579049-1b9f9c36-bdf2-476b-811a-d2755e53253c.png)
![image](https://user-images.githubusercontent.com/47103479/147579065-9296ad00-0559-450d-ab17-44c0735f65f1.png)
 

# 백준
### 그리디
    * 11034_캥거루 세마리2
    * 1434_책 정리
    * 2810_컵홀더
    * 5585_거스름돈
    * 14659_한조서열정리하고옴ㅋㅋ
    * 2828_사과 담기 게임
    * 2839_설탕배달

### 구현
    * 1008_A/B
    * 1212_8진수 2진수
    * 1330_두 수 비교하기 분류
    * 2420_사파리월드
    * 2753_윤년
    * 5575_타임 카드
    * 5596_시험점수
    * 5893_17배
### 정렬
    * 2752_세수정렬
    * 13771_Presents
    * 5576_콘테스트
    * 2750_수정렬하기
    * 6996_애너그램
    * 15720_카우버거
    * 15819_너의 핸들은
    * 18766_카드 바꿔치기
### 스택
![image](https://user-images.githubusercontent.com/47103479/146679108-c8698204-d3de-4dba-9bbc-3e65a04968f5.png)

    * 12605_단어순서 뒤집기.py
    * 20001_고무오리 디버깅.py

### 큐 
![image](https://user-images.githubusercontent.com/47103479/146679098-d0e042f5-fd3d-41ae-ac47-b3b994b617df.png)
![image](https://user-images.githubusercontent.com/47103479/147672994-811e4ddf-1331-4b51-98b5-c2f6bfd18838.png)
![image](https://user-images.githubusercontent.com/47103479/147673085-e7ad0e12-9804-4890-bcc0-255da9a71b41.png)
![image](https://user-images.githubusercontent.com/47103479/147673348-077bf42d-c966-483a-b778-f0c82df32527.png)


### Bronze V
	* 1000_A+B
	* 1001_A-B
	* 1271_엄청난 부자2 
	* 1550_16진수
	* 2338_긴자리 계산
	* 2475_검증수
	* 2558_A+B - 2
	* 2845_파티가 끝나고 난 뒤 
	* 2914_저작권
	* 3003_킹, 퀸, 룩, 비숍, 나이트, 폰
	* 3046_R2
	* 5337_웰컴 
	* 5338_마이크로소프트 로고
	* 5339_콜센터
	* 5522_카드게임
	* 5554_심부름 가는 길
	* 6749_Next in line
	* 7287_등록
	* 8370_Plane
	* 8437_Julka
	* 9653_스타워즈 로고
	* 9654_나부 함대 데이터
	* 10170_NFC West vs North
	* 10171_고양이
	* 10430_나머지 
	* 10699_오늘 날짜
	* 10757_큰 수 A+B
	* 10926_??!
	* 11283_한글 2
	* 11382_꼬마 정민
	* 11654_아스키 코드
	* 11942_고려대는 사랑입니다
	* 13277_큰 수 곱셈
	* 14645_와이버스 부릉부릉
	* 14652_나는 행복합니다~
	* 14928_큰 수(BIG)
	* 15439_Vera and Outfits
	* 15641_SUPER SUPER BINARY SEARCH DELUXE 2.5: THE LEGEND OF THE GOLDEN MAZASSUMNIDA, EPISODE 2: THE MAZWAETL UNIVERSE, PART 2: THE PARALLEL UNIVERSE AND THE LOST MAZASSUMNIDA: GAME OF THE YEAR EDITION 스페셜 저지출처언어 제한분류번외
	* 15727_조별과제를 하려는데 조장이 사라졌다
	* 15733_나는 누구인가
	* 15740_A+B-9
	* 15802_타노스
	* 15890_전국 대학생 프로그래밍 대회 동아리 연합 여름 대회 2018
	* 15894_수학은 체육과목 입니다	
	* 15962_	새로운 시작
	* 15964_이상한 기호	
	* 16170_오늘의 날짜는?
	* 16394_홍익대학교	
	* 16430_제리와 톰
	* 17256_달달함이 넘쳐흘러
	* 17295_엔드게임 스포일러
	* 17496_스타후르츠	
	* 18096_Арифметическая магия
	* 1998년생인 내가 태국에서는 2541년생?!
	* 18301_Rats	
	* 20254_Site Score
	* 20492_세금

# 2) SQL 코딩풀이
## 1)Leetcode
    * 595. Big Countries.sql
    * 196. Delete Duplicate Emails.sql
    * 620. Not Boring Movies.sql
    * 1179. Reformat Department Table.sql
    * 626. Exchange Seats.sql
    * 1303.Find the Team Size.sql
    * 1069.Product Sales Analysis II .sql
    * 1068.Product Sales Analysis I.sql
    * 511.Game Play Analysis I .sql
    * 1075.Project Employees I.sql
    * 579. Find Cumulative Salary of an Employee.sql
    * 197. Rising Temperature.sql
    * 1164.Product Price at a Given Date.sql
    * 1148.Article Views I.sql
    * 1729.Find Followers Count.sql
    * 1050.Actors and Directors Who Cooperated At Least Three Times.sql
    * 1667.Fix Names in a Table.sql
    * 1322.Ads Performance.sql
    * 1076.Project Employees II .sql
    * 619.Biggest Single Number.sql
    * 1285.Find the Start and End Number of Continuous Ranges.sql
    * 1398.Customers Who Bought Products A and B but Not C.sql
    * 1421.NPV Queries.sql
    * 1077.Project Employees III.sql	
    * 1112.Highest Grade For Each Student.sql
    * 1045.Customers Who Bought All Products.sql
    * 1757.Recyclable And Low Fat Products Problem.sql
    * 570.Managers with at Least 5 Direct Reports.sql
    * 574.Winning Candidate.sql
    * 178.Rank Scores.sql
    * 1149.Article Views II.sql
    * 180. Consecutive Numbers.sql
    * 614.Second Degree Follower.sql 
    * 569.Median Employee Salary.sql
    * 1350.Students With Invalid Departments.sql
    * 1378.Replace Employee ID With The Unique Identifier.sql
    * 1407.Top Travellers.sql
    * 1251.Average Selling Price.sql
    * 1173.Immediate Food Delivery I.sql
    * 613.Shortest Distance in a Line.sql
    * 1327.List the Products Ordered in a Period .sql
    * 586.Customer Placing the Largest Number of Orders.sql
    * 1280.Students and Examinations.sql
    * 1082.Sales Analysis I.sql
    * 1511.Customer Order Frequency.sql
    * 1517. Find Users With Valid E-Mails.sql
    * 603.Consecutive Available Seats.sql
    * 1113.Reported Posts.sql
    * 512.Game Play Analysis II.sql
    * 1141.User Activity for the Past 30 Days I.sql
    * 1495.Friendly Movies Streamed Last Month.sql
    * 1393.Capital Gain_Loss.sql
    * 1445.Apples & Oranges.sql
    * 1270.All People Report to the Given Manager.sql
    * 1308.Running Total for Different Genders.sql
    * 534_Game Play Analysis III.sql
    * 1440.Evaluate Boolean Expression.sql
    * 1532. The Most Recent Three Orders.sql
    * 1204.Last Person to Fit in the Elevator.sql
    * 1321.Restaurant Growth.sql
    * 608.Tree Node.sql
    * 1264.Page Recommendations .sql
    * 1193.Monthly Transactions I.sql
    * 1126.Active Businesses.sql
    * 1501.Countries You Can Safely Invest In.sql
    * 1341.Movie Rating.sql
    * 1212.Team Scores in Football Tournament.sql
    * 580.Count Student Number in Departments.sql
    * 1205.Monthly Transactions II.sql
    
