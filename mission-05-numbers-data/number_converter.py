try:
    decimal = int(input("Enter a decimal integer: "), 10)
except ValueError:
    raise SystemExit("Please enter a whole number in base 10.") from None

print(f"Binary: {bin(decimal)}")
print(f"Hexadecimal: {hex(decimal)}")
