import drawSvg as draw
import math
import statistics

print ("Enter input") # eg:1 2 3
Numbers = [float(i) for i in input().split()]

x,y,z = Numbers

area_x = math.pi * (x**2)
area_y = math.pi * (y**2)
area_z = math.pi * (z**2)

area_list = [area_x, area_y, area_z]

c1_area = min(area_list)
c2_area = c1_area + statistics.median(area_list)
c3_area = c2_area + max(area_list)

c1_radius = math.sqrt(c1_area / math.pi)
c2_radius = math.sqrt(c2_area / math.pi)
c3_radius = math.sqrt(c3_area / math.pi)

d = draw.Drawing(50, 50, origin='center', displayInline=False)
d.append(draw.Circle(0,0, c3_radius, fill='blue', stroke_width=0.25, stroke='black'))
d.append(draw.Circle(0,0, c2_radius, fill='green', stroke_width=0.25, stroke='black'))
d.append(draw.Circle(0,0, c1_radius, fill='red', stroke_width=0.25, stroke='black'))

d.saveSvg('concentric.svg')	


