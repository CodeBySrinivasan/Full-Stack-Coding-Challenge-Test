from flask import Flask, request, jsonify, render_template
import pandas as pd
from secret_santa import SecretSantaManager

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_files():
    employees_file = request.files['employeesFile']
    previous_year_file = request.files.get('previousYearFile')

    # Reading the Excel files using pandas
    employees_df = pd.read_excel(employees_file)
    previous_df = pd.read_excel(previous_year_file) if previous_year_file else None

    # Convert the DataFrames to lists of dictionaries (or appropriate data structures)
    employees = [{'Employee_Name': row['Employee_Name'], 'Employee_EmailID': row['Employee_EmailID']} for _, row in employees_df.iterrows()]
    
    previous_assignments = {}
    if previous_df is not None:
        previous_assignments = {row['Employee_Name']: row['Secret_Child_Name'] for _, row in previous_df.iterrows()}

    # Run the Secret Santa assignment logic
    santa_manager = SecretSantaManager(employees, previous_assignments)
    santa_manager.assign_secret_children()

    # Prepare response --------------------------------
    response = []
    for employee in santa_manager.employees:
        response.append({
            'Employee_Name': employee.name,
            'Employee_EmailID': employee.email,
            'Secret_Child_Name': employee.secret_child.name,
            'Secret_Child_EmailID': employee.secret_child.email
        })
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
