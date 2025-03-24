from flask import Flask, request, render_template, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load voter data from CSV
voter_data = pd.read_csv('voters.csv')

# Display actual column names for debugging
print("Actual Columns in CSV:", voter_data.columns)

# Strip whitespace from column names
voter_data.columns = voter_data.columns.str.strip()

current_count = 0
MAX_CAPACITY = 5  # Maximum booth capacity

@app.route('/')
def home():
    return render_template('index.html', current_count=current_count, max_capacity=MAX_CAPACITY)

@app.route('/verify', methods=['POST'])
def verify():
    global current_count
    voter_id = request.form['voter_id'].strip()  # Strip whitespace
    
    # Identify the actual column names for Voter ID, Name, and Eligibility
    voter_id_col = [col for col in voter_data.columns if 'Voter_ID' in col or 'ID' in col][0]
    name_col = [col for col in voter_data.columns if 'Name' in col][0]
    eligible_col = [col for col in voter_data.columns if 'Eligible' in col][0]

    # Check if voter ID exists
    voter = voter_data[voter_data[voter_id_col].astype(str) == voter_id]

    if voter.empty:
        return "Invalid Voter ID. Please try again."

    # Get voter name and eligibility
    name = voter.iloc[0][name_col]
    eligibility = voter.iloc[0][eligible_col].strip().lower()

    if eligibility == "no":
        return f"Sorry, {name}! You are not eligible to vote."

    if current_count >= MAX_CAPACITY:
        return render_template('crowded.html', name=name)

    # Only increment count if verification is successful
    current_count += 1
    return render_template('verification.html', name=name, current_count=current_count, max_capacity=MAX_CAPACITY)

@app.route('/leave')
def leave():
    global current_count
    if current_count > 0:
        current_count -= 1
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
