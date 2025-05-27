import random

arr = [0, 0, 0]

def place_ball():
    ball_position = random.randint(0, 2)

    arr[ball_position] = 1

    print(f"the ball is inside cup {ball_position + 1}.")

def switch_two_cups():
    a = random.randint(0, 2)
    b = a
    while b == a:
        b = random.randint(0, 2)
    
    c = arr[a]
    arr[a] = arr[b]
    arr[b] = c

    print(f"switched cup {a + 1} and cup {b + 1}")

def main():
    place_ball()

    for i in range(5):
        switch_two_cups()

    a = int(input("which cup has the ball?\nenter the answer here: "))

    if arr[a - 1]:
        print("correct!")
    else:
        print("wrong!")
    
main()

# 동전, 버튼, 배경 디자인
