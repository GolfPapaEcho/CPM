#takes review file and spits out json
import docx
from simplify_docx import simplify
import json

file_name = input("Please input file name with type: ")
# read in a document 
your_doc = docx.Document("/home/michael/CPM/Reviews/" + file_name)

# coerce to JSON using the standard options
your_doc_as_json = simplify(your_doc)
json_data = json.dumps(your_doc_as_json, indent=4)
json_path = 'output.json'
with open(json_path, 'w') as json_file:
    json_file.write(json_data)
with open('/home/michael/CPM/yourCMS/output.json', 'r') as file:
    data = file.read()

parsed = json.loads(data)
print(json.dumps(parsed) + "\n")