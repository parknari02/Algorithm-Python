# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# tmp = [0] * n  # 병합용 임시 배열

# def merge_sort(l, r):
#     if r - l <= 1:
#         return 0
#     m = (l + r) // 2
#     inv = merge_sort(l, m) + merge_sort(m, r)

#     i, j, k = l, m, l
#     while i < m and j < r:
#         if arr[i] <= arr[j]:
#             tmp[k] = arr[i]
#             i += 1
#         else:
#             tmp[k] = arr[j]
#             j += 1
#             inv += (m - i)  # 오른쪽 원소가 앞설 때, 왼쪽에 남은 개수만큼 역순 추가
#         k += 1

#     # 남은 것들 복사
#     while i < m:
#         tmp[k] = arr[i]; i += 1; k += 1
#     while j < r:
#         tmp[k] = arr[j]; j += 1; k += 1

#     # 원본에 반영
#     arr[l:r] = tmp[l:r]
#     return inv

# print(merge_sort(0, n))