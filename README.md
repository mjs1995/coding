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

## 정렬(Sorting)
기준에 따라서 데이터를 정렬

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
    * 비효율적인 피보나치 수열 구현
    * 피보나치 수열 (Top-bottom)
    * 피보나치 수열 (Bottom-top)
    * 1로 만들기
    * 개미 전사
    * 바닥 공사
    * 효율적인 화폐 구성

## 최단 경로(ShortestPath)
가장 빠른 길 찾기

    * 간단한 다익스트라 알고리즘
    * 개선된 다익스트라 알고리즘 (우선순위 큐)
    * 플로이드 워셜 알고리즘
    * 미래 도시
    * 전보

## 기타 그래프 이론(graph/ETC)
다양한 그래프 알고리즘

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

## 백준
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
    
