//javascript file referenced
console.log('Hello World');
//let name = 'Simon';
//let fistName = 'Simon';
//let lastName = 'Schirber';

//can't change constants
const interestRate = 1;
console.log(interestRate)

let name = 'Simon'; //String literal
let age = 30; // Number Literal
let isApproved = true; //Boolean Literal
let firstname = undefined; //undefined
let lastName = null; //clear value using null

let person = {name: 'Simon', age: 30};//literal
person.name = 'John';
person['name'] = 'Mary';

let selectedColors = ['red', 'blue']; // array
selectedColors[1] = 'green';
console.log(typeof selectedColors)


//function
function greet(xname, xlastname) { 
    console.log('Hello ' + xname + ' ' + xlastname);
}
greet('John' , 'Doe');


