def format_money(amount, currency):
    if currency == "USD":
        return "${:,.2f}".format(amount)
    if currency == "EUR":
        return "€{:,.2f}".format(amount)
    return "₹{:,.2f}".format(amount)
