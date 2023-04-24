function movieMaker(input){
    let budget = Number(input[0]);
    let numberOfPeople = Number(input[1]);
    let priceForClothes = Number(input[2]);
    let decorMoney = budget * 0.10;
    let clothesMoney = numberOfPeople * priceForClothes
    if (numberOfPeople > 150){
        clothesMoney *= 0.90
    }
    let finalPriceForMovie = clothesMoney + decorMoney
    let moneyLeft = Math.abs(budget - finalPriceForMovie).toFixed(2)

    if (finalPriceForMovie > budget) {
        console.log(`Not enough money!
        Wingard needs ${moneyLeft} leva more.`)
    } else {
        console.log(`Action! 
        Wingard starts filming with ${moneyLeft} leva left.`)
    }
}

movieMaker(["20000",
"120",
"55.5"])