import json
import urllib.request

image_links = json.load(open("image_links.json"))
attribute_labels = json.load(open("attribute_labels.json"))
mvc_info = json.load(open("mvc_info.json"))

MAX_ATTEMPT = 5

for i in range(len(image_links)):
    for j in range(MAX_ATTEMPT):
        try:
            link = image_links[i]['image_url_4x']
            if i % 10 == 0:
                print(str(i) + ":   " + link)
            urllib.request.urlretrieve(link, "data/MVC/images." + str(i) + ".jpg")
            break
        except Exception as e:
            print("Error: " + str(i) + " " + link + " " + str(type(e)))
            
