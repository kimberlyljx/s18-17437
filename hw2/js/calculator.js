
var OpTypes = {
  PLUS: '+',
  MINUS: '-',
  DIVIDE: '/',
  TIMES: '*',
  EQUALS: '='
};

var newValue = 0;
var prevValue = 0;
var prevOp = OpTypes.PLUS;
var lastWasOp = false;

function resetState() {
    newValue = 0;
    prevValue = 0;
    prevOp = OpTypes.PLUS;
    lastWasOp = false;
}

function updateDisplay(value) {
    var display   = document.getElementById("display");
    display.innerHTML = value;
}

function digitPress(digit) {
    if (lastWasOp) {
        newValue = digit;
    } else {
        newValue = newValue * 10 + digit;
    }
    updateDisplay(newValue);
    lastWasOp = false;
}

function isValidOp(operator) {
    switch (operator) {
        case OpTypes.PLUS:
            return true;
            break;
        case OpTypes.MINUS:
            return true;
            break;
        case OpTypes.DIVIDE:
            return true;
            break;
        case OpTypes.TIMES:
            return true;
            break;
        case OpTypes.EQUALS:
            return true;
            break;
        default:
            return false;
            break;
    }
}

function updatePrevOp(newOp) {
    if (isValidOp(newOp)) {
        prevOp = newOp;
    }
    lastWasOp = true;
}

function evaluate() {
    switch (prevOp) {
        case OpTypes.PLUS:
            prevValue = newValue + prevValue;
            break;
        case OpTypes.MINUS:
            prevValue = prevValue - newValue;
            break;
        case OpTypes.DIVIDE:
            if (newValue == 0) {
                alert("Cannot divide by Zero");
                resetState();
            } else {
                prevValue = Math.floor(prevValue / newValue);
            }
            break;
        case OpTypes.TIMES:
            prevValue = newValue * prevValue;
            break;
        default:
            break;
    }
}

function operatorPress(operator) {
    if (lastWasOp) {
        updatePrevOp(operator);
        return;
    }
    evaluate();
    updateDisplay(prevValue);
    prevOp = operator;
    newValue = 0;
    lastWasOp = true;

    if (operator == OpTypes.EQUALS) {
        resetState();
    }
}