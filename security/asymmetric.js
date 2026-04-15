const crypto = require('crypto')

async function demo(rl, appState) {
  console.log('\n--- 2. Asymmetric Encryption (RSA) ---')

  const plaintext = await rl.question(
    'Enter the secret message to encrypt with RSA: ',
  )

  console.log('\nGenerating RSA Keys (This may take a moment)...')
  const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
    modulusLength: 2048,
    publicKeyEncoding: { type: 'spki', format: 'pem' },
    privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
  })

  appState.keyPair = { publicKey, privateKey }

  console.log('RSA Keys Generated Successfully.')
  console.log(`Public Key (Snippet): ${publicKey}`)

  // Encrypt with Public Key
  const encryptedData = crypto.publicEncrypt(publicKey, Buffer.from(plaintext))
  console.log(`\nOriginal Text: ${plaintext}`)
  console.log(`Encrypted (Base64): ${encryptedData}`)

  // Decrypt with Private Key
  const decryptedData = crypto.privateDecrypt(privateKey, encryptedData)
  console.log(`Decrypted Text: ${decryptedData.toString('utf8')}`)

  await rl.question('\nPress Enter to return to the main menu...')
}

module.exports = { demo }
