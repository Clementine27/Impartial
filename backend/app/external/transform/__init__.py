# map json fields to event models only 

def transform_britanica(wiki_data): 
    """
    read json files and then reconcile with model and return runtime 
    models for load 
    """
    return {
        "title": wiki_data["title"],
        "description": wiki_data["snippet"],
        "year": (wiki_data["snippet"]),
        "source": "Wikipedia"
    }

def transform_wiki(wiki_data): 
    """
    read json files and then reconcile with model and return runtime 
    models for load 
    """
    return {
        "title": wiki_data["title"],
        "description": wiki_data["snippet"],
        "year": (wiki_data["snippet"]),
        "source": "Wikipedia"
    }

def run_all_transforms(): 
    for file in "data/": 
        if file.__contains__("wiki"): 
            transform_wiki(file)
        
        