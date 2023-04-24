function basketballSeason(input){
    let yearTax = Number(input[0]);
    let basketballShoes = yearTax * 0.60;
    let basketballShirt = basketballShoes * 0.80;
    let basketballBall = basketballShirt / 4;
    let basketballAccesories = basketballBall / 5;

    let allMoneyYouNeed = yearTax + basketballShoes + basketballShirt 
    + basketballBall + basketballAccesories

    console.log(allMoneyYouNeed)
}
basketballSeason(["365"])