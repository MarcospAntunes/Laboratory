function romanToInt(s) {
    const romanNumberDic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    let result = 0

    for(let i=0; i < s.length; i++) {
        const p1 = romanNumberDic[s[i]]
        const p2 = romanNumberDic[s[i + 1]]

        if(p1 < p2) {
            result += p2 - p1
            i++
        } else {
            result += p1
        }
    }
    return result
}

romanToInt("III")
romanToInt("IV")
romanToInt("V")
romanToInt("XII")
romanToInt("XX")
