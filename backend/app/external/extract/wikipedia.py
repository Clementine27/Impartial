
import requests
from app.config import Config 
import json 



def get_history_index(country):     

    params = {
        "action": "parse", 
        "format": "json", 
        "page": country, 
        "prop": "sections", 
        "disabletoc": True 
        }
    response = requests.get(Config.WIKIPEDIA_URL, params= params, headers= Config.WIKI_HEADERS)
    
    try: 
        response.raise_for_status()
    except requests.HTTPError: 
        print("Error in parsing response for " + country)
        return None
    
    dict = response.json()
    
    with open("app/external/data/test5.json", "w") as f: 
        json.dump(dict, f)  
        
    sections = dict["parse"]["sections"]
    index = ""
    for section in sections: 
        if section["line"] == "History":
            index = int(section["index"]) 
            
    return params, index 



def get_history_text(params, index): 
    params.update({
        "section": index, 
        "prop": "wikitext"
    }) 
        
    sect_response = requests.get(Config.WIKIPEDIA_URL, params= params, headers= Config.WIKI_HEADERS)
    
    print(sect_response.url)
    try: 
        sect_response.raise_for_status()
    except requests.HTTPError: 
        print("Error in finding history section for " + params["page"])
        return None
    
    history_dict = sect_response.json()["parse"]
    
    
    with open("app/external/data/test4.json", "w") as f: 
        json.dump(history_dict, f)  
        
    return None


def get_history(country): 
    info = get_history_index(country)   
    # print(type(info)) 
    get_history_text(info[0], info[1])


# def get_sections_content(int): 
#     params = {
#         "action": "parse", 
#         "format": "json", 
#         "prop": "section",
#         "page" 
#         "section": int, 
#         "disabletoc": True 
#         }
    
#     response = requests.get(Config.WIKIPEDIA_URL, params= params, headers= Config.WIKI_HEADERS)
    
#     dict = response.json()

#     with open("app/external/data/test3.json", "w") as f: 
#         json.dump(dict, f)
    
#     # return None
    
    
# def get_history(country): 
#     index = get_sections(country)
    
#     get_sections_content(index)



