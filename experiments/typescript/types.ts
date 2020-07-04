let myString: string;
let myNum: number;
let myBool: boolean;
let myVar: any;

myString = 'Hello world';
myNum = 22;
myNum = 0x00d;
myBool = false;

let strArr: string[];
let numArr: Array<number>;
let strNumTuple: [string, number];

numArr = [1, 3, 4];
strArr = ['Hello', 'World'];
strNumTuple = ['The answer', 42];

console.log(myString);
console.log(myNum);
console.log(myVar);
console.log(strArr);
console.log(numArr);
console.log(strNumTuple);