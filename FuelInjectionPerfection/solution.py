def solution(n):
    count = 0
    while n > 1:
        if n&1 ==0:
            n >>= 1
        elif n&7 == 7:
            print(n)
            n += 1
        else:
            n-=1
        count += 1
    return count

print("solution : ",solution(4))
print("solution : ",solution(15))
#print(solution(10**309 - 1))
print("solution : ",solution(3))
print("solution : ",solution(39))