import requests 
url = 'http://127.0.0.1:5000/results'
r = requests.post(url,json=
                  {"ml_num": "N3613770",
                   "property_type": "A.",
                   "br": 4.0,
                   "br_plus": 0,
                   "br_final": 4.0,
                   "bath_tot": 3,
                   "taxes": 0.0,
                   "lp_dol": 406400,
                   "yr_built": "New",
                   "gar_type": "Attached",
                   "garage": 1.0,
                   "topHighschoolScore": 0.0,
                   "topBelowHighschoolScore": 5.0,
                   "geo_latitude": 44.316996,
                   "geo_longitude": -79.857459,
                   "lot_frontfeet": 30.02,
                   "lot_depthfeet": 117.29,
                   "lot_size": 3521.0458,
                   "sqft_numeric": 1750,
                   "id_community": 232,
                   "id_municipality": 10103,
                   "date_start": "2016-09-25 00:00:00",
                   "date_end": "2016-10-03 00:00:00"
                   })  
print(r.json())