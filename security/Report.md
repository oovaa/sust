### Core Cryptographic Modules: Concepts and Implementation

This report details the core mathematical concepts and JavaScript implementations for the five foundational cryptographic modules using the native Node.js `crypto` library.

#### 1. Symmetric Encryption (AES-256-CBC)

**The Concept:** Symmetric encryption uses a single shared secret key to both lock and unlock data. Advanced Encryption Standard (AES) is the global standard. Using **AES-256-CBC**, the algorithm requires a 256-bit (32-byte) key. Cipher Block Chaining (CBC) mode introduces a random 16-byte Initialization Vector (IV). The IV ensures that encrypting the same message multiple times yields different ciphertexts, preventing attackers from recognizing patterns.

**Core Implementation:**

```javascript
const crypto = require('crypto');

// 1. Derive a strict 32-byte key using SHA-256 and generate a 16-byte IV
const key = crypto.createHash('sha256').update("user_password").digest(); 
const iv = crypto.randomBytes(16);

// 2. Encrypt
const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
let encrypted = cipher.update("Secret Message", 'utf8', 'hex');
encrypted += cipher.final('hex');

// 3. Decrypt
const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
let decrypted = decipher.update(encrypted, 'hex', 'utf8');
decrypted += decipher.final('utf8');

```

#### 2. Asymmetric Encryption (RSA)

**The Concept:** Asymmetric encryption solves the problem of securely sharing a key by generating a mathematically linked pair: a **Public Key** (shared openly to encrypt data) and a **Private Key** (kept secret to decrypt data). RSA relies on the computational difficulty of factoring large prime numbers. Data locked by the public key can *only* be unlocked by the corresponding private key.

**Core Implementation:**

```javascript
// 1. Generate the 2048-bit RSA Key Pair
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
    modulusLength: 2048,
    publicKeyEncoding: { type: 'spki', format: 'pem' },
    privateKeyEncoding: { type: 'pkcs8', format: 'pem' }
});

// 2. Encrypt using the Public Key (requires a Buffer)
const encryptedData = crypto.publicEncrypt(publicKey, Buffer.from("Secret Message"));

// 3. Decrypt using the Private Key
const decryptedData = crypto.privateDecrypt(privateKey, encryptedData);
console.log(decryptedData.toString('utf8'));

```

#### 3. Session Key Distribution (Hybrid Encryption)

**The Concept:** RSA is highly secure for key distribution but too slow for encrypting large amounts of data. AES is fast but requires securely sharing a single key. Hybrid encryption merges them: the system generates a fast, temporary AES symmetric key (the "Session Key"), encrypts that Session Key using the recipient's slow but secure RSA Public Key, and transmits it. Once decrypted by the recipient, both parties share the AES key and use it for fast communication.

**Core Implementation:**

```javascript
// 1. Generate a temporary Symmetric AES key (32 bytes)
const sessionKey = crypto.randomBytes(32);

// 2. Encrypt the Session Key using the receiver's RSA Public Key
const encryptedSessionKey = crypto.publicEncrypt(publicKey, sessionKey);

// 3. The receiver decrypts the Session Key using their RSA Private Key
const decryptedSessionKey = crypto.privateDecrypt(privateKey, encryptedSessionKey);
// Both parties now possess the identical 'sessionKey' for AES encryption.

```

#### 4. Cryptographic Hashing (SHA-256 & The Avalanche Effect)

**The Concept:** Hashing is a one-way mathematical function that converts data of any size into a fixed-length string (a fingerprint). It cannot be decrypted or reversed. A secure hash like SHA-256 exhibits the **Avalanche Effect**: changing even a single bit of the input data completely scrambles the resulting hash. This allows systems to verify data integrity and detect corruption or tampering.

**Core Implementation:**

```javascript
// Hash the original message
const hash1 = crypto.createHash('sha256').update("Data to hash").digest('hex');

// Hash a slightly modified message to demonstrate the Avalanche Effect
const hash2 = crypto.createHash('sha256').update("data to hash").digest('hex');

// hash1 and hash2 will be completely different 64-character hexadecimal strings.

```

#### 5. Message Authentication Code (HMAC-SHA256)

**The Concept:** While standard hashing proves a message wasn't corrupted, it doesn't prove *who* sent it (an attacker could alter the message and send a new hash). A Hash-based Message Authentication Code (HMAC) solves this by blending a shared secret key into the hashing math. To generate a valid HMAC, a user must possess both the exact message and the secret key, ensuring both data integrity and sender authenticity.

**Core Implementation:**

```javascript
const message = "Transfer $1000";
const secretKey = "BankSharedSecret123";

// Generate an HMAC by combining the SHA-256 algorithm with the secret key
const mac = crypto.createHmac('sha256', secretKey).update(message).digest('hex');

```