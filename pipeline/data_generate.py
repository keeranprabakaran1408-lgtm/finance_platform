import numpy as np
rng = np.random.default_rng(12345)
rints = rng.integers(low=0, high=10, size=3)
print(rints)
print(type(rints[0]))