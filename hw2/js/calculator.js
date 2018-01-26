
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

function evaluate() {
    switch (prevOp) {
        case OpTypes.PLUS:
            prevValue = newValue + prevValue;
            break;

        case OpTypes.MINUS:
            prevValue = prevValue - newValue;
            break;

        case OpTypes.DIVIDE:
            prevValue = prevValue / newValue;
            break;

        case OpTypes.TIMES:
            prevValue = newValue * prevValue;
            break;
        case OpTypes.EQUALS:
            break;
        default:
            break;
    }
}

function operatorPress(operator) {
    evaluate();
    updateDisplay(prevValue);
    prevOp = operator;
    newValue = 0;
    lastWasOp = true;
}