#---------------------------------------------------------------------------
# get_profiles.py
#
# Desc  :  Reads output of get_people.py and get_companies.py
#          and uses Google search to build a list of LinkedIn profile URLs
# Author:  Janet Prumachuk
# Date  :  Nov 2015
#---------------------------------------------------------------------------
import sys, requests, re 
from google import search

def build_search_strings(people, companies):
    ss  = open('links.txt', 'w') 

    cdict  = {}
    fields = []
    for c in companies:
        fields = c.split("|")
        if fields[0] != "id":
            key = fields[0]
            key = int(key)
            val = fields[1]
            cdict[key] = val

    results = []
    fields  = []
    for p in people:
        fields = p.split("|")
        if fields[0] != "company_id":
            company_id   = fields[0]
            company_id   = int(company_id)
            company_name = cdict[company_id]
            company_name = company_name.replace(" ","+")
            company_name = re.sub(r"[^\x00-\x7f]+"," ", company_name)
            person_id    = fields[1]
            person_name  = fields[2]
            person_name  = person_name.replace(" ","+")
            record = "linkedin+" + person_name + "+" + company_name + "\n"
            links = []
            record = fields[1] + "|" + fields[2] 
            for url in search(record, lang='en', stop=1):
                 if "www.linkedin.com/pub/" in url:
                     record = record + "|" + url + "\n"
                     ss.write(record)
                     break
                 elif "www.linkedin.com/in/" in url:
                     record = record + "|" + url + "\n"
                     ss.write(record)
                     break
                 elif "linkedin.com" in url:
                     record = record + "|" + url + "\n"
                     ss.write(record)
                     break
                              
    ss.close()

def main():
    people_file  = open(sys.argv[1])
    company_file = open(sys.argv[2])

    build_search_strings(people_file, company_file)

    people_file.close()
    company_file.close()

if __name__ == '__main__':
    main()
