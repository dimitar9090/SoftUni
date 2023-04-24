function hoursPerday(input){
    let numberOfPages = Number(input[0]);
    let pagesPerHour = Number(input[1]);
    let numberOfDays = Number(input[2]);
    let sumOfHours = numberOfPages / pagesPerHour
    let hoursNeedPerday = sumOfHours / numberOfDays
    console.log(hoursNeedPerday)
}
hoursPerday(["212","20","2"])