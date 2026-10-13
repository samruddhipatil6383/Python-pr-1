import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4]
marks = [80, 75, 90, 85]

# Line plot
plt.plot(x, marks, marker='o')
plt.title("Line Plot")
plt.xlabel("Subjects (1-4)")
plt.ylabel("Marks")
plt.show()

# Bar chart
plt.bar(x, marks)
plt.title("Bar Chart")
plt.xlabel("Subjects (1-4)")
plt.ylabel("Marks")
plt.show()

# Histogram
plt.hist(marks)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
