import numpy as np
from time import perf_counter as now

amount = 1000000
lastTime = now()

normalArray = [1*2 for i in range(amount)]
print(f"Time taken for normalArray : {now() - lastTime:.6f}")

lastTime = now()
nArray = np.full(amount, 1*2, dtype=int)
print(f"Time taken for nArray : {now() - lastTime:.6f}")
