from simple_image_download import simple_image_download as simp 

response = simp.simple_image_download()

keywords = ["football 4k shot"]
limit = 100
for kw in keywords:
    response.download(kw, limit)

# Check point insde polygon
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

point = Point(0.5, 0.5)
polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
print(polygon.contains(point))