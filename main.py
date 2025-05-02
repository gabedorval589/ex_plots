import matplotlib.pyplot as plt
from my_funcs import build_dict

test = ('Carissa', '12/10/01', 'mangoes') 
res = build_dict(test)

print(f"The user details is as follows: {res}")

x_values =[0, 1, 2, 3, 4, 5]
y_values1 = [10, 13, 15, 18, 16, 20]
y_values2 = [9, 11, 18, 16, 17, 19]

#fig = plt.figure
ax1 = plt.subplot(2, 2, 1)
ax2 = plt.subplot(2, 2, 2)

ax1.plot(x_values, y_values1)
ax2.plot(x_values, y_values2)
#plt.show()
#plt.show()