//  Question 1

let darthVader = {
    allegiance : "Empire",
    weapon : "lightsabre",
    sith : true
};

let jedi;
if (darthVader.sith == true){
    jedi = false;
}
else{
    jedi = true;
}


//  Qeustion 2
console.log(`Darth Vader's allegiance is to the ${darthVader.allegiance}`);
console.log(`Darth vader's weapong of choice is a ${darthVader.weapon}`);
console.log(`Darth Vader is a sith? ${darthVader.sith}`);
console.log(`Darth Vader is a Jedi? ${!darthVader.sith}`);


//  Question 3
let myArray = ["hello", "everyone"];
console.log(myArray.length);

console.log(myArray.push("my", "favourite", "group"));

console.log(myArray.length);

myArray.shift();

// console.log(myArray.pop());

// for (let i = 0; i< myArray.length; i++){
//     console.log(myArray[i]);
// }

for (let myWords of myArray) {
    console.log(myWords);
}








