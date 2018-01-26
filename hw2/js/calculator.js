var newValue = 0;
var prevValue = 0;

var OpTypes = {
  PLUS,
  MINUS,
  DIVIDE,
  TIMES,
  EQUALS
};

function digitPress(digit) {
    var display   = document.getElementById("display");
        
    newValue = newValue * 10 + digit;
    display.innerHTML = newValue;
}