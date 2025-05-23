import json, os, getpass, socket
from datetime import datetime
from PyQt5.QtCore import QObject, pyqtSlot
from smail.src.connection.command_line_mail import send_email

# This class is used for notification to authorized people
# Whenever user ignore warning from connection to phishing web page
# And fill their information in
class NotificationFillTextToPhishing(QObject):
    @pyqtSlot(str)
    def receiveData(self, received_data):
        # Parse received JSON data to invidial data
        parsing_data = json.loads(received_data)
        input_text = parsing_data.get('value')
        connected_phishing_url = parsing_data.get('url')
        computer_username = getpass.getuser()
        computer_devicename = socket.gethostname()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Customize result 
        send_data = f'''*****Data received from sWEB when user filled text in phishing website*****
        - Device name: {computer_devicename}
        - User name: {computer_username}
        - Website: {connected_phishing_url}
        - Time: {current_time}
        - Filled text: {input_text}
        '''
        '''
        # Send received data to authorized people
        send_phishing_option = _dataProvider.get_sweb_configuration().sendPhishingWarning
        if send_phishing_option:
            self.send_email(send_data)
        else:
            return
        '''

     
    def send_email(self, message_to_receiver):
        # Load needed configuration from sweb_config in sconf for sending notification to authorized people
        ##receiver_mail = _dataProvider.get_smail_configuration().emailContacts[0]
        receiver_mail = "test@gmail.com"

        try:
            # Load the command line mail script
            command_line_mail_script = os.path.join(os.path.dirname(__file__), 'command_line_mail.py')
            with open(command_line_mail_script) as f:
                exec(f.read())
            print("Email sent successfully!!!")
        except Exception as excep:
            print(f"Error sending email: {excep}")
        
  