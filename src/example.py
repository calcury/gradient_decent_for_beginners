lr = 0.1
x = 2
for _ in range(100):
    Loss = (x ** 2) / 2 # Loss function
    Gradient = x # Gradient
    x = x - lr * Gradient # Update param
print(f'x:{x:.2f}; Loss:{Loss:.2f}')