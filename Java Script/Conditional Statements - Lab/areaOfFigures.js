function area(input) {
    let figure = (input[0]);
    if (figure === "square") {
        let side = Number(input[1]);
        console.log((side * side).toFixed(3));
    } else if (figure === "rectangle"){
        let sideOne = Number(input[1]);
        let sideTow = Number(input[2]);
        let areaRectangle = sideOne * sideTow;
        console.log((areaRectangle).toFixed(3));
    } else if (figure === "circle"){
        let r = Number(input[1]);
        let areaCircle = Math.PI * Math.pow(r,2)
        console.log((areaCircle).toFixed(3))
    } else if (figure === "triangle"){
        let base = Number(input[1]);
        let height = Number(input[2]);
        let areaTriangle = (base * height) / 2;
        console.log((areaTriangle).toFixed(3));
    }
}
area(["square", "5"]);