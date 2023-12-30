let clock=document.getElementById('clock');
setInterval(() => {
        console.log("Set interval is called");
        let time=new Date().toLocaleTimeString();
        clock.innerHTML=time;
},1000)
let date=new Date().toLocaleDateString();
document.getElementById('date').innerHTML=date;