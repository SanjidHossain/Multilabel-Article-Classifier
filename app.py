from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    label_list = []
    is_empty_result = True  # Flag to indicate if the result is empty

    if request.method == "POST":
        output = predict_label(request.form['text'])[0]
        confident_list = output['confidences']
        for elem in confident_list:
            if elem['confidence'] >= 0.5:
                is_empty_result = False # Update flag if result is found
                label_list.append({
                    'label': elem['label'],
                    'confidence': int(elem['confidence'] * 100)
                })

    return render_template('index.html', label_list=label_list, is_empty_result=is_empty_result)

def predict_label(input_text):
    response = requests.post("https://sanjid-news-classifier.hf.space/run/predict", json={
        "data": [
            input_text
        ]
    }).json()
    data = response["data"]
    return data

if __name__ == "__main__":
    app.run(debug=True)
