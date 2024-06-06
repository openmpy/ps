T = int(input())

for _ in range(T):
  N, M = map(int, input().split())

  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  answer = 0

  A.sort(reverse=True)
  B.sort(reverse=True)

  left, right = 0, 0

  while True:
    if A[left] > B[right]:
      answer += len(B) - right
      left += 1
    else:
      right += 1

    if left == N or right == M:
      break

  print(answer)