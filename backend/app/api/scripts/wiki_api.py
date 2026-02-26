import wikipediaapi
import request


page_py = wiki_wiki.page('Python_(programming_language)')
print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True

print("Page - Title: %s" % page_py.title)
# Page - Title: Python (programming language)

print("Page - Summary: %s" % page_py.summary[0:60])
# Page - Summary: Python is a widely used high-level programming language for


section_history = page_py.section_by_title('History')
print("%s - %s" % (section_history.title, section_history.text[0:40]))

# History - Python was conceived in the late 1980s b


# Read API docs

# Make requests

# Parse JSON

# Map fields

# Insert into DB

# Link relationships

# Avoid duplicates

# Test endpoints