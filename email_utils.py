import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_templates import generate_order_confirmation_email, generate_status_update_email

class EmailService:
    def __init__(self):
        self.config = {
            'host': 'smtp.gmail.com',
            'port': 587,
            'address': 'mobitelm583@gmail.com',
            'password': 'hnykzexmchqpdvbs',
            'from_name': 'Mini Webshop',
            'admin_email': 'mobitelm583@gmail.com'
        }
    
    def _send_email(self, to_email, subject, html_content):
        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = f"{self.config['from_name']} <{self.config['address']}>"
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Create plain text version as fallback
            text_content = f"""
            {subject}
            
            Ovo je HTML email. Vaš email klijent možda ne podržava HTML poruke.
            """
            
            msg.attach(MIMEText(text_content, 'plain'))
            msg.attach(MIMEText(html_content, 'html'))
            
            with smtplib.SMTP(self.config['host'], self.config['port']) as server:
                server.starttls()
                server.login(self.config['address'], self.config['password'])
                server.send_message(msg)
            
            print(f"Email uspješno poslan na {to_email}")
            return True
        except Exception as e:
            print(f"Greška pri slanju emaila: {str(e)}")
            return False
    
    def send_order_confirmation(self, order):
        subject = f"📦 Potvrda narudžbe #{order['id']}"
        html_content = generate_order_confirmation_email(order)
        return self._send_email(self.config['admin_email'], subject, html_content)
    
    def send_status_update(self, order):
        if not order['customer'].get('email'):
            print("Kupac nema email adresu, preskačem slanje obavijesti")
            return False
        
        subject = f"🔄 Status narudžbe #{order['id']}"
        html_content = generate_status_update_email(order)
        return self._send_email(order['customer']['email'], subject, html_content)

# Globalna instanca za cijelu aplikaciju
email_service = EmailService()