from bs4 import BeautifulSoup
import re, requests, pickle

field_names = ['Name', 'Ball Control', 'Dribbling', 'Marking', 'Slide Tackle', 'Stand Tackle', 'Aggression', 'Reactions', 'Att. Position', 'Interceptions', 'Vision', 'Composure', 'Crossing', 'Short Pass', 'Long Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint Speed', 'Agility', 'Jumping', 'Heading', 'Shot Power', 'Finishing', 'Long Shots', 'Curve', 'FK Acc.', 'Penalties', 'Volleys', 'Overall Rating']

def getAllPlayerLinks(page_number) :
    page = requests.get("https://www.fifaindex.com/players/?page="+str(page_number)+"&gender=0&position=25&order=desc")
    soup = BeautifulSoup(page.content, 'html.parser')
    links = []
    for s in soup.find_all('tr') :
        link = re.findall("href=\"/player/[0-9]+/[^/]+/\"", str(s))
        if link != [] :
            links.append(link[0][6:][:-1])
    return links

for page_number in range(1, 100, 1) :
    file = open("/Users/RHyde23/Desktop/FIFAML/rows.dat","rb")
    rows = pickle.load(file)
    print(page_number)
    links = getAllPlayerLinks(page_number)
    for li in links :
        try :
            page2 = requests.get("https://www.fifaindex.com"+li)
        except :
            continue
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        csv_dictionary = {}
        add = True
        overall = None
        for s2 in soup2.find_all('p') :
            s2 = str(s2)
            if " was born on" in s2 :
                csv_dictionary["Name"] = s2.split(" was born on")[0][3:]
                overall = int(s2.split("His overall rating in FIFA 22 is ")[1][:2])
            s2 = s2[12:]
            cat = s2.split(" <")[0]
            if cat == "Preferred Positions" :
                if s2 != "Preferred Positions <span class=\"float-right\"><a class=\"link-position\" href=\"/players/?position=25\" title=\"ST\"><span class=\"badge badge-dark position st\">ST</span></a></span></p>":
                    add = False
                    break
            if cat in field_names :
                value = int(s2.split(">")[-4].split("<")[0])
                csv_dictionary[cat] = value
        if add :
            csv_dictionary["Overall Rating"] = overall
            if list(csv_dictionary.keys()) == field_names :
                rows.append(csv_dictionary)
                print(csv_dictionary["Name"])
            else :
                print("FAILED >>>>>>>>>>> ", csv_dictionary["Name"])
    print()
    file2 = open("/Users/RHyde23/Desktop/FIFAML/rows.dat","wb")
    pickle.dump(rows, file2)    
    file2.close()
    
