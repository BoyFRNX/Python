import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from die import Die


# Make two D6 dice.
die_1 = Die()
die_2 = Die()

# Roll die and add results to a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Count the frequency of each number rolled and add it to a list.
max_result = die_1.num_sides + die_2.num_sides
x_values = range(2, max_result+1)
y_values = [results.count(value) for value in x_values]

# Set up plot.
plt.title('Rolling a D6 die 1000 times')
plt.ylabel('Frequency')
plt.xlabel('Number Rolled')
plt.xticks(x_values)

# Plug in numbers to the plot.
plt.bar(x_values, y_values)

plt.show()
