const readline = require('readline/promises');
const { stdin: input, stdout: output } = require('process');

const symmetric = require('./symmetric');
const asymmetric = require('./asymmetric');
const sessionKey = require('./sessionKey');
const hashing = require('./hashing');
const mac = require('./mac');

const rl = readline.createInterface({ input, output });

const appState = {
    keyPair: null
};

async function showMenu() {
    console.log("\n=========================================");
    console.log("      Cryptography Software System       ");
    console.log("=========================================");
    console.log("1. Symmetric Encryption (AES)");
    console.log("2. Asymmetric Encryption (RSA)");
    console.log("3. Session Key Distribution");
    console.log("4. Hash Function (SHA-256 Avalanche)");
    console.log("5. Message Authentication Code (MAC)");
    console.log("6. Exit");
    
    const answer = await rl.question("Select an option (1-6): ");
    
    switch (answer.trim()) {
        case '1': await symmetric.demo(rl); break;
        case '2': await asymmetric.demo(rl, appState); break;
        case '3': await sessionKey.demo(rl, appState); break;
        case '4': await hashing.demo(rl); break;
        case '5': await mac.demo(rl); break;
        case '6': 
            console.log("Exiting program. Goodbye!");
            rl.close(); 
            return; 
        default:
            console.log("Invalid option. Please try again.");
            break;
    }
    
    // Show menu again after the selected module finishes
    showMenu();
}

showMenu();