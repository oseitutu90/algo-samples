"""An avid hiker keeps meticulous records of their hikes. 
During the last hike that took exactly  steps,
for every step it was noted if it was an uphill, , or a downhill, 
step. Hikes always start and end at sea level,
and each step up or down represents a  unit change in altitude"""

# print(counting_valleys(8,[U,D,D,D,U,D,U,U])) # 1

def counting_valleys(steps, path):
    """Return the number of valleys traversed."""
    level = 0
    valleys = 0
    for step in path: 
        if step == 'U':
            level += 1
        else:
            level -= 1
        if level == 0 and step == 'U': # if current level 
            valleys += 1
    return valleys
print(counting_valleys(12,["D","D","U","U","D","D","U","D","U","U","U","D"]))
# _                 / \_
#  \    / \        /
#   \ /    \ / \ /
#     
#   