def apply_discount(amount, percent):
    if percent < 0:
        raise ValueError("Discount percent cannot be negative")
    return amount - (amount * percent / 100)
