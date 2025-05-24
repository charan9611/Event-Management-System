from flask import Flask ,render_template ,jsonify,request ,session,redirect,url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash ,check_password_hash
from flask_cors import CORS

app=Flask(__name__)
app.secret_key = 'ckvk@#samreen' 
mysql=MySQL(app)
CORS(app)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='newrootpassword'
app.config['MYSQL_DB']='demo'

#main routes
@app.route('/')
def home():
    return render_template('user/index.html')

@app.route('/register')
def register():
    return render_template('user/register.html')

@app.route('/login')
def login():
    return render_template('user/login.html')

@app.route('/about')
def about():
    return render_template('user/about2.html')

@app.route('/contact')
def contact():
    return render_template('user/contact3.html')

@app.route('/services')
def services():
    return render_template('user/s2.html')

#services routes

@app.route('/services/wedding')
def wedding():
    return render_template('user/w2.html')

@app.route('/services/stage_event')
def stage_event():
    return render_template('user/stage_event.html')

@app.route('/services/social_event')
def social_event():
    return render_template('user/social_events.html')

@app.route('/services/house_warming')
def house_warming():
    return render_template('user/house_warming.html')

@app.route('/services/concert')
def concert():
    return render_template('user/concert.html')

@app.route('/services/college_events')
def college_events():
    return render_template('user/college_events.html')

@app.route('/services/anniversary')
def anniversary():
    return render_template('user/anniversary.html')

@app.route('/services/baby_shower')
def baby_shower():
    return render_template('user/baby_showers.html')

@app.route('/services/birthday')
def birthday():
    return render_template('user/birthday.html')

#booking route

@app.route('/services/booking')
def booking():
    if 'id' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in
    return render_template('user/booking.html')



@app.route('/Authlogin', methods=['POST'])
def authlogin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, user, password FROM user WHERE email = %s", (email,))
    user_data = cur.fetchone()
    cur.close()

    if user_data:
        id, user, stored_hashed_password = user_data
        
        if check_password_hash(stored_hashed_password, password):
            session['id'] = id
            session['user'] = user
            session['email'] = email
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Incorrect password'}), 401
    else:
        return jsonify({'message': 'Email not found'}), 404



@app.route('/services/booking/confirm', methods=['POST'])
def confirm_booking():
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO booking (event_type, event_date, venue, guests, name, email)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        data['event_type'],
        data['event_date'],
        data['venue'],
        data['guests'],
        data['name'],
        data['email']
    ))
    mysql.connection.commit()
    booking_id = cur.lastrowid  # Get the auto-incremented booking ID
    cur.close()

    return jsonify({"message": "Booking successful", "booking_id": booking_id})  # ✅ Return it


@app.route('/booking/confirmation/<int:booking_id>')
def booking_confirmation(booking_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM booking WHERE id = %s", (booking_id,))
    booking = cur.fetchone()
    cur.close()

    if booking:
        return render_template('user/confirmationPage.html', booking=booking)
    else:
        return "Booking not found", 404


@app.route('/user', methods=['POST'])
def postuser():
    data = request.json
    hashed_password = generate_password_hash(data['password'])  # Secure password storage

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user (user, email, phone_number, address, password) VALUES (%s, %s, %s, %s, %s)",
                (data['user'], data['email'], data['phone_number'], data['address'], hashed_password))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "User added successfully"})

@app.route('/logout')
def logout():
    session.clear()  # Clear all session data
    return redirect(url_for('home')) 


@app.route('/contact_info',methods=['POST'])
def contact_info():
    data = request.json
    cur =mysql.connection.cursor()
    cur.execute("INSERT INTO contact (name, number, email, message) VALUES (%s, %s, %s, %s)",
                (data['name'], data['number'], data['email'], data['message']))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "contact information submitted, our Team reach you soon..  thank you!! "})


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='127.0.0.1', port=5000)