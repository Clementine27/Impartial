TERMINOLOGY: 

components: smaller chunks of ui elements for your application 

componnent func: how to create components 
    input = props = parameters 

DOM: basically a tree of all the components of a website as a tree (index being root, events page being child)

fragment = div without adding additional node in DOM 

jsx: looks like html but is secretly javascript 

state = datat that changes over time 

props: property of parent -> child class that is called by the parent class 

hooks: special functions that allow user to access React special properties 
    - useState: hook that allows to access metadata about state of elements 

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