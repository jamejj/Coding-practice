# Write code below 💖
import math

wwa = (52.223933,20.994810)
ktw = (50.264893,19.023781)
gda = (54.516842,18.541941)

print(wwa)
print(ktw)
print(gda)

wwa_ktw = math.sqrt( ((wwa[0]-wwa[1])**2) + ((ktw[0]-ktw[1])**2) )
print(wwa_ktw)

wwa_gda = math.sqrt( ((wwa[0]-wwa[1])**2) + ((gda[0]-gda[1])**2) )
print(wwa_gda)

all_in_one = (wwa + ktw + gda)
print(all_in_one)
