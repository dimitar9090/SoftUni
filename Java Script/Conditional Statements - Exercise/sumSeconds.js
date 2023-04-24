function finalTime(input){
    let firstTime = Number(input[0]);
    let secondTime = Number(input[1]);
    let thirdTime = Number(input[2]);

    let finalTimeInMinutes = firstTime + secondTime + thirdTime;

    let minutes = Math.floor(finalTimeInMinutes / 60);
    let seconds = finalTimeInMinutes % 60;

    if (seconds < 10) {
        console.log(`${minutes}:0${seconds}`);
    } else {
        console.log(`${minutes}:${seconds}`);
    }
}
finalTime(["35", "45", "44"]);