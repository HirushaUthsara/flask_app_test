from flask import Flask, render_template
import gradio as gr
import numpy as np
import pandas as pd
import folium
from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

# Replace the placeholder with your Atlas connection string
username = "hirusha"
password = "hiru@mongodb"
cluster_name = "cluster0"
uri = f"mongodb+srv://{quote_plus(username)}:{quote_plus(password)}@{cluster_name}.dlrxsa6.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)



# # Load your machine learning model and data
# # Replace this with your own model and data loading code
# def load_model():
#     # Load your ML model here
#     pass

# def load_data():
#     # Load your data here
#     # Replace this with your own data loading code
#     data = pd.read_csv("historical_data.csv")
#     return data

# def predict_precipitation(year, month):
#     # Your machine learning model prediction code here
#     # Replace this with your own prediction code using the loaded model and data
#     prediction = np.random.uniform(low=0, high=100, size=(1,))  # Dummy example
#     return prediction[0]

# Create the Flask app
app = Flask(__name__)

# # Load the model and data
# model = load_model()
# data = load_data()

# Define the Gradio interface
year_slider = gr.inputs.Slider(minimum=1970, maximum=2005, default=2000, step=1, label="Year")
month_slider = gr.inputs.Slider(minimum=1, maximum=12, default=6, step=1, label="Month")

# def predict_and_map(year, month):
#     # Make the prediction using the selected year and month
#     prediction = predict_precipitation(year, month)

#     # Create a map with the predicted precipitation
#     location = (8.0260, 79.8471)  # Replace with the actual coordinates of your location
#     m = folium.Map(location=location, zoom_start=10)
#     folium.CircleMarker(
#         location=location,
#         radius=10,
#         color='blue',
#         fill=True,
#         fill_color='blue',
#         fill_opacity=prediction / 100,  # Scale opacity based on prediction value
#     ).add_to(m)

#     return m

def predict_and_map(year,month):
    pass
output_text = gr.outputs.Textbox(label="Output Text")

interface = gr.Interface(fn=predict_and_map, inputs=[year_slider, month_slider],outputs=output_text)

# Define the Flask routes
@app.route('/')
def index():
    m = folium.Map()
    m.save("index.html")
    interface.launch(share=True)
    return render_template('index.html')

# @app.route('/gradio')
# def gradio():
#     return interface.launch()

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
