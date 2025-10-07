def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_remain = 0
    pickup_remain = 0
    
    for i in range(n-1, -1, -1):
        deliver_remain += deliveries[i]
        pickup_remain += pickups[i]
        
        while deliver_remain > 0 or pickup_remain > 0:
            deliver_remain -= cap
            pickup_remain -= cap
            answer += (i+1) * 2
            
    return answer