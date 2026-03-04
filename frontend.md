TERMINOLOGY: 
react js: js library that renders UI logic specific to web applications 

react: mobile apps and stuff

components: smaller chunks of ui elements for your application 

componnent func: how to create components 
    input = props = parameters 

DOM: basically a tree of all the components of a website as a tree (index being root, events page being child)

fragment = div without adding additional node in DOM 

jsx: looks like html but is secretly javascript 

state = data that changes over time 

props: parameters, but React always take it as a single object, so always wrap in {}
    ex. ButtonRenderer({param1, param2}) = ButtonRenderer(props){later on props.param1, props.param2}

hooks: special functions that allow user to access React special properties 
    - useState: hook that allows to access metadata about state of elements 
    - useEffect: hook that allows you to perform side effects 

promise: results of an asynchronous operation 
    can either be pending, fulfilled, or rejected
    can be handled with async + await/then(accept, reject)

side effects: functions outside the control of react rendering logic 
    i.e. fetch api 


CORS: CORS origin platform sharing.
    basically a browser can only talk to the server it came from. in order to surpass this, cors is there to say hey i accept requests from anyone i.e. flask server accepts requests from react js 
------
USEFUL REACT JS FUNCS 

1. useEffect(() => {}, [optional dependencies]): sync component w external system 
    upon action return stuff in {}
    which can either be nothing/a cleanup func (stops/undo something useEffect started)

    Ex of what can go in the {}: aync func 

2. functionName = async (parameters) => {await funcs}: 
    always return a promise 



------

How does react work: 
react creates a virtual dom (in memory doms) whenever you changes a node, its virtual dom detects the change accordingly in memory 






conditional logic: 

if panelState == true: # the info panel is open rn
    show gotriangleleft 
    show info panel 


button: 
    on click  
        change the state of panelState 
        change the rotation of the button 
        hide/show in stylelised way for panelState 

if panelState == false: 



work on the button logic first 
work on the panel logic second 
think about how to duplicate it for country and event later 



ok, so, reformat events so that it is common for both events and country 

then put in a


click on button 
-> expand/collapse panel 
-> change panel icon 




now: how to make react fetch data from backend 
    use load async & await custom func 

    input: id of the event into custom func 
    output: data for events to load 



preload the data before launch app  (what data) 



how to make react fetch data from an api in backend 


