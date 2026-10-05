def apply_discount(amount, percent):
    if percent < 0:
        raise ValueError("Discount percent cannot be negative")
    if percent > 100:
        raise ValueError("discount percent must be between 0 and 100")
    return amount * (1 - percent / 100)
