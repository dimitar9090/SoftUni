//сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
function finalsum(input) {
    let depositeSum = Number(input[0]);
    let numberOfMonths = Number(input[1]);
    let yearPrecent = Number(input[2]) / 100;
    let finalMoney = depositeSum + numberOfMonths * ((depositeSum * yearPrecent) / 12);
    console.log(finalMoney)
}
finalsum(["200","3","5.7"])