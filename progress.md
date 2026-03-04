* hook front end with back end 
* fix external api 
* deploy 
* more front end pages (use events as template for both events and countries later)


-----
External APIs game plan: 
- make wiki works 
    - how to query stuff under a specific subsection 
    - <h2 id=\"History\">History</h2>



input: wiki api 
    process: 
        get the index of history session of the country's page 
        
        from that index, parse and get all the text

        from text, get events 

        from events output to json file 

output: 
- json files of all events on that countries page so transform can go through it and map to Event schema 


write events 
    for country in  countries txt, 
        response = get_events(country)  
        response.jsonify to path .data(wiki_events) 

ohhhh, so when a dir has an init file 
its treated as a module/package rather 
than just a dir, so think of it as an extension like pandas


hgrugharkhgw
--------------------
- finish writing to dict for country 

- finsih writing to dict for events 

---------------------

flask run -> create_app() triggered --> initialise app, db n migration system -> register model, error, routes, api blueprints (because usually, the elements are registered to the app, but the app hasnt been created yet, so we are using bp as a placeholder)

flask is a pure api responder to front end react requests 

i.e. user send a request that forces front end to call an api to the backend. flask checks to see if the required route is defined. if not, it returns an error and flask tries to see if you have defined that yet. if yes, then input the error object and flask returns an api request to frontend with a json body and a code for the header. we import modules after creating bp to avoid circular import. 

404: server works but cant find the resource 
500: server found the requested route but couldnt finish responding to frontend call. server prob

we prepends api infront of all api calls so that we know that it is a call to interract with the backend 

the data lives in the app.db as a binary file. the models file just outline what the tables look like and then when you upgrade via alchemy, it actually executes the commands according to the sql script outlined in migration and make changes depending on what you do to it. 




-- 
primary join: sync column of choice with left column in assc. table 
secondary join: sync column of choice with right column in assc. table 




----
[START HERE]


Done by 12 --> frontend around 2 
Set up the dashboard 

- external connection () 
    - wiki 
    - britanica 


the country entity ill enter manually 

- frontend 
    - config 
    - header template 
    - map page components
    - events page components 
    - timeline config 
    - countries page components

- bias control  
    - list of trusted resources 
    - script of scoring 
- deploy: Netlify 
(by 12am)

testing: 
- check if count_extract works by printing 
db.Country
- check if wikipedia works by seeing if it populated data/ with json files/countries 


Future iterations: 
- more countries 
- live update for more recent events 
- search via summary 
- search that support acronyms and mispellings 
- webscraping pipeline that ingests more sources
- phone support 
- timeline stretches 
- pagination
- Avoid duplicates
- more robust error handling
- frontend bug: the transition of opening the info pane after closing have words appearing too fast 

competitor: https://timeline.oldera.org/timeline/
- different ui design for different purposes 
    - this ones for fun 
        - zoom in to months, who gives a shit 
        - 1 source 
    - mine solves a real problem: 
        - starts with me being a stem major having to finish 
        my college requirements 
        - a lot of readings and researches required for paper assignemnts if i still want an A 
        - but i dont have time for that and usually do it the day before dl 
        - this website is supposed to facilitate getting that grasp of a background info required to quickly whisk up an paper 
- ui kinda ass 