function restaurant(input){
    let chikenMenu = 10.35;
    let fishMenu = 12.40;
    let veganMenu = 8.15;
    let delivery = 2.50;

    let numberOfChickenMenus = Number(input[0]);
    let numberOfFishMenus = Number(input[1]);
    let numberOfVeganMenus = Number(input[2]);

    let priceForChiken = numberOfChickenMenus * chikenMenu
    let priceforFish = numberOfFishMenus * fishMenu
    let priceForVegan = numberOfVeganMenus * veganMenu
    let priceForAllMenus = priceForChiken + priceForVegan + priceforFish

    let dessertPrice = priceForAllMenus * 0.20

    let finalPrice = priceForAllMenus + dessertPrice + delivery
    
    console.log(finalPrice)
}
restaurant(["2","4","3"])