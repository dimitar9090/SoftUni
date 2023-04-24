function moneyForRepair(input){
    let nilonPerMeter = 1.50;
    let paintPerliter = 14.50;
    let thinnerPerLiter = 5;

    let nilonNeeded = Number(input[0]);
    let painNeeded = Number(input[1]);
    let thinnerNeeded = Number(input[2]);
    let hoursrepairsNeeded = Number(input[3]);

    let moneyForNilon = (nilonNeeded + 2) * nilonPerMeter
    let moneyForPaint = (painNeeded * 1.10) * paintPerliter
    let moneyForThinner = thinnerNeeded * thinnerPerLiter
    let bag = 0.40

    let sumForAllMaterials = moneyForNilon + moneyForPaint + moneyForThinner + bag
    let sumForRepairs = (sumForAllMaterials * 0.30) * hoursrepairsNeeded

    console.log(sumForAllMaterials + sumForRepairs)
}
moneyForRepair(["10","11","4","8"])