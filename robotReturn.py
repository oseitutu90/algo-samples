"""Robot Return to origin"""

def judgeCircle(moves):
    """Return True if robot returns to origin"""
    y = 0
    x = 0
    for i in moves:
        if i == 'U':
            y += 1
        elif i == 'D':
            y -= 1
        elif i == 'L':
            x -= 1
        elif i == 'R':
            x += 1
    if x == 0 and y == 0:
        return True
    return False
    
    
print(judgeCircle("UDLURL"))