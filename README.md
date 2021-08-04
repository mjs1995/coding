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


# 1) Python
- 코딩 기초 상식을 위한 개인 연습지입니다.

## 그리디(greedy)
 당장 좋은 것만 선택하는 그리디   
 
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
아이디어를 코드로 바꾸는 구현
  
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
    * 12605_단어순서 뒤집기.py
    * 20001_고무오리 디버깅.py

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

# 2) SQL
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
   
