/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function printSection() {
    var originalContents = document.body.innerHTML;
    var section = document.getElementById('sectionToPrint').innerHTML;
    document.body.innerHTML = section;
    window.print();
    document.body.innerHTML = originalContents;
}

// Event listener to trigger the printing when the button is clicked
document.getElementById('printButton').addEventListener('click', printSection);
