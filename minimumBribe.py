

def minimumBribes(queue):
    # Write your code here
    bribe = 0
    for i in range(len(queue)):
        if queue[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, queue[i] - 2), i):
            if queue[j] > queue[i]:
                bribe += 1
    return bribe

print(minimumBribes([1,2,3,4,5,7,6,8]))