/* Project 4 - Dynamic Shopping Cart */

document.addEventListener('DOMContentLoaded', () => {
  const cartBody = document.getElementById('cart-body')
  const taxInput = document.getElementById('tax-rate')
  const shippingInput = document.getElementById('shipping-threshold')
  const clearCartBtn = document.getElementById('clear-cart')

  const subtotalEl = document.getElementById('subtotal')
  const taxEl = document.getElementById('tax')
  const shippingEl = document.getElementById('shipping')
  const grandTotalEl = document.getElementById('grand-total')

  function calculateTotal(quantity, price) {
    return quantity * price
  }

  function outputCartRow(item, itemTotal) {
    const tr = document.createElement('tr')

    const tdProduct = document.createElement('td')
    tdProduct.className = 'product-cell'

    const img = document.createElement('img')
    img.src = item.product.filename
    img.alt = item.product.title
    img.style.width = '60px' // styling for image
    img.style.marginRight = '10px'
    img.style.verticalAlign = 'middle'

    const span = document.createElement('span')
    span.textContent = item.product.title

    tdProduct.appendChild(img)
    tdProduct.appendChild(span)
    tr.appendChild(tdProduct)

     const tdPrice = document.createElement('td')
    tdPrice.textContent = `$${item.product.price.toFixed(2)}`
    tr.appendChild(tdPrice)

    const tdQty = document.createElement('td')
    tdQty.textContent = item.quantity
    tr.appendChild(tdQty)

    const tdTotal = document.createElement('td')
    tdTotal.textContent = `$${itemTotal.toFixed(2)}`
    tr.appendChild(tdTotal)

    const tdAction = document.createElement('td')
    const removeBtn = document.createElement('button')
    removeBtn.textContent = 'Remove'
    removeBtn.className = 'btn-remove'

    removeBtn.addEventListener('click', () => {
      tr.remove()

      const index = cart.indexOf(item)
      if (index > -1) {
        cart.splice(index, 1)
      }

      updateTotals()
    })

    tdAction.appendChild(removeBtn)
    tr.appendChild(tdAction)

    cartBody.appendChild(tr)
  }

  function updateTotals() {
    let subtotal = 0

    cart.forEach((item) => {
      subtotal += calculateTotal(item.quantity, item.product.price)
    })

    const taxRate = parseFloat(taxInput.value) || 0
    const shippingThreshold = parseFloat(shippingInput.value) || 0

    const taxAmount = subtotal * (taxRate / 100)

    const shippingAmount =
      subtotal > 0 && subtotal < shippingThreshold ? 40.0 : 0

    const grandTotal = subtotal + taxAmount + shippingAmount

    subtotalEl.textContent = `$${subtotal.toFixed(2)}`
    taxEl.textContent = `$${taxAmount.toFixed(2)}`
    shippingEl.textContent = `$${shippingAmount.toFixed(2)}`
    grandTotalEl.textContent = `$${grandTotal.toFixed(2)}`
  }

  function renderCart() {
    cartBody.innerHTML = ''

    cart.forEach((item) => {
      const total = calculateTotal(item.quantity, item.product.price)
      outputCartRow(item, total)
    })

    updateTotals()
  }

  taxInput.addEventListener('input', updateTotals)
  shippingInput.addEventListener('input', updateTotals)

  clearCartBtn.addEventListener('click', () => {
    cartBody.innerHTML = ''

    cart.length = 0

    updateTotals()
  })

  renderCart()
})
