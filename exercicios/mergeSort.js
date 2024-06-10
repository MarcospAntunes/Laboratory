const geraArrayAleaotorio = require("./geraArrayAleatorio");

function mergeSort(arr) {
    if(arr.length === 1) return arr;

    const middle = Math.floor(arr.length / 2);
    const left =  arr.slice(0, middle);
    const right = arr.slice(middle, arr.length);

    const arr1 = mergeSort(left);
    const arr2 = mergeSort(right);

    arr = merge(arr1, arr2);
    
    return arr;
};

function merge(left, right) {
    let resultArray = [],
        leftIndex = 0,
        rightIndex = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] < right[rightIndex]) {
            resultArray.push(left[leftIndex]);
            leftIndex++; 
        } else {
            resultArray.push(right[rightIndex]);
            rightIndex++;
        }
    }

    return resultArray
        .concat(left.slice(leftIndex))
        .concat(right.slice(rightIndex));
}

const test1 = geraArrayAleaotorio(1, []);
const test2 = geraArrayAleaotorio(10, []);
const test3 = geraArrayAleaotorio(5, []);

console.log(mergeSort(test1));
console.log(mergeSort(test2));
console.log(mergeSort(test3));
