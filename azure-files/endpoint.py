import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://9c5d63b4-a8d8-4a1b-ba19-8936707f61e9.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'hFV4HIpIggmgprjdKxDUuXmEqRp96pOV'

# Two sets of data to score, so we get two results back
data = {"data": 
            [
                {
                    "Age": 20.0,
                    "Number of sexual partners": 2.0,
                    "First sexual intercourse": 16.0,
                    "Num of pregnancies": 2.316400580551524,
                    "Smokes": 0.0, "Smokes (years)": 0.0,
                    "Smokes (packs/year)": 0.0,
                    "Hormonal Contraceptives": 1.0,
                    "Hormonal Contraceptives (years)": 0.75,
                    "IUD": 0.0,
                    "IUD (years)": 0.0,
                    "STDs": 0.0,
                    "STDs (number)": 0.0,
                    "STDs:condylomatosis": 0.0,
                    "STDs:vaginal condylomatosis": 0.0,
                    "STDs:vulvo-perineal condylomatosis": 0.0,
                    "STDs:syphilis": 0.0,
                    "STDs:pelvic inflammatory disease": 0.0,
                    "STDs:genital herpes": 0.0,
                    "STDs:molluscum contagiosum":0.0,
                    "STDs:HIV": 0.0,
                    "STDs:Hepatitis B": 0.0,
                    "STDs:HPV": 0.0,
                    "STDs: Number of diagnosis": 0.0,
                    "Dx:Cancer": 0.0,
                    "Dx:CIN": 0.0,
                    "Dx:HPV": 0.0,
                    "Dx": 0.0,
                    "Column1": 0.0
                }, 
                {
                    "Age": 45.0,
                    "Number of sexual partners": 5.0,
                    "First sexual intercourse": 15.0,
                    "Num of pregnancies": 7.0,
                    "Smokes": 0.0,
                    "Smokes (years)": 0.0,
                    "Smokes (packs/year)": 0.0,
                    "Hormonal Contraceptives": 1.0,
                    "Hormonal Contraceptives (years)": 0.66,
                    "IUD": 0.0,
                    "IUD (years)": 0.0,
                    "STDs": 0.0,
                    "STDs (number)": 0.0,
                    "STDs:condylomatosis": 0.0,
                    "STDs:vaginal condylomatosis": 0.0,
                    "STDs:vulvo-perineal condylomatosis": 0.0,
                    "STDs:syphilis": 0.0,
                    "STDs:pelvic inflammatory disease": 0.0,
                    "STDs:genital herpes": 0.0,
                    "STDs:molluscum contagiosum": 0.0,
                    "STDs:HIV": 0.0,
                    "STDs:Hepatitis B": 0.0,
                    "STDs:HPV": 0.0,
                    "STDs: Number of diagnosis": 0.0,
                    "Dx:Cancer": 0.0,
                    "Dx:CIN": 0.0,
                    "Dx:HPV": 0.0,
                    "Dx": 0.0,
                    "Column1": 0.0
                }, 
                {
                    "Age": 41.0,
                    "Number of sexual partners": 4.0,
                    "First sexual intercourse": 21.0,
                    "Num of pregnancies": 3.0,
                    "Smokes": 0.0,
                    "Smokes (years)": 0.0,
                    "Smokes (packs/year)": 0.0,
                    "Hormonal Contraceptives": 1.0,
                    "Hormonal Contraceptives (years)": 0.25,
                    "IUD": 0.0,
                    "IUD (years)": 0.0,
                    "STDs": 0.0,
                    "STDs (number)": 0.0,
                    "STDs:condylomatosis": 0.0,
                    "STDs:vaginal condylomatosis": 0.0,
                    "STDs:vulvo-perineal condylomatosis": 0.0,
                    "STDs:syphilis": 0.0,
                    "STDs:pelvic inflammatory disease": 0.0,
                    "STDs:genital herpes": 0.0,
                    "STDs:molluscum contagiosum": 0.0,
                    "STDs:HIV": 0.0,
                    "STDs:Hepatitis B": 0.0,
                    "STDs:HPV": 0.0,
                    "STDs: Number of diagnosis": 0.0,
                    "Dx:Cancer": 0.0,
                    "Dx:CIN": 0.0,
                    "Dx:HPV": 0.0,
                    "Dx": 0.0,
                    "Column1": 0.0
                }
            ]
        }

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())