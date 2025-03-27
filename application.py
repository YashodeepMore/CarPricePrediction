from flask import Flask,redirect,render_template,request,jsonify
import pickle
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np

application = Flask(__name__)
app = application

label = pickle.load(open('models/lable.pickle',"rb"))
rf_model = pickle.load(open('models/model.pickle',"rb"))
preprocessor = pickle.load(open('models/preprocessor.pickle',"rb"))

@app.route('/')
def index():
    return render_template("home.html")

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method =='POST':
        
        brand = request.form.get("brand")
        model = request.form.get("model")
        vehicle_age = int(request.form.get("vehicle_age"))
        km_driven = int(request.form.get("km_driven"))
        seller_type=request.form.get("seller_type")
        fuel_type=request.form.get("fuel_type")
        transmission_type=request.form.get("transmission_type")
        mileage=float(request.form.get("mileage"))
        engine=int(request.form.get("engine"))
        max_power=float(request.form.get("max_power"))
        seats=int(request.form.get("seats"))
       
        try:
            model = int(label.transform([model])[0])
            columns = ["model", "vehicle_age", "km_driven", "seller_type", "fuel_type", "transmission_type", "mileage", "engine", "max_power", "seats"]
            input_df = pd.DataFrame([[model, vehicle_age, km_driven, seller_type, fuel_type, transmission_type, mileage, engine, max_power, seats]], columns=columns)

            new_pro_data = preprocessor.transform(input_df)
            result = rf_model.predict(new_pro_data)
            return render_template('new2.html', results=round(result[0],2))
        except Exception as e:
            return render_template('new2.html', results="Error occurred: " + str(e))

        # new_pro_data = preprocessor.transform([[model,vehicle_age,km_driven,seller_type,fuel_type,transmission_type,mileage,engine,max_power,seats]])
        
        # df = pd.DataFrame(new_pro_data)
        # result = rf_model.predict(new_pro_data)

        # return render_template('new2.html',results=result[0])
    else:
        return render_template('new2.html',results=None)

if __name__=="__main__":
    app.run(debug=True)