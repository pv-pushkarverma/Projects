let submit=document.getElementById('submit')
let bmi;
submit.addEventListener('click',(event)=>{
    event.preventDefault();

    let height=document.getElementById('height').value;
    height=height/100;//centimeter to meter

    let weight=document.getElementById('weight').value;
    bmi=weight/(height*height);

    bmi=bmi.toFixed(2);
    let string;
    let result=document.getElementById('result');
    result.innerHTML=`Your BMI is ${bmi}`;

    if(isNaN(bmi))
        string='Enter valid Height and Weight.';

    else if(bmi<18.6)
        string='You are Underweight.';
    else if(bmi<=24.9)
        string='You are in Normal Range.';
    else if(bmi>24.9)
        string='You are Overweight.';
    //result.innerHTML+=string;
    alert(string);
});