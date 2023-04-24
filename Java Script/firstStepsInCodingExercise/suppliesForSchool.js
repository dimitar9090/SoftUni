function moneyNeeded(input){
    let packOfPens = 5.80;
    let packOfMarkers = 7.20;
    let preperation = 1.20;

    let numberPensPacks = Number(input[0]);
    let numberMarkersPacks = Number(input[1]);
    let litersOfPreperation = Number(input[2]);
    let precentDiscount = Number(input[3]) / 100;

    let moneyForPens = numberPensPacks * packOfPens
    let moneyForMarkers = numberMarkersPacks * packOfMarkers
    let moneyForPreperation = litersOfPreperation * preperation
    let moneyForAllMaterials = moneyForMarkers + moneyForPens + moneyForPreperation
    let finalPrice = moneyForAllMaterials - (moneyForAllMaterials * precentDiscount)
    console.log(finalPrice)
}
moneyNeeded(["2","3","4","25"])