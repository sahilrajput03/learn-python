import re

# ex2. The position of some particles on the horizontal x-axis are
#       -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8
#       in the positive direction. Extract these numbers from this whole
#       text and find the distance between the two furthest particles.

# *EXPECTED RESULTS*
# points = ["-12", "-4", "-3", "-1", "0", "4", "8"]
# sorted_points = [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 - (-12)  # 20

# Solution:
inputText = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."
points = re.findall(r"-?\d+", inputText)
points = [int(p) for p in points]  # converting str to int via list comprehension
print(points)  # [-12, -4, -3, -1, 0, 4, 8]
sorted_points = sorted(points)  # [-12, -4, -3, -1, 0, 4, 8]

# distance b/w most extreme points
distance = sorted_points[-1] - sorted_points[0]
print(f"\nDistance between furthest points: {distance}")
