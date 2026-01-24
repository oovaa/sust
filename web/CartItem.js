/* CartItem Class Module */
export class CartItem {
    constructor(product, quantity) {
        this.product = product;
        this.quantity = quantity;
    }

    // Method to calculate total price for this item
    getTotal() {
        return this.quantity * this.product.price;
    }
}