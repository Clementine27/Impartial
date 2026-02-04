

// object stuffInside 
const stuffInside = document.querySelector(".parent-node"); 

const firstChild = stuffInside.firstElementChild; 

console.log(firstChild); 

// create a new tag <div>
const newStuff = document.createElement("div"); 


// specify css styling from js
// newStuff.style.color = "blue"; 
// newStuff.style.cssText = "color: blue, background: white"
newStuff.setAttribute("style", "color: blue, background: white"); 
newStuff.textContent = "js edited text"; 
newStuff.classList.add("huh"); 

stuffInside.appendChild(newStuff); 



// interractivity 

const firstButton = document.querySelector("#firstButton"); 
firstButton.addEventListener("click", ()=> {
    alert("good girl"); 
}); 


// event type being passed as an argument 



const secondButtons = document.querySelectorAll(".secondButton"); 

secondButtons.forEach(   
    (button) => {
        button.addEventListener("click", function(e) {
    console.log(e.target);
    }
)

})

const specialOne = document.querySelector(".secondButton#new"); 
specialOne.addEventListener("click", function(e){
    e.target.style.background = "blue"; 
})

