import matplotlib.pyplot as plt
import numpy as np
import math
import random
from operator import add


w_desired_list = [0.2, 0.3, 0.4, 0.5, 0.6]
#u_list = []
u_list = [0, 0, 0 , 0, 0]
w_actual_list = [0, 0, 0 , 0, 0]

char_function_a = []
char_function_b = []
char_function_c = []
char_function_d = []
char_function_e = []

for i in range(101):
	for j in range (5):
		xsi = ((random.uniform(0,1)) - 0.5) * 2
		u_list[j] = xsi
	
	
	char_function_a.append(w_actual_list[0])
	char_function_b.append(w_actual_list[1])
	char_function_c.append(w_actual_list[2])
	char_function_d.append(w_actual_list[3])
	char_function_e.append(w_actual_list[4])
	
	y_star_temp = np.multiply(w_desired_list, u_list)
	y_star_n = sum(y_star_temp)
	
	temp_a = sum(np.multiply(w_actual_list, u_list))
	temp_b = sum(np.multiply(u_list, u_list))
	temp_c = (y_star_n - temp_a) / temp_b
	gamma = [k * (temp_c) for k in u_list]
	
	w_actual_list = list(map(add, w_actual_list, gamma))

# print (temp_a)
# print (temp_b)
# print (temp_c)
# print (y_star_n)
# print (w_actual_list)

big_grid = np.arange(0,101)
plt.plot(big_grid,char_function_a, label='w1*, w1(n) = 0.2')
plt.plot(big_grid,char_function_b, label='w2*, w2(n) = 0.3')
plt.plot(big_grid,char_function_c, label='w3*, w3(n) = 0.4')
plt.plot(big_grid,char_function_d, label='w4*, w4(n) = 0.5')
plt.plot(big_grid,char_function_e, label='w5*, w5(n) = 0.6')
plt.legend(loc='lower right'), plt.suptitle('Simulation Results of Kaczmarz Algorithm')
# Customize the major grid
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.minorticks_on()
plt.show()