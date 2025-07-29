# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
apartamente = [(37, 65_000), (40, 68_000), (55, 85_000), (60, 90_000),  (80, 130_000), (120, 200_000)]
apartamente = np.array(apartamente)
apartamente

# %%
suprafete = apartamente[:, 0]
preturi = apartamente[:, 1]
suprafete, preturi

# %%
from sklearn.linear_model import LinearRegression

# %%
model = LinearRegression()
model

# %%
x = suprafete
y = preturi

# %%
x, x.shape

# %%
reshaped_x = x.reshape((-1, 1))
reshaped_x, reshaped_x.shape

# %%
model.fit(reshaped_x, y)

# %%



