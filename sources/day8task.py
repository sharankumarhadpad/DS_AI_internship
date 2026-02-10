import numpy as np
std_score=([[89,87,95],[88,82,92],[78,71,58],[83,93,91],[96,85,79]])
mean_avg=np.mean(std_score,axis=0)
print(mean_avg)
result = mean_avg-std_score
print(result)

# the reshaper
sensor_R=np.arange(24)
print(sensor_R)
print(sensor_R.reshape(4,3,2))
print(sensor_R.reshape(4,2,3))
        