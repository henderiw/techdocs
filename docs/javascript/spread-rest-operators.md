# javascript spread - rest operator

## spread

clone an array/object and potentially extend it

const newArray = [...oldArray, 1, 2]
const newObject = {...oldObject, newProp:5}

## rest

used to merge a list of function arguments into an array

function sortArgs(...args) {
    return arg.sort()
}