let age=25;
age=40; // literal later changes but you can't redeclare 'let'
console.log(age);
console.log("=======================");

const __ID__ =3.14;  // declaration + initialization both together is only allowed 
console.log(__ID__);
console.log("=======================");
var userId;
userId=10;
userId=20;
console.log(userId);
let n1= 27;
let n2= 31;
let n3= n1++ + n2++; // 27 + 31 = 58
let n4 = n1++;  //27 +1 //28
let n5= n2++; // 31 +1 // 32
let n6 =n4 + n5;