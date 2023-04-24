function fishTank(input){
    let lenght = Number(input[0]);
    let width = Number(input[1]);
    let hight = Number(input[2]);
    let precent = Number(input[3]) / 100;

    let volumeIncm = lenght * width * hight;
    let volumeInLiters = volumeIncm * 0.001;
    
    let letersNeeded = volumeInLiters * (1 - precent);

    console.log(letersNeeded)
}
fishTank(["85","75","47","17"])