NAME_WIDTH = 30


def _format_product_name(name):
    if len(name) > NAME_WIDTH:
        name = name[: NAME_WIDTH - 3] + "..."
    return f"{name:<{NAME_WIDTH}}"


def format_report(products):
    header = f"{_format_product_name('Product Name')} | Price | Quantity | Total"
    lines = [header, "-" * len(header)]
    for product in products:
        total = product["price"] * product["quantity"]
        lines.append(
            f"{_format_product_name(product['name'])} | "
            f"{product['price']:>10.2f} | {product['quantity']:>8} | {total:>10.2f}"
        )
    return "\n".join(lines)
