function calculateMoney(input) {
    let puzzel = 2.60
    let doll = 3
    let teddyBear = 4.10
    let minion = 8.20
    let truck = 2

    let tripPrice = Number(input[0])
    let numberOfPuzzels = Number(input[1])
    let numberOfDolls = Number(input[2])
    let numberOfBears = Number(input[3])
    let numberOfminions = Number(input[4])
    let numberOfTrucks = Number(input[5])

    let moneyForPuzzels = numberOfPuzzels * puzzel
    let moneyForDolls = numberOfDolls * doll
    let moneyForBears = numberOfBears * teddyBear
    let moneyForMinions = numberOfminions * minion
    let moneyForTrucks = numberOfTrucks * truck
    let numberOfToys = numberOfPuzzels + numberOfDolls + numberOfBears + numberOfminions + numberOfTrucks
 
    let moneyForEverything = moneyForPuzzels + moneyForDolls + moneyForBears + moneyForMinions + moneyForTrucks
    
    
    if (numberOfToys >= 50){
        moneyForEverything = moneyForEverything * 0.75
    }
    moneyForEverything = moneyForEverything * 0.90

    
    let moneyLeft = Math.abs(tripPrice - moneyForEverything).toFixed(2)

    if (moneyForEverything >= tripPrice){
        console.log(`Yes! ${moneyLeft} lv left.`)
    } else {
        console.log(`Not enough money! ${moneyLeft} lv needed.`)
    }
}
calculateMoney(["40.8",
"20",
"25",
"30",
"50",
"10"])