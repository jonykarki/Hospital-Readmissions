import requests
import pandas as pd

# Set the URL you want to webscrape from


LAST_DATA = {
    "name": "test",
    "gender": "0"
}

def gender(name):
    GENDER_VALUE = "0"
    if (LAST_DATA['name'] == name):
        print("Repear: ", name)
        return LAST_DATA["gender"]
    else:
        print("Current: ", name)

        req_url = MAIN_URL.format(name)

        # Connect to the URL
        response = requests.get(req_url)
        if MALE_HTML in response.text:
            GENDER_VALUE = "0"
        elif FEMALE_HTML in response.text:
            GENDER_VALUE = "1"
        else:
            GENDER_VALUE = "2"
        LAST_DATA["name"] = name
        LAST_DATA["gender"] = GENDER_VALUE
        return GENDER_VALUE

# Read one line at at time. Change chunksize to process more lines at a time. 
data = pd.read_csv('resulto.csv', chunksize=1)
write_header = True  # Needed to get header for first chunk

COUNTER = 0
for line in data:
    COUNTER = COUNTER + 1
    print("Currently at ", COUNTER)
    line['Gender, M=0, F=1'] = gender(line.iloc[0]['First.Name'])

    # Save the file to a csv, appending each new chunk you process. mode='a' means append.
    line.to_csv('final.csv', mode='a', header=write_header, index=False)
    write_header = False