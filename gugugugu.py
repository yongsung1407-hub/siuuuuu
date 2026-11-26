def gugudan(n):
    """숫자 n을 받아 n단을 출력합니다."""
    print(f"===== {n}단 =====")
    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")


num = int(input("구구단을 출력할 숫자를 입력하세요: "))
gugudan(num)