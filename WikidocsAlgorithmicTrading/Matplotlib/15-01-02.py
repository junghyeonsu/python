import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

# # 2행 1열의 첫번째
# ax1 = fig.add_subplot(2,1,1)
# # 2행 1열의 두번째
# ax2 = fig.add_subplot(2,1,2)
#
# x = range(1,100)
# y = [z*z for z in x]
# ax1.plot(x,y)
# ax2.bar(x,y)
# plt.show()


# # 1행2열의 첫번째
# ax3 = fig.add_subplot(1,2,1)
# # 1행2열의 두번째
# ax4 = fig.add_subplot(1,2,2)
# plt.show()

x = np.arange(0.0 , 2*np.pi, 0.1)
sin_y = np.sin(x)
cos_y = np.cos(x)

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(x,sin_y,'b--')
ax2.plot(x,cos_y,'r--')

ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')

ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')

plt.show()