import math

rgarden= float(input("Enter the radius of the garden: "))
#get the circumference
circumference= 2*math.pi*rgarden

#get the area
area = math.pi*(math.pow(rgarden,2))

#get the square root
sqroot=math.sqrt(area)

#get the area rounded up and down
rounddown=math.floor(area)
roundup=math.ceil(area)

#Ouput the answers
print(f"Area of the garden : {area:.2f}")
print(f"Circumference of the garden: {circumference:.2f}")
print(f"Square root of the garden : {sqroot:.2f}")
print(f"Area rounded down : {rounddown:.2f}")
print(f"Area rounded up : {roundup:.2f}")

