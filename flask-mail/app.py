from flask import Flask, render_template
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail = Mail(app)

# Use environment variables to store sensitive information
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # Mailtrap's TLS port
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True  # Use TLS for secure communication
app.config['MAIL_USE_SSL'] = False  # Disable SSL


@app.route('/send_email')
def send_email():
    sender = os.environ.get('MAIL_USERNAME')
    msg = Message('Hello from Flask', sender=sender,
                  recipients=['briankmbuguak@gmail.com'])
    msg.body = 'This is an email sent from Flask using Flask-Mail'
    mail.send(msg)
    return 'Email sent!'


if __name__ == '__main__':
    app.run(debug=True)
