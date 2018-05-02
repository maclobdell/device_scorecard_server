from flask import Flask, render_template, request, redirect
app = Flask(__name__)

email_addresses = []

@app.route('/')
def hello_world():
    author = "Mbed Enabled"
    name = "FRDM-K99G"
    flash_val = "checked"
    rtc_val = ""
    trng_val = "checked"
    return render_template('index.html', author=author, name=name, flash_val=flash_val, rtc_val=rtc_val, trng_val=trng_val)

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    #print("The email address is '" + email + "'")
    email_addresses.append(email)
    print(email_addresses) 
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

@app.route('/add.html')
def add_stuff():
    return render_template('add.html')

#NEED TO RECEIVE JSON, THEN AUTOMATICALLY GENERATE THE TEXT BOXES, ETC

#NEED TO MAKE SURE TO RUN TESTS ON LOTS OF DEVICES PLUGGED IN IN PARALLEL.


if __name__ == "__main__":
    app.run()
