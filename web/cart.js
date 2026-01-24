/* Project 4 - Dynamic Shopping Cart */

document.addEventListener('DOMContentLoaded', () => {
  // Select DOM elements
  const cartBody = document.getElementById('cart-body')
  const taxInput = document.getElementById('tax-rate')
  const shippingInput = document.getElementById('shipping-threshold')
  const clearCartBtn = document.getElementById('clear-cart')

  const subtotalEl = document.getElementById('subtotal')
  const taxEl = document.getElementById('tax')
  const shippingEl = document.getElementById('shipping')
  const grandTotalEl = document.getElementById('grand-total')

  // Helper: Calculate Total for an item
  function calculateTotal(quantity, price) {
    return quantity * price
  }

  // Helper: Output a single Cart Row
  function outputCartRow(item, itemTotal) {
    const tr = document.createElement('tr')

    // 1. Product Column (Title + Image)
    const tdProduct = document.createElement('td')
    tdProduct.className = 'product-cell'

    const img = document.createElement('img')
    img.src = item.product.filename
    img.alt = item.product.title
    img.style.width = '60px'
    img.style.height = 'auto'
    img.style.marginRight = '10px'
    img.style.verticalAlign = 'middle'

    const span = document.createElement('span')
    span.textContent = item.product.title

    tdProduct.appendChild(img)
    tdProduct.appendChild(span)
    tr.appendChild(tdProduct)

    // 2. Price Column
    const tdPrice = document.createElement('td')
    tdPrice.textContent = `$${item.product.price.toFixed(2)}`
    tr.appendChild(tdPrice)

    // 3. Quantity Column
    const tdQty = document.createElement('td')
    tdQty.textContent = item.quantity
    tr.appendChild(tdQty)

    // 4. Total Column
    const tdTotal = document.createElement('td')
    tdTotal.textContent = `$${itemTotal.toFixed(2)}`
    tr.appendChild(tdTotal)

    // 5. Action Column (Remove Button)
    const tdAction = document.createElement('td')
    const removeBtn = document.createElement('button')
    removeBtn.textContent = 'Remove'
    removeBtn.className = 'btn-remove'

    // Event Listener: Remove Item
    removeBtn.addEventListener('click', () => {
      // Remove row from DOM
      tr.remove()

      // Remove item from global cart array
      const index = cart.indexOf(item)
      if (index > -1) {
        cart.splice(index, 1)
      }

      // Recalculate totals
      updateTotals()
    })

    tdAction.appendChild(removeBtn)
    tr.appendChild(tdAction)

    // Append row to table body
    cartBody.appendChild(tr)
  }

  // Function to calculate and update dashboard totals
  function updateTotals() {
    let subtotal = 0

    // Sum of all item totals
    cart.forEach((item) => {
      subtotal += calculateTotal(item.quantity, item.product.price)
    })

    // Get Tax Rate and Threshold from inputs
    const taxRate = parseFloat(taxInput.value) || 0
    const shippingThreshold = parseFloat(shippingInput.value) || 0

    // Calculate Tax
    const taxAmount = subtotal * (taxRate / 100)

    // Calculate Shipping
    // $40 if subtotal is below threshold, otherwise $0
    const shippingAmount =
      subtotal > 0 && subtotal < shippingThreshold ? 40.0 : 0

    // Grand Total
    const grandTotal = subtotal + taxAmount + shippingAmount

    // Update DOM
    subtotalEl.textContent = `$${subtotal.toFixed(2)}`
    taxEl.textContent = `$${taxAmount.toFixed(2)}`
    shippingEl.textContent = `$${shippingAmount.toFixed(2)}`
    grandTotalEl.textContent = `$${grandTotal.toFixed(2)}`
  }

  // Initial Render Loop
  function renderCart() {
    // Clear existing rows
    cartBody.innerHTML = ''

    cart.forEach((item) => {
      const total = calculateTotal(item.quantity, item.product.price)
      outputCartRow(item, total)
    })

    updateTotals()
  }

  // --- Event Listeners ---

  // Inputs: Recalculate on change
  taxInput.addEventListener('input', updateTotals)
  shippingInput.addEventListener('input', updateTotals)

  // Clear Cart Button
  clearCartBtn.addEventListener('click', () => {
    // Remove all rows
    cartBody.innerHTML = ''

    // Clear array
    cart.length = 0

    // Reset totals
    updateTotals()
  })

  // Run initial render
  renderCart()
})
