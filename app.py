from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Set to store unique visitor IPs
visitor_ips = set()

@app.route('/')
def index():
    visitor_ip = request.remote_addr  # Get the visitor's IP address
    visitor_ips.add(visitor_ip)  # Add the IP to the set of visitors
    return render_template('index.html')  # Render your HTML template

@app.route('/visitor_count')
def visitor_count():
    # Return the number of unique visitors as JSON
    return jsonify({'current_visitors': len(visitor_ips)})

if __name__ == '__main__':
    app.run(debug=True)
