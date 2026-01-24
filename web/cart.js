/* Project 5 - Modular Cart Enhancement */
import { CartItem } from './CartItem.js'

document.addEventListener('DOMContentLoaded', () => {
  // State to hold CartItem objects
  let cartItems = []

  // Select DOM elements
  const cartBody = document.getElementById('cart-body')
  const taxInput = document.getElementById('tax-rate')
  const shippingInput = document.getElementById('shipping-threshold')
  const clearCartBtn = document.getElementById('clear-cart')
  const searchInput = document.getElementById('search-filter') // New Search Input

  const subtotalEl = document.getElementById('subtotal')
  const taxEl = document.getElementById('tax')
  const shippingEl = document.getElementById('shipping')
  const grandTotalEl = document.getElementById('grand-total')

  // --- 1. Fetch Data ---
  fetch('cart.json')
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      return response.json()
    })
    .then((data) => {
      // Convert JSON data into CartItem instances
      cartItems = data.map((item) => new CartItem(item.product, item.quantity))

      // Initial Render
      renderCart(cartItems)
    })
    .catch((error) => {
      console.error('Error fetching cart data:', error)
      cartBody.innerHTML =
        '<tr><td colspan="5">Error loading cart data.</td></tr>'
    })

  // --- 2. Render Function ---
  function renderCart(itemsToRender) {
    cartBody.innerHTML = '' // Clear table

    itemsToRender.forEach((item) => {
      const tr = document.createElement('tr')

      // Product Cell
      const tdProduct = document.createElement('td')
      tdProduct.className = 'product-cell'

      const img = document.createElement('img')
      img.src = item.product.filename
      img.alt = item.product.title

      const span = document.createElement('span')
      span.textContent = item.product.title

      tdProduct.appendChild(img)
      tdProduct.appendChild(span)
      tr.appendChild(tdProduct)

      // Price Cell
      const tdPrice = document.createElement('td')
      tdPrice.textContent = `$${item.product.price.toFixed(2)}`
      tr.appendChild(tdPrice)

      // Quantity Cell
      const tdQty = document.createElement('td')
      tdQty.textContent = item.quantity
      tr.appendChild(tdQty)

      // Total Cell (Using Class Method)
      const tdTotal = document.createElement('td')
      tdTotal.textContent = `$${item.getTotal().toFixed(2)}`
      tr.appendChild(tdTotal)

      // Actions Cell
      const tdAction = document.createElement('td')
      const removeBtn = document.createElement('button')
      removeBtn.textContent = 'Remove'

      // Remove Logic
      removeBtn.addEventListener('click', () => {
        // Find index of item in the main array
        const index = cartItems.indexOf(item)
        if (index > -1) {
          cartItems.splice(index, 1)
          // Re-render based on current filter state
          filterAndRender()
        }
      })

      tdAction.appendChild(removeBtn)
      tr.appendChild(tdAction)

      cartBody.appendChild(tr)
    })

    // Always update totals based on the *current* items in the cart
    updateTotals()
  }

  // --- 3. Update Totals Function ---
  function updateTotals() {
    // Calculate subtotal using Class Method reduce
    const subtotal = cartItems.reduce((sum, item) => sum + item.getTotal(), 0)

    const taxRate = parseFloat(taxInput.value) || 0
    const shippingThreshold = parseFloat(shippingInput.value) || 0

    const taxAmount = subtotal * (taxRate / 100)

    // Shipping is $40 if subtotal < threshold, else $0. (Also 0 if cart is empty)
    let shippingAmount = 0
    if (subtotal > 0 && subtotal < shippingThreshold) {
      shippingAmount = 40.0
    }

    const grandTotal = subtotal + taxAmount + shippingAmount

    // Update DOM
    subtotalEl.textContent = `$${subtotal.toFixed(2)}`
    taxEl.textContent = `$${taxAmount.toFixed(2)}`
    shippingEl.textContent = `$${shippingAmount.toFixed(2)}`
    grandTotalEl.textContent = `$${grandTotal.toFixed(2)}`
  }

  // --- 4. Event Listeners ---

  // Inputs
  taxInput.addEventListener('input', updateTotals)
  shippingInput.addEventListener('input', updateTotals)

  // Clear Cart
  clearCartBtn.addEventListener('click', () => {
    cartItems = []
    renderCart(cartItems)
  })

  // Optional: Filter Feature
  searchInput.addEventListener('input', (e) => {
    filterAndRender()
  })

  function filterAndRender() {
    const searchTerm = searchInput.value.toLowerCase()

    // Filter items based on title
    const filteredItems = cartItems.filter((item) =>
      item.product.title.toLowerCase().includes(searchTerm),
    )

    renderCart(filteredItems)
  }
})
