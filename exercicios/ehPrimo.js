function ehPrimo(num) {
    if (num <= 1) {
        
        return console.log("não é primo");

    } else if (num <= 3) {

        return console.log("é primo");

    } else if (num % 2 === 0 || num % 3 === 0 || num % 5 === 0 || num % 7 === 0) {

        if (num === 2 || num === 3 || num === 5 || num === 7) {

            return console.log("é primo");

        } else {
            
            return console.log("não é primo");

        }
    } else {

        return console.log("é primo");

    }
}

console.log("\nNúmeros Primos:\n")
ehPrimo(2)
ehPrimo(3)
ehPrimo(5)
ehPrimo(7)
ehPrimo(11)
ehPrimo(13)
ehPrimo(17)
ehPrimo(19)

console.log('\nNúmeros Não Primos: \n')
ehPrimo(1)
ehPrimo(4)
ehPrimo(6)
ehPrimo(8)
ehPrimo(9)
ehPrimo(10)
ehPrimo(12)
ehPrimo(14)
ehPrimo(15)
