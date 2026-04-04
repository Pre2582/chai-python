# Problem: Calculate the sum of even numbers up to a given number n.

n =10
total_sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        total_sum_even +=1
print("sum off even number is: ", total_sum_even)        

