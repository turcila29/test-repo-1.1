"use strict";

function sub(a, b) {
    return a - b;
}

console.log(sub(10,8));


const greeting = function (name, age, gender){
    return console.log(`My name is ${name}, i am ${age} years old, and of gender ${gender}`);
}

greeting("andrei", 23, "male");

const powerUp = (num1, num2) => Math.pow(num1, num2);

console.log(powerUp(4, 6));