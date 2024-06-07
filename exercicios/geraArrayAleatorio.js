function geraArrayAleaotorio(length, arr) {
    while(arr.length < length) {
        if(arr.length  === length) break;
        if(!arr[Math.floor(Math.random() * 1000)])arr.push(Math.floor(Math.random() * 1000));
    }
    return arr;
};

module.exports = geraArrayAleaotorio;