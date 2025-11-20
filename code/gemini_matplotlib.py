import matplotlib.pyplot as plt
import numpy as np

# 1. Create your data
x = np.linspace(0, 10, 100)
print(np)
y = np.sin(x)

# 2. Create and plot the figure
plt.figure()
plt.plot(x, y, label='sin(x)')
plt.title('My Simple Matplotlib Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# 3. Save the plot as a PDF file
# The format is determined by the file extension (.pdf)
plt.savefig('my_matplotlib_plot.pdf')

# If running in a script, you would use this to display the plot
# plt.show()