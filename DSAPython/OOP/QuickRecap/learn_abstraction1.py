# Abstraction
# Reduce complexity by hiding unecessary details

class EmailService:

    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self):
        print("Authenticating....")

    def send_email(self):
        self._connect()
        self._authenticate
        print("Sending email....")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server")

email = EmailService()
email.send_email()

# Manual implementation without abstraction
# email = EmailService()
# email.connect()
# email.authenticate()
# email.send_email()
# email.disconnect()