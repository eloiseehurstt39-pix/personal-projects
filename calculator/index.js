// javascript

const display = document.getElementById("display");

function appendToDisplay(input){
    display.value += input; //a += b => a = a + b
} 

function clearDisplay(){
    display.value = "";
}

function calculate(){
    try{
        display.value = eval(display.value); // function that calculates numbers
    }
    catch(error){
        display.value = "Error";
    }
}