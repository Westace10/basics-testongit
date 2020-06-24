import json

a_dictionary = {"APX-45CV": ['yomi', 'daji', +2349988497766]}

with open("vehiclereg.json", "r+") as file:
    data = json.load(file)
    data.update(a_dictionary)
    file.seek(0)
    json.dump(data, file)


