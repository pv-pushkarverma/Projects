let body=document.querySelector('body');
let buttons=document.querySelectorAll('button');

console.log(buttons);
buttons.forEach(function (button){
    button.addEventListener('click',function(e){
        console.log(e);
        body.style.backgroundColor=e.target.style.backgroundColor;
    })
})