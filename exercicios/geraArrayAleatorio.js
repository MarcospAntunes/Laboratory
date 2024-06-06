function geraArrayAleaotorio(length, arr) {
    for(let i = 0; i < length; i++) {
        arr.push(Math.floor(Math.random() * 1000));
    }


    return arr;
};

module.exports = geraArrayAleaotorio;