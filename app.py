from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = round(num1 + num2)
        elif operation == 'subtract':
            result = round(num1 - num2)
        elif operation == 'multiply':
            result = round(num1 * num2)
        elif operation == 'divide':
            result = round((num1 / num2),2) if num2 != 0 else "Error: Division by zero"
        else:
            result = "Invalid Operation"
        
        return render_template('calculator.html', result=result)
    except Exception as e:
        return render_template('calculator.html', result=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
