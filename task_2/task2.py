import numpy as np
import time

start_time = time.time()

array = np.random.rand(1000, 1000)

end_time = time.time()


creation_time = end_time - start_time
print("total time taken = ", creation_time, "seconds")

array_bytes = array.tobytes()

new_array = np.frombuffer(array_bytes, dtype=array.dtype).reshape(array.shape)

if np.array_equal(array, new_array):
    print("Arrays are equal")
else:
    print("Arrays are not equal")
