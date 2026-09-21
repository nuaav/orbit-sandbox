export type LineItem = {
  unitPrice: number;
  quantity: number;
};

export type Invoice = {
  items: LineItem[];
  discountPercent?: number;
  taxPercent?: number;
};

const roundHalfUp = (value: number, decimals: number): number => {
  const factor = 10 ** decimals;
  return Math.round((value + Number.EPSILON) * factor) / factor;
};

export const calculateInvoiceTotal = (invoice: Invoice): number => {
  const subtotal = invoice.items.reduce(
    (sum, item) => sum + item.unitPrice * item.quantity,
    0
  );
  const discountPercent = invoice.discountPercent ?? 0;
  const taxPercent = invoice.taxPercent ?? 0;

  const discountedSubtotal = subtotal * (1 - discountPercent / 100);
  const taxedTotal = discountedSubtotal * (1 + taxPercent / 100);

  return roundHalfUp(taxedTotal, 2);
};
