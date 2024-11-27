from flask import Flask, render_template, request, jsonify
import functions
import arduino

app = Flask(__name__)



@app.route('/data', methods=['POST','GET'])
def recieve_data():
    formatted_data = []
    c = 0
    data = functions.get_data()
    for row in data:
        formatted_data.append(
            {
                "N_level" : row[0],
                "P_level" : row[1],
                "K_level" : row[2],
                "M_level" : row[3],
                "timestamp" : row[4]
            }
        )


        
    print(f"Recieved Data : {formatted_data}")
    print(f"This is how jsonified data looks : {jsonify(formatted_data)}")
    return jsonify(formatted_data)

@app.route('/front_page')
def front_page():
    
    return render_template("front_page.html")


if __name__ == '__main__':
    app.run(debug=True)
