import statistics

# finding the mean of a given list
print(statistics.mean([100, 90]))
print(statistics.mean([1, 2, 3]))
print(statistics.mean([1, 2]))

# gives different data types depending on the mean
print(type(statistics.mean([1, 2, 3])))
print(type(statistics.mean([1, 2])))

# statistics.StatisticsError
print(statistics.mean([]))

# finding the mode of a given list
print(statistics.mode([1, 2, 2, 3, 3, 3, 4, 3, 4, 3]))

# if frequencies are same for multiple modes, the first one encountered will be returned
print(statistics.mode([1, 1, 2, 2, 3]))
print(statistics.mode([2, 2, 1, 1, 3]))
