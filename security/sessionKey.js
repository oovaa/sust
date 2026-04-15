const crypto = require('crypto')

async function demo(rl, appState) {
  console.log('\n--- 3. Session Key Distribution ---')

  if (!appState.keyPair) {
    console.log(
      'Error: Please run the Asymmetric Encryption (RSA) module first to generate keys!',
    )
    await rl.question('\nPress Enter to return to the main menu...')
    return
  }

  const sessionKey = crypto.randomBytes(32)
  console.log(`Generated Session Key (Hex): ${sessionKey.toString('hex')}`)

  const encryptedSessionKey = crypto.publicEncrypt(
    appState.keyPair.publicKey,
    sessionKey,
  )
  console.log(
    `Encrypted Session Key (Base64): ${encryptedSessionKey.toString('base64').substring(0, 60)}...`,
  )

  const decryptedSessionKey = crypto.privateDecrypt(
    appState.keyPair.privateKey,
    encryptedSessionKey,
  )
  console.log(
    `Decrypted Session Key (Hex): ${decryptedSessionKey.toString('hex')}`,
  )

  if (sessionKey.equals(decryptedSessionKey)) {
    console.log('Success: Session key securely distributed and verified!')
  }

  await rl.question('\nPress Enter to return to the main menu...')
}

module.exports = { demo }
