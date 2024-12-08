from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model and label encoder
model = joblib.load('crop_recommendation_model.pkl')
encoder = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    """Process user input and provide crop recommendation."""
    try:
        # Parse form data
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Prepare input for the model
        input_data = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
        prediction = model.predict(input_data)
        recommended_crop = encoder.inverse_transform(prediction)[0]

        return jsonify({'success': True, 'crop': recommended_crop})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
