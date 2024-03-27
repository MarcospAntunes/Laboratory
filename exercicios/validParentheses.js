const pares = {
    "(": ")",
    "[": "]",
    "{": "}"
}

function isValid(s) {
    if(s.length % 2 === 1) return false
    if(s[0] === ")" || s[0] === "]" || s[0] === "}") return false
    if(s[s.length - 1] === "(" || s[s.length - 1] === "[" || s[s.length - 1] === "{") return false

    let tipo = []

    for(let i=0; i < s.length; i++) {
        if(s[i] === "(" || s[i] === "[" || s[i] === "{") {
            tipo.push(s[i])
        } else if(pares[tipo.pop()] !== s[i]) {
            return false
        }
    }
    return tipo.length === 0
}

isValid("{}")
isValid("()")
isValid("()[]{}")
isValid("(]")
