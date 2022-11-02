"""
이진 탐색을 생각해보자.

1. 중간점을 기준으로 작으면 왼쪽에서 찾고, 크면 오른쪽에서 찾는다.
2. 찾을때까지 반복한다.
"""


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))


result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소 x")
else:
    print(result+1)
