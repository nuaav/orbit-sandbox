def format_money(amount, currency):
    if currency == "USD":
        symbol = "$"
    elif currency == "EUR":
        symbol = "€"
    else:
        symbol = "₹"
    return f"{symbol}{amount:,.2f}"
