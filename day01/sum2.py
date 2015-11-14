#!/usr/bin/python
sum = 0
sum2 = 0
data = range(0,101)
for i in data:
	if i%2==0:
		sum = sum +i
	else:
		sum2 = sum2 + i
print sum-sum2
print sum , sum2
