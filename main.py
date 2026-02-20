from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/teamlist')
def teamlist():sto
    return render_template('teamlist.html')

@app.route('/submit-registration', methods=['POST'])
def submit_registration():
    data = request.get_json()
    
    # Team mapping based on grade and section
    team_map = {
        "7-Emerald": "Blue Bears",
        "7-Ruby": "Red Bulldogs",
        "7-Sapphire": "Red Bulldogs",
        "7-Topaz": "Green Hornets",
        "8-Emerald": "Blue Bears",
        "8-Ruby": "Red Bulldogs",
        "8-Sapphire": "Yellow Tigers",
        "8-Topaz": "Green Hornets",
        "9-Emerald": "Blue Bears",
        "9-Ruby": "Red Bulldogs",
        "9-Sapphire": "Yellow Tigers",
        "9-Topaz": "Green Hornets",
        "10-Emerald": "Blue Bears",
        "10-Ruby": "Red Bulldogs",
        "10-Sapphire": "Yellow Tigers",
        "10-Topaz": "Green Hornets",
        "11-Luna": "Blue Bears",
        "11-Amorsolo": "Red Bulldogs",
        "10-Tinio": "Yellow Tigers",
        "12-Jose": "Green Hornets"
    }
    
    grade = data.get('grade')
    section = data.get('section')
    key = f"{grade}-{section}"
    team = team_map.get(key, "Blue Bears")
    
    registration_data = {
        'online_registration': data.get('onlineRegistration'),
        'medical_clearance': data.get('medicalClearance'),
        'grade': grade,
        'section': section,
        'team': team
    }
    
    # Here you can save to database or file
    print(f"Registration submitted: {registration_data}")
    
    return jsonify({
        'status': 'success',
        'message': f'Congratulations! You are part of the {team} !!',
        'team': team
    })

@app.route('/team-checker', methods=['GET'])
def team_checker():
    return jsonify({'message': 'Team Checker feature coming soon'})

@app.route('/players', methods=['GET'])
def players():
    return jsonify({'message': 'Players feature coming soon'})

if __name__ == '__main__':
    app.run(debug=True)