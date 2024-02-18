let random=parseInt(Math.random()*100+1);
let play=true;
let AllGuess=new Array();
let moves=10;
const p = document.createElement('p');
p.classList.add('button');
p.innerHTML = `<h2 id="newGame">Start new Game</h2>`;

document.getElementById('moves').innerHTML='Moves Remaining : '+moves;
let submit=document.getElementById('submit-button');

submit.addEventListener('click',e=>{
    if(moves===0){
        submit.setAttribute('disabled','');
        endGame();
    }

    if(play){
    let guess=parseInt(document.getElementById('num-input').value);

    let checkguess=check_guess(guess);
    if(checkguess){

        AllGuess.push(guess);
        console.log(random);
        console.log(AllGuess);
        document.getElementById('guessed-num').innerHTML=AllGuess;
        moves--;
        document.getElementById('moves').innerHTML='Moves Remaining : '+moves;

        if(guess === random){
            document.getElementById('message').innerHTML=
            'Congratulations You Guessed the number correctly';
            endGame();
        }
        else if(guess>random){
            document.getElementById('message').innerHTML=
            'Number is Smaller';
        }
        else{
            document.getElementById('message').innerHTML=
            'Number is Greater';
        }
        
    }  
    }
    else{
        document.getElementById('message').innerHTML=
        'Game Over';
    }   
})

function check_guess(guess){
    if(isNaN(guess)){
        alert('Enter a valid number');
        return false;
    }
    if(guess<0){
        alert('Enter number greater than 0');
        return false;
    }
    if(guess>100){
        alert('Enter number less than 101');
        return false;
    }
    return true;
}

function endGame(){
    play=false;
    document.body.appendChild(p);

    p.addEventListener('click',e=>{
        startnew();
    })
}

function startnew(){
    document.getElementById('num-input').value='';
    random=parseInt(Math.random()*100+1);
    document.body.removeChild(p);
    AllGuess=[];
    moves=10;
    document.getElementById('message').innerHTML='';
    document.getElementById('guessed-num').innerHTML=AllGuess;
    document.getElementById('moves').innerHTML='Moves Remaining : '+moves;
    play=true;
}