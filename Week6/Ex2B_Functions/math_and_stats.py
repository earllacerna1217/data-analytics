import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

sample_sum = sum(vals_sample)
print("Experimenting with a subsetset of integers 1-100:")
print('\n')
print (f"Sum of 5 samples values from 1 to 100: {sample_sum}") 

sample_avg = statistics.mean(vals_sample)
print(f"Average of 75 sample values: {sample_avg: .2f}")

sample_median = statistics.median(vals_sample)
print(f"Median of 75 sample values: {sample_median}")


print("Experimenting with 200 values, integers 1-100")
print('\n')

sample2avg = statistics.mean(vals_sample)
print(f"Average of 200 values: {sample2avg}") 

sample2median = statistics.median(vals_choices)
print(f"Median of 200 values: {sample2median}") 

sample2mode = statistics.mode(vals_choices)
print(f"Mode of 200 values: {sample2mode}") 

sample2standev = statistics.stdev(vals_choices)
print(f"Standard deviation of 200 values: {sample2standev: .2f}") 

sample2variance = statistics.variance(vals_choices)
print(f"Variance of 200 values: {sample2variance}") 

area = pi * radius ** 2
print(f"Radius = {radius}, area = {area:.0f}")

area2 = pi * 10 ** 2
print(f"Radius = 10, area = {area2:.2f}")
