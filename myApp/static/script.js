function printSection() {
  var prtContent = document.getElementById("sectionToPrint");
  var WinPrint = window.open('', '', 'left=0,top=0,width=800,height=900,toolbar=0,scrollbars=0,status=0');
  WinPrint.document.write(prtContent.innerHTML);
  WinPrint.document.close();
  WinPrint.focus();
  WinPrint.print();
  WinPrint.close();
}

// Event listener to trigger the printing when the button is clicked
document.getElementById('printButton').addEventListener('click', printSection);

document.addEventListener('DOMContentLoaded', function () {
  var swiper = new Swiper('.swiper-container', {
      pagination: {
          el: '.swiper-pagination',
          clickable: true,
      },
  });
});