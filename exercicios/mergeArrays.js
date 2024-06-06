const geraArrayAleaotorio = require("./geraArrayAleatorio");

function mergeArrays(arr) {
    const newArr = [];

    for(let i = 0; i < arr.length; i++) {
       for(let j = 0; j < arr[i].length; j++) {
            newArr.push(arr[i][j]);
       }
    };

    return newArr;
}

const arr1 = geraArrayAleaotorio(10, []);
const arr2 = geraArrayAleaotorio(20, []);
const arr3 = geraArrayAleaotorio(5, []);
const arr4 = geraArrayAleaotorio(30, []);
const arr5 = geraArrayAleaotorio(100, []);

console.log(mergeArrays([arr1, arr2, arr3, arr4, arr5]));