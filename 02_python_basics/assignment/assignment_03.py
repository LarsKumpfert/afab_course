""" 3. write a code that generates a nested list with 
point coordinates to generate a point grid in rhino (of the form:

list_points =

[[x1,y1,z1], [x1,y1,z2],...[x1,y1,zn],
[x1,y2,z1], [x1,y2,z2],...[x1,y2,zn],
...
[x1,yn,z1], [x1,yn,z2],...[x1,yn,zn],
[x2,y1,z1], [x2,y1,z2],...[x2,y1,zn],
[x2,y2,z1], [x2,y2,z2],...[x2,y2,zn],
...
[x2,yn,z1], [x2,yn,z2],...[x2,yn,zn],
...
[xn,y1,z1], [xn,y1,z2],...[xn,y1,zn],
[xn,y2,z1], [xn,y2,z2],...[xn,y2,zn],
...
[xn,yn,z1], [xn,yn,z2],...[xn,yn,zn]]
"""

points = []



x_size = 4
y_size = 4
z_size = 4

list_x = list(range(x_size))
list_y = list(range(y_size))
list_z = list(range(z_size))

point_list = []

for i in list_x:
    for j in list_y:
        for k in list_z:
            if i == 0:
                pass
            elif j == 5:
                pass
            else:
                point_list.append(i)
                point_list.append(j)
                point_list.append(k)

formatted_list=[]

i=0
while i<len(point_list):
  formatted_list.append(point_list[i:i+3])
  i+=3

print(formatted_list)
