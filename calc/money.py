def format_money(amount, currency="INR"):
    if currency == "USD":
        return f"${amount:,.2f}"
    if currency == "EUR":
        return f"€{amount:,.2f}"
    return f"₹{amount:,.2f}"
