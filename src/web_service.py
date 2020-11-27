import csv
from flask import Flask, jsonify

app = Flask(__name__,static_url_path="")

@app.route('/', methods=['GET'])
def convert_csv_to_json():
    path = '../data/employees.csv'
    with open (path, 'r') as file:
        reader = csv.reader(file)
        data_line = list()
        for line in reader:
            data_line.append(line)
        data = [dict(zip(data_line[0],line)) for line in data_line]
        data.pop(0)
        ans = jsonify(data)
        return ans

if __name__== '__main__':
    app.run(debug=True)