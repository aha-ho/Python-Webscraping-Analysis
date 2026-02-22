import datetime
import random

now = datetime.datetime.now() 
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

formatted_date = now.strftime("%Y년 %m월 %d일 %A")
print(f"포맷된 날짜: {formatted_date}")

rand_int = random.randint(1, 10)
print(f"임의의 숫자: {rand_int}")

rand_float = round(random.random() * 10, 2)
print(f"임의의 실수: {rand_float}")

fruits = ['사과', '바나나', '딸기', '오렌지', '포도']
picked = random.choice(fruits)
print(f"임의의 리스트 요소: {picked}")

random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")