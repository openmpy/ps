n = int(input())

numbers = [(list(map(str, input().split()))) for _ in range(n)]
answer = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            counter = 0

            if a == b or b == c or c == a:
                continue

            for arr in numbers:
                number = list(arr[0])

                strike_count = 0
                ball_count = 0

                if a == int(number[0]):
                    strike_count += 1
                if b == int(number[1]):
                    strike_count += 1
                if c == int(number[2]):
                    strike_count += 1

                if a == int(number[1]) or a == int(number[2]):
                    ball_count += 1
                if b == int(number[0]) or b == int(number[2]):
                    ball_count += 1
                if c == int(number[0]) or c == int(number[1]):
                    ball_count += 1

                if strike_count != int(arr[1]):
                    break
                if ball_count != int(arr[2]):
                    break

                counter += 1

            if counter == n:
                answer += 1

print(answer)