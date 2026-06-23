import numpy as np

a = np.array([3, 2])
b = np.array([4, 1])
print(f"a: {a}")
print(f"b: {b}")

dot = np.dot(a, b)                                      # arithmetic form
cos_sim = dot / (np.linalg.norm(a) * np.linalg.norm(b)) # geometric form
angle = np.degrees(np.arccos(cos_sim))

print(f"Dot product: {dot}")
print(f"Cosine similarity: {cos_sim:.3f}")
print(f"Angle: {angle:.1f}°")