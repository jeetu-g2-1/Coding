## Python Print Output Note

In Python, using `print()` with a comma inserts an automatic space between elements, which may disrupt pattern formatting.

✅ Use `' + '` for accurate control over spacing and output.

### Example:
```python
print(' ' * spaces + '*' * stars)  # Correct
print(' ' * spaces, '*' * stars)   # Adds unwanted space
