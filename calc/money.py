def format_money(amount, currency):
    formatted_amount = f"{amount:,.2f}"
    if currency == "USD":
        return f"${formatted_amount}"
    if currency == "EUR":
        return f"€{formatted_amount}"
    return f"₹{formatted_amount}"
