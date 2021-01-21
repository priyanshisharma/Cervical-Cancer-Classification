import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = ''
# If the service is authenticated, set the key or token
key = ''

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "age": 35,
            "Number of sexual partners": 1,
            "First sexual intercourse": 25.0,
            "Num of pregnancies": 0.0,
            "Smokes": 0.0,
            "Smokes (years)": 0.0,
            "Smokes (packs/year)": 0.0,
            "Hormonal Contraceptives": 0.0,
            "Hormonal Contraceptives (years)": 0.0,
            "IUD": 0.0,
            "IUD (years)": 0.0,
            "STDs": 0.0,
            "STDs (number)": 0.0,
            "STDs:condylomatosis": "yes",
            "STDs:cervical condylomatosis": "married",
            "STDs:vaginal condylomatosis": "may",
            "STDs:vulvo-perineal condylomatosis": 5099.1,
            "STDs:syphilis": 999,
            "STDs:pelvic inflammatory disease": "failure",
            "STDs:genital herpes": 1,
            "STDs:molluscum contagiosum": 0.0,
            "STDs:AIDS": 0.0,
            "STDs:HIV": 0.0,
            "STDs:Hepatitis B": 0.0,
            "STDs:HPV": 0.0,
            "STDs: Number of diagnosis": 0.0,
            "STDs: Time since first diagnosis": 0.0,
            "STDs: Time since last diagnosis": 0.0,
            "Dx:Cancer":0,
            "Dx:CIN":0,
            "Dx:HPV":0,
            "Dx":0,
          },
          {
            "age": 25,
            "Number of sexual partners": 7,
            "First sexual intercourse": 17.0,
            "Num of pregnancies": 0.0,
            "Smokes": 1.0,
            "Smokes (years)": 7.0,
            "Smokes (packs/year)": 12.0,
            "Hormonal Contraceptives": 1.0,
            "Hormonal Contraceptives (years)": 5.0,
            "IUD": 0.0,
            "IUD (years)": 0.0,
            "STDs": 0.0,
            "STDs (number)": 0.0,
            "STDs:condylomatosis": "yes",
            "STDs:cervical condylomatosis": "married",
            "STDs:vaginal condylomatosis": "may",
            "STDs:vulvo-perineal condylomatosis": 5099.1,
            "STDs:syphilis": 999,
            "STDs:pelvic inflammatory disease": "failure",
            "STDs:genital herpes": 1,
            "STDs:molluscum contagiosum": 0.0,
            "STDs:AIDS": 0.0,
            "STDs:HIV": 0.0,
            "STDs:Hepatitis B": 0.0,
            "STDs:HPV": 0.0,
            "STDs: Number of diagnosis": 0.0,
            "STDs: Time since first diagnosis": 0.0,
            "STDs: Time since last diagnosis": 0.0,
            "Dx:Cancer":0,
            "Dx:CIN":0,
            "Dx:HPV":0,
            "Dx":0,
          },
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