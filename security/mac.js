const crypto = require('crypto')

async function demo(rl) {
  console.log('\n--- 5. Message Authentication Code (HMAC-SHA256) ---')

  const message = await rl.question(
    'Enter the message you want to authenticate: ',
  )
  const secretKey = await rl.question('Enter a shared secret key: ')

  console.log(`\nMessage: ${message}`)
  console.log(`Secret Key: ${secretKey}`)

  const mac = crypto
    .createHmac('sha256', secretKey)
    .update(message)
    .digest('hex')
  console.log(`Generated MAC: ${mac}`)

  await rl.question('\nPress Enter to return to the main menu...')
}

module.exports = { demo }
