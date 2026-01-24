/* Project 4 - Dynamic Shopping Cart 
    [cite_start][cite: 4, 23]
*/

[cite_start]// Ensure code runs after page loads [cite: 25]
document.addEventListener('DOMContentLoaded', () => {
    
    // Select DOM elements
    const cartBody = document.getElementById('cart-body');
    const taxInput = document.getElementById('tax-rate');
    const shippingInput = document.getElementById('shipping-threshold');
    const clearCartBtn = document.getElementById('clear-cart');

    const subtotalEl = document.getElementById('subtotal');
    const taxEl = document.getElementById('tax');
    const shippingEl = document.getElementById('shipping');
    const grandTotalEl = document.getElementById('grand-total');

    [cite_start]// Helper: Calculate Total for an item [cite: 27]
    function calculateTotal(quantity, price) {
        return quantity * price;
    }

    [cite_start]// Helper: Output a single Cart Row [cite: 29]
    function outputCartRow(item, itemTotal) {
        const tr = document.createElement('tr');

        [cite_start]// 1. Product Column (Title + Image) [cite: 31]
        const tdProduct = document.createElement('td');
        tdProduct.className = 'product-cell';
        
        const img = document.createElement('img');
        img.src = item.product.filename; 
        img.alt = item.product.title;
        img.style.width = '80px'; // styling for image
        
        const span = document.createElement('span');
        span.textContent = item.product.title;

        tdProduct.appendChild(img);
        tdProduct.appendChild(span);
        tr.appendChild(tdProduct);

        [cite_start]// 2. Price Column [cite: 32]
        const tdPrice = document.createElement('td');
        tdPrice.textContent = `$${item.product.price.toFixed(2)}`;
        tr.appendChild(tdPrice);

        [cite_start]// 3. Quantity Column [cite: 33]
        const tdQty = document.createElement('td');
        tdQty.textContent = item.quantity;
        tr.appendChild(tdQty);

        [cite_start]// 4. Total Column [cite: 34]
        const tdTotal = document.createElement('td');
        tdTotal.textContent = `$${itemTotal.toFixed(2)}`;
        tr.appendChild(tdTotal);

        [cite_start]// 5. Action Column (Remove Button) [cite: 35]
        const tdAction = document.createElement('td');
        const removeBtn = document.createElement('button');
        removeBtn.textContent = 'Remove';
        
        [cite_start]// Event Listener: Remove Item [cite: 51]
        removeBtn.addEventListener('click', () => {
            [cite_start]// Remove row from DOM [cite: 52]
            tr.remove();
            
            [cite_start]// Remove item from global cart array [cite: 53]
            const index = cart.indexOf(item);
            if (index > -1) {
                cart.splice(index, 1);
            }

            [cite_start]// Recalculate totals [cite: 54]
            updateTotals();
        });

        tdAction.appendChild(removeBtn);
        tr.appendChild(tdAction);

        // Append row to table body
        cartBody.appendChild(tr);
    }

    [cite_start]// Function to calculate and update dashboard totals [cite: 39]
    function updateTotals() {
        let subtotal = 0;

        [cite_start]// Sum of all item totals [cite: 41]
        cart.forEach(item => {
            subtotal += calculateTotal(item.quantity, item.product.price);
        });

        // Get Tax Rate and Threshold from inputs
        const taxRate = parseFloat(taxInput.value) || 0;
        const shippingThreshold = parseFloat(shippingInput.value) || 0;

        [cite_start]// Calculate Tax [cite: 42]
        const taxAmount = subtotal * (taxRate / 100);

        [cite_start]// Calculate Shipping [cite: 43]
        // $40 if subtotal is below threshold, otherwise $0
        const shippingAmount = subtotal < shippingThreshold && subtotal > 0 ? 40.00 : 0;

        [cite_start]// Grand Total [cite: 44]
        const grandTotal = subtotal + taxAmount + shippingAmount;

        [cite_start]// Update DOM [cite: 45]
        subtotalEl.textContent = `$${subtotal.toFixed(2)}`;
        taxEl.textContent = `$${taxAmount.toFixed(2)}`;
        shippingEl.textContent = `$${shippingAmount.toFixed(2)}`;
        grandTotalEl.textContent = `$${grandTotal.toFixed(2)}`;
    }

    [cite_start]// Initial Render Loop [cite: 36]
    function renderCart() {
        // Clear existing rows (useful for re-rendering if needed)
        cartBody.innerHTML = '';

        cart.forEach(item => {
            [cite_start]const total = calculateTotal(item.quantity, item.product.price); // [cite: 37]
            outputCartRow(item, total); [cite_start]// [cite: 38]
        });

        updateTotals();
    }

    // --- Event Listeners ---

    [cite_start]// Inputs: Recalculate on change [cite: 55, 56]
    taxInput.addEventListener('input', updateTotals);
    shippingInput.addEventListener('input', updateTotals);

    [cite_start]// Clear Cart Button [cite: 57]
    clearCartBtn.addEventListener('click', () => {
        [cite_start]// Remove all rows [cite: 58]
        cartBody.innerHTML = '';
        
        [cite_start]// Clear array [cite: 59]
        cart.length = 0; // efficient way to clear array
        
        [cite_start]// Reset totals [cite: 60]
        updateTotals();
    });

    // Run initial render
    renderCart();
});