const crypto = require('crypto')

async function demo(rl) {
  console.log('\n--- 1. Symmetric Encryption (AES-256) ---')

  // Get user input
  const plaintext = await rl.question(
    'Enter the plaintext message to encrypt: ',
  )
  const userKey = await rl.question('Enter a secret password/key: ')

  // AES-256 requires exactly a 32-byte key. We hash the user's input to ensure correct length.
  const key = crypto.createHash('sha256').update(userKey).digest()
  const iv = crypto.randomBytes(16)

  console.log(`\nOriginal Text: ${plaintext}`)
  console.log(`Derived 32-byte Key (Hex): ${key.toString('hex')}`)

  // Encrypt
  const cipher = crypto.createCipheriv('aes-256-cbc', key, iv)
  let encrypted = cipher.update(plaintext, 'utf8', 'hex')
  encrypted += cipher.final('hex')
  console.log(`Ciphertext: ${encrypted}`)

  // Decrypt
  const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv)
  let decrypted = decipher.update(encrypted, 'hex', 'utf8')
  decrypted += decipher.final('utf8')
  console.log(`Decrypted Text: ${decrypted}`)

  await rl.question('\nPress Enter to return to the main menu...')
}

module.exports = { demo }
