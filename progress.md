- finish writing to dict for country 

- finsih writing to dict for events 

- allow sql to update the new schema 

write new api for events 

# validate apis 
# CORS Configuration
# validate with Postman




front end may want these things when interracting with the database for country 

- search bar 
- map 




test out how front end is running 
test out if flask 

2h30-8h30 = 6h 

1. subtasks 
- buy face cleanser 
- moisturiser 


n
2. restructure the backend & make sure you can run both front and back and connect (30 mins) 
- figure out how things are working first of all 
- what needs to change to adhere to the mega tutorial 


3. CORS
4. API design again 
5. frontend input validation 
6. error handling
--- 
7. design frontend 


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


restful APIs -> test 

# validate apis 
# validate with Postman

- pagination? 
- external connection 


by 5am 

then I do LASER 


Select * 
from Event 
Where childEventIDs is not included in (select child_event from events_table)