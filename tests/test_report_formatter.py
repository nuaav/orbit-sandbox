from src.report_formatter import format_report


class _Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getitem__(self, key):
        return getattr(self, key)


def _line_for(report, text):
    for line in report.splitlines():
        if text in line:
            return line
    raise AssertionError(f"No line found containing: {text}")


def _name_field(line):
    return line.split(" | ")[0]


def test_report_alignment_truncates_and_pads_product_name_column():
    long_name = "Extra Long Product Name That Exceeds Thirty Characters"
    short_name = "Short Name"
    products = [_Product(long_name, 10.0, 2), _Product(short_name, 5.0, 1)]

    report = format_report(products)

    truncated = long_name[:27] + "..."
    line_long = _line_for(report, truncated)
    line_short = _line_for(report, short_name)

    assert _name_field(line_long) == truncated.ljust(30)
    assert _name_field(line_short) == short_name.ljust(30)
    assert line_long.index(" | ") == line_short.index(" | ")


def test_report_alignment_with_equal_width_names():
    name_one = "A" * 30
    name_two = "B" * 30
    products = [_Product(name_one, 1.0, 1), _Product(name_two, 2.0, 2)]

    report = format_report(products)

    line_one = _line_for(report, name_one)
    line_two = _line_for(report, name_two)

    assert _name_field(line_one) == name_one
    assert _name_field(line_two) == name_two
    assert line_one.index(" | ") == line_two.index(" | ")
