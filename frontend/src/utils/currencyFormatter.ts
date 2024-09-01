export default class CurrencyFormatter {

    public static format(value: number|string): string {
        return `$${Number(value).toFixed(2)}`;
    }
    
}