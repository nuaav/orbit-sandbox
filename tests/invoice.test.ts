import { calculateInvoiceTotal } from "../src/invoice";

describe("calculateInvoiceTotal", () => {
  it("rounds half up only at final total with discount-before-tax on subtotal", () => {
    const invoice = {
      items: [{ unitPrice: 2.003, quantity: 5 }],
      discountPercent: 10,
      taxPercent: 5,
    };

    expect(calculateInvoiceTotal(invoice)).toBe(9.46);
  });
});
