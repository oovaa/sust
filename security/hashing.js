const crypto = require('crypto')

async function demo(rl) {
  console.log('\n--- 4. Hash Algorithm (SHA-256) ---')

  console.log(
    'To demonstrate the avalanche effect, enter a message, and then enter a slightly modified version of it.',
  )
  const text1 = await rl.question('Enter the first message: ')
  const text2 = await rl.question('Enter the slightly modified message: ')

  const hash1 = crypto.createHash('sha256').update(text1).digest('hex')
  const hash2 = crypto.createHash('sha256').update(text2).digest('hex')

  console.log(`\nInput 1: "${text1}"`)
  console.log(`Hash 1:  ${hash1}`)
  console.log(`\nInput 2: "${text2}"`)
  console.log(`Hash 2:  ${hash2}`)

  console.log(
    '\nAvalanche Effect Demonstrated: Notice how completely different the second hash is from the first.',
  )

  await rl.question('\nPress Enter to return to the main menu...')
}

module.exports = { demo }
