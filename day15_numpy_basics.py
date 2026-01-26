import numpy as np

# Basic array
ages = np.array([23, 25, 22, 30, 28])
print("Ages:", ages)

# Vectroized operations
print("Ages + 5:", ages + 5)
print("Ages * 2:", ages * 2)

# Stats
print("Mean:", ages.mean())
print("Std:", ages.std())
print("Max:", ages.max())
print("Min:", ages.min())

# 2D Matrix
matrix = np.array([[1,2,3],[4,5,6]])
print("\nMatrix:\n", matrix)
print("Shape:", matrix.shape)

# Indexing
print("First row:", matrix[0])
print("Element [1,2]:", matrix[1,2])

# ML-style normalization
saleries = np.array([30000, 40000, 25000, 52000, 47000])
normalized = (saleries - saleries.mean()) / saleries.std()
print("\nNormalized saleries:", normalized)
