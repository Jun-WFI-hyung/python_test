from math import atan2, sin, radians, cos, tan
from geopy.distance import geodesic

# 북쪽이 0, 남쪽이 180

# 첫번째 좌표
coord1 = (37.393015, 126.959387)  # 예시 좌표 (샌프란시스코)

# 두번째 좌표
coord2 = (37.393084, 126.959353)  # 예시 좌표 (로스앤젤레스)

# 좌표 간 거리 및 방향 계산
distance = geodesic(coord1, coord2).miles  # 거리를 마일로 얻음

# 두 지점 간의 방향 계산
delta_lon = coord2[1] - coord1[1]
bearing = ((180 / 3.14159) * atan2(sin(radians(delta_lon)), cos(radians(coord1[0])) * tan(radians(coord2[0])) - sin(radians(coord1[0])) * cos(radians(delta_lon))) + 360) % 360

print(f"거리: {distance} 마일")
print(f"방향: {bearing}도")
