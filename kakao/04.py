#이진트리
def solution(numbers):
    def pad_to_full_tree(bin_str: str) -> str:
        length = 1
        while length < len(bin_str):
            length = length * 2 + 1
        return bin_str.zfill(length)
    
    def valid(sub: str) -> bool:
        if len(sub) == 1:
            return True
        mid = len(sub) // 2
        root = sub[mid]
        left, right = sub[:mid], sub[mid+1:]

        if root == '0' and ('1' in left or '1' in right):
            return False
        return valid(left) and valid(right)
    answer = []
    for x in numbers:
        b = bin(x)[2:]
        b = pad_to_full_tree(b)
        if valid(b):
            answer.append(1)
        else:
            answer.append(0)
    return answer