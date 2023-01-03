# Disease Prediction Flask

This is a appliaction which uses flask for http requests and in this app Machine Learning is implemented using disease prediction data model to predict disease according to symptoms provided.

## Features

- It provides precautions and treatment towards a certain disease
- It uses REST API's

## Requirements

| Language | Version |
| ------ | ------ |
| Python | 3.7.0 |

## Dependencies

|Plugins | Version |
| ------ | ------ |
| numpy | 1.21.1 |
| flask_restx | 1.0.3 |
| Flask-Cors | 3.0.10 |
| joblib | 1.2.0 |
| pipreqs | 0.4.11 |
| python-dotenv | 0.21.0 |

## Installation

Go  inside disease-prediction-flask/ folder to create a virtual environment, and activate it

```sh
cd disease-prediction-flask/
py -m venv venv
.\venv\Scripts\activate
```

Now install dependencies...

```sh
pip install -r requirements.txt
```
Requirements.txt contains all the packages required to run this project.
If you add additional package use below command to add them to Requirements.txt

```sh
pip freeze > requirements.txt
```

## To Run Server

Create .env file inside disease-prediction-flask/ and add following
```sh
FLASK_APP = app.py
FLASK_ENV = development
FLASK_RUN_PORT = 5000
FLASK_DEBUG=1
```

Then launch the server using :

```sh
flask run
```

## Usage

```javascript
    fetch('/api/prediction',
      {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(response => {
        console.log("Response Came",response)
      });
```

Data sent in post request is present at bottom of this page. 

## Deployment

| Plugin | Version |
| ------ | ------ |
| waitress | 2.1.2 |

To run locally on production

```sh
 waitress-serve app:app   
 #OR
 waitress-serve --listen=*:8000 app:app
```

For Deployment

```sh
 #Build Command
 pip install -r requirements.txt

 # Start Command
 waitress-serve --port=$PORT app:app
 #As PORT should be dynamic
```

## Data 
This data has symtoms which passed to the request.

```javascript
    data = {
  "itching": true,
  "skin_rash": false,
  "nodal_skin_eruptions": false,
  "continuous_sneezing": false,
  "shivering": true,
  "chills": false,
  "joint_pain": false,
  "stomach_pain": false,
  "acidity": true,
  "ulcers_on_tongue": false,
  "muscle_wasting": false,
  "vomiting": false,
  "burning_micturition": false,
  "spotting_ urination": false,
  "fatigue": false,
  "weight_gain": false,
  "anxiety": false,
  "cold_hands_and_feets": false,
  "mood_swings": false,
  "weight_loss": false,
  "restlessness": false,
  "lethargy": false,
  "patches_in_throat": false,
  "irregular_sugar_level": false,
  "cough": false,
  "high_fever": false,
  "sunken_eyes": false,
  "breathlessness": false,
  "sweating": false,
  "dehydration": false,
  "indigestion": false,
  "headache": false,
  "yellowish_skin": false,
  "dark_urine": false,
  "nausea": false,
  "loss_of_appetite": false,
  "pain_behind_the_eyes": false,
  "back_pain": false,
  "constipation": false,
  "abdominal_pain": false,
  "diarrhoea": false,
  "mild_fever": false,
  "yellow_urine": false,
  "yellowing_of_eyes": false,
  "acute_liver_failure": false,
  "fluid_overload": false,
  "swelling_of_stomach": false,
  "swelled_lymph_nodes": false,
  "malaise": false,
  "blurred_and_distorted_vision": false,
  "phlegm": false,
  "throat_irritation": false,
  "redness_of_eyes": false,
  "sinus_pressure": false,
  "runny_nose": false,
  "congestion": false,
  "chest_pain": false,
  "weakness_in_limbs": false,
  "fast_heart_rate": false,
  "painDuringBowel_movements": false,
  "pain_in_anal_region": false,
  "bloody_stool": false,
  "irritation_in_anus": false,
  "neck_pain": false,
  "dizziness": false,
  "cramps": false,
  "bruising": false,
  "obesity": false,
  "swollen_legs": false,
  "swollen_blood_vessels": false,
  "puffy_face_and_eyes": false,
  "enlarged_thyroid": false,
  "brittle_nails": false,
  "swollen_extremeties": false,
  "excessive_hunger": false,
  "extra_marital_contacts": false,
  "drying_and_tingling_lips": false,
  "slurred_speech": false,
  "knee_pain": false,
  "hip_joint_pain": false,
  "muscle_weakness": false,
  "stiff_neck": false,
  "swelling_joints": false,
  "movement_stiffness": false,
  "spinning_movements": false,
  "loss_of_balance": false,
  "unsteadiness": false,
  "weakness_of_one_body_side": false,
  "loss_of_smell": false,
  "bladder_discomfort": false,
  "foul_smell_of urine": false,
  "continuous_feel_of_urine": false,
  "passage_of_gases": false,
  "internal_itching": false,
  "toxic_look_(typhos)": false,
  "depression": false,
  "irritability": false,
  "muscle_pain": false,
  "altered_sensorium": false,
  "red_spots_over_body": false,
  "belly_pain": false,
  "abnormal_menstruation": false,
  "dischromic _patches": false,
  "watering_from_eyes": false,
  "increased_appetite": false,
  "polyuria": false,
  "family_history": false,
  "mucoid_sputum": false,
  "rusty_sputum": false,
  "lack_of_concentration": false,
  "visual_disturbances": false,
  "receiving_blood_transfusion": false,
  "receiving_unsterile_injections": false,
  "coma": false,
  "stomach_bleeding": false,
  "distention_of_abdomen": false,
  "historyOfAlcoholConsumption": false,
  "Fluid_overload": false,
  "blood_in_sputum": false,
  "prominent_veins_on_calf": false,
  "palpitations": false,
  "painful_walking": false,
  "pus_filled_pimples": false,
  "blackheads": false,
  "scurring": false,
  "skin_peeling": false,
  "silver_like_dusting": false,
  "small_dents_in_nails": false,
  "inflammatory_nails": false,
  "blister": false,
  "red_sore_around_nose": false,
  "yellow_crust_ooze": false
}
```
