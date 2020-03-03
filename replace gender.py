import requests
import pandas as pd

# Set the URL you want to webscrape from
MAIN_URL = ""
MALE_HTML = ''
FEMALE_HTML = ''

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

URL = ""
PARAMS = {'advanced': 1,
          'namo': 'name'}

def unid(name):
    if LAST_DATA['name'] == name:
        return LAST_DATA["gender"]
    else:
        print("Fetching Data...")
        PARAMS['namo'] = name
        LAST_DATA["name"] = name
        session = requests.Session()
        r = session.post(url=URL, data=PARAMS)
        m_c = r.text.count('class="M"')
        f_c = r.text.count('class="F"')
        if m_c > f_c:
            LAST_DATA["gender"] = 3
            return 3
        elif m_c < f_c:
            LAST_DATA["gender"] = 4
            return 4
        else:
            LAST_DATA["gender"] = 5
            return 5

# Read one line at at time. Change chunksize to process more lines at a time. 
data = pd.read_csv('finala.csv', chunksize=1)
write_header = True  # Needed to get header for first chunk

COUNTER = 0
c_2 = 0
for line in data:
    COUNTER = COUNTER + 1

    if line.iloc[0]['Gender, M=0, F=1'] == 3:
        line['Gender, M=0, F=1'] = 0
    elif line.iloc[0]['Gender, M=0, F=1'] == 4:
        line['Gender, M=0, F=1'] = 1

    # line['Gender, M=0, F=1'] = gender(line.iloc[0]['First.Name'])

    # # Save the file to a csv, appending each new chunk you process. mode='a' means append.
    line.to_csv('finala2.csv', mode='a', header=write_header, index=False)
    write_header = False