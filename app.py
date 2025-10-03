from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('spam_detector.pkl', 'rb'))

@app.route('/')
def home():
    # Flask automatically looks in the 'templates' folder.
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        prediction = model.predict(data)[0]
        result = "This is a Spam Email!" if prediction == 1 else "This is a Ham Email!"
        return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)

