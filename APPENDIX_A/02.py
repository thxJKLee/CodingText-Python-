print()

a = 0.1 + 0.2
print(f"0.1 + 0.2 = {a}")
print("실수 정보 표현에 대한 한계점")
print(f"0.1 + 0.2 == 0.3 [{a==0.3}]")  # 실수 정보 표현에 대한 한계

print()

print("일반적으로 반올림함수를 사용한다.")
a = 6.66666666666
print("소수점 아래가 3자리가 남도록 반올림연산 >> ")
print(f"round({a},3) >> {round(a, 3)}")

print()

print("그러면 어떻게 활용할 수 있을까")
a = 0.1 + 0.2
print("아래처럼 하면 의도한대로, 실수값의 정확한 비교를 할 수 있다.")
print(f"round({a},4) == 0.3 [{round(a,4) == 0.3}]")
