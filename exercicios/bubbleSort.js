const geraArrayAleaotorio = require("./geraArrayAleatorio");

function bubbleSort(arr) {

    for(let i = 0; i < arr.length; i++) {
        let temp;
        for(let j = 0; j < arr.length; j++) {
            if(arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            };
        };
    };

    return arr;
}


const array = geraArrayAleaotorio(10, []);

console.log(bubbleSort(array));