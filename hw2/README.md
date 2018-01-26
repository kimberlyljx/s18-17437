# Homework 2

This homework is the second in a series of three homeworks in which you will build calculator
applications. In this homework, you will implement the calculator functions using JavaScript running
client-side in the web browser. 

## Specifications

The following **required** functionality is completed:

* [X] The calculator will use the front end that you wrote for the previous homework.
* [X] The number displayed at all times is a single integer value. This value is initially zero (0)… unless the user attempts to divide by zero, in which case you should reset the state and display an error message using a JavaScript alert.
* [X] The calculator does integer math (e.g. 9 ÷ 4 = 2).
* [X] No operator precedence. Do the operations in the order they are encountered.

The following **optional** features are implemented:

## Requirements

Your submission must also follow these requirements:

* [X] Your submission must follow all of the requirements specified in the last homework assignment.
* [X] You may not use any external libraries (e.g. jQuery, Bootstrap, etc.).
* [X] You may not use the JavaScript eval() function in the implementation of your calculator.
* [] Your calculator must be able to support numbers up to ±1,000,000. We will not test numbers
beyond that range, so you don’t have to worry about overflow.
* [] Your JavaScript may not crash at any user input—there must not be any errors reported by the
browser JavaScript console. If two (or more) operation buttons are clicked without a digit in between, you must not
crash. The computation for this is up to you.
* [X] All of your JavaScript functions must be defined in a file called calculator.js. Minimize the
amount of JavaScript written directly in your HTML file.

## Implementation
● An internal “new value”, “previous value”, and “previous operation” are kept

● Reset State: “new value” and “previous value” are zero, and “previous operation” would be “+”.

● When a digit is pressed, “new value” is updated accordingly (multiply by 10 and add digit) and then display “new value”.

● When an operation is clicked (+, -, ×, ÷, or =), use the “previous value”, “previous operation” and
“new value” to do the computation and get a “result” to display. Update as follows:

    ○ “Previous value” ← “result”
    
    ○ “Previous operation” ← operation clicked
    
    ○ “New value” ← 0

● After an operation button is clicked, the display will be replaced by the next digit that is clicked.

● Hitting '=' displays the computed value and also sets calculator to reset state

● Hitting a non-equal operator more than once, updates "previous operation" to the last non-equal operator

● No support fo entering in negative numbers, but it is possible to use the negative numbers resulting from previous operations.

## Submisssion

Your submission should be turned in via Git in a directory called hw2 and should consist of an HTML file
called calculator.html, a JavaScript file called calculator.js, and associated assets (CSS andimages).

## References
- [Shadows](https://www.w3schools.com/css/css3_shadows.asp)

## License

    Copyright [2018] [KIMBERLY LIM JINXIA]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.