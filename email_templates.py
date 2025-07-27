from datetime import datetime

def generate_gradient_header():
    return """
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px 0;
        text-align: center;
        border-radius: 8px 8px 0 0;
    ">
        <h1 style="
            color: white;
            margin: 0;
            font-size: 28px;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        ">Mini Webshop</h1>
    </div>
    """

def generate_order_confirmation_email(order):
    items_html = "".join([
        f"""
        <tr>
            <td style="padding: 12px 15px; border-bottom: 1px solid #e0e0e0;">
                {item['name']}
            </td>
            <td style="padding: 12px 15px; border-bottom: 1px solid #e0e0e0; text-align: center;">
                {item['quantity']}
            </td>
            <td style="padding: 12px 15px; border-bottom: 1px solid #e0e0e0; text-align: right;">
                {item['price']:.2f} KM
            </td>
            <td style="padding: 12px 15px; border-bottom: 1px solid #e0e0e0; text-align: right;">
                {(item['price'] * item['quantity']):.2f} KM
            </td>
        </tr>
        """ for item in order['items']
    ])
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nova narudžba #{order['id']}</title>
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    </head>
    <body style="font-family: 'Open Sans', Arial, sans-serif; background-color: #f5f7fa; margin: 0; padding: 0;">
        <div style="max-width: 600px; margin: 20px auto; background: white; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            {generate_gradient_header()}
            
            <div style="padding: 30px;">
                <div style="margin-bottom: 30px;">
                    <h2 style="color: #2d3748; margin-top: 0;">Hvala na vašoj narudžbi!</h2>
                    <p style="color: #4a5568;">Broj vaše narudžbe: <strong>#{order['id']}</strong></p>
                    <p style="color: #4a5568;">Datum: {order['created_at']}</p>
                </div>
                
                <div style="background-color: #f8fafc; border-radius: 6px; padding: 20px; margin-bottom: 30px;">
                    <h3 style="color: #2d3748; margin-top: 0; margin-bottom: 15px;">Detalji narudžbe</h3>
                    
                    <table style="width: 100%; border-collapse: collapse;">
                        <thead>
                            <tr>
                                <th style="padding: 12px 15px; text-align: left; border-bottom: 2px solid #e2e8f0;">Proizvod</th>
                                <th style="padding: 12px 15px; text-align: center; border-bottom: 2px solid #e2e8f0;">Količina</th>
                                <th style="padding: 12px 15px; text-align: right; border-bottom: 2px solid #e2e8f0;">Cijena</th>
                                <th style="padding: 12px 15px; text-align: right; border-bottom: 2px solid #e2e8f0;">Ukupno</th>
                            </tr>
                        </thead>
                        <tbody>
                            {items_html}
                            <tr>
                                <td colspan="3" style="padding: 12px 15px; text-align: right; font-weight: bold; border-top: 2px solid #e2e8f0;">Ukupno:</td>
                                <td style="padding: 12px 15px; text-align: right; font-weight: bold; border-top: 2px solid #e2e8f0;">
                                    {sum(item['price'] * item['quantity'] for item in order['items']):.2f} KM
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                
                <div style="margin-bottom: 30px;">
                    <h3 style="color: #2d3748; margin-top: 0; margin-bottom: 15px;">Podaci o kupcu</h3>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                        <div>
                            <p style="margin: 5px 0; color: #4a5568;"><strong>Ime:</strong> {order['customer']['first_name']}</p>
                            <p style="margin: 5px 0; color: #4a5568;"><strong>Prezime:</strong> {order['customer']['last_name']}</p>
                        </div>
                        <div>
                            <p style="margin: 5px 0; color: #4a5568;"><strong>Telefon:</strong> {order['customer']['phone']}</p>
                            <p style="margin: 5px 0; color: #4a5568;"><strong>Email:</strong> {order['customer'].get('email', 'Nije naveden')}</p>
                        </div>
                    </div>
                    <p style="margin: 10px 0 0; color: #4a5568;"><strong>Adresa:</strong> {order['customer']['address']}</p>
                </div>
                
                <div style="text-align: center; padding-top: 20px; border-top: 1px solid #edf2f7;">
                    <p style="color: #718096; margin-bottom: 20px;">Hvala vam što kupujete kod nas!</p>
                    <a href="https://vaswebshop.com" style="
                        display: inline-block;
                        background-color: #667eea;
                        color: white;
                        text-decoration: none;
                        padding: 12px 24px;
                        border-radius: 4px;
                        font-weight: 600;
                        margin-bottom: 20px;
                    ">Posjetite našu web stranicu</a>
                    <p style="color: #a0aec0; font-size: 12px; margin-bottom: 0;">
                        © {datetime.now().year} Mini Webshop. Sva prava pridržana.
                    </p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

def generate_status_update_email(order):
    status_info = {
        'Pending': {'color': '#f6ad55', 'text': 'Vaša narudžba je primljena i u obradi.'},
        'Accepted': {'color': '#68d391', 'text': 'Vaša narudžba je prihvaćena i priprema se za isporuku.'},
        'Completed': {'color': '#68d391', 'text': 'Vaša narudžba je uspješno isporučena.'},
        'Rejected': {'color': '#fc8181', 'text': 'Nažalost, vaša narudžba nije mogla biti procesuirana.'}
    }
    
    status_data = status_info.get(order['status'], {'color': '#a0aec0', 'text': ''})
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ažuriranje statusa narudžbe #{order['id']}</title>
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    </head>
    <body style="font-family: 'Open Sans', Arial, sans-serif; background-color: #f5f7fa; margin: 0; padding: 0;">
        <div style="max-width: 600px; margin: 20px auto; background: white; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            {generate_gradient_header()}
            
            <div style="padding: 30px;">
                <div style="text-align: center; margin-bottom: 30px;">
                    <div style="
                        background-color: {status_data['color']}20;
                        border-left: 4px solid {status_data['color']};
                        padding: 15px;
                        margin-bottom: 20px;
                        text-align: left;
                    ">
                        <h3 style="color: #2d3748; margin-top: 0;">Status narudžbe #{order['id']}</h3>
                        <p style="color: #4a5568; margin-bottom: 0;">{status_data['text']}</p>
                    </div>
                    
                    <div style="
                        display: inline-block;
                        background-color: {status_data['color']};
                        color: white;
                        padding: 8px 16px;
                        border-radius: 20px;
                        font-weight: 600;
                        font-size: 14px;
                        margin-bottom: 20px;
                    ">
                        {order['status']}
                    </div>
                </div>
                
                <div style="margin-bottom: 30px;">
                    <h3 style="color: #2d3748; margin-top: 0; margin-bottom: 15px;">Sažetak narudžbe</h3>
                    
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                        <div>
                            <p style="margin: 5px 0; color: #4a5568;"><strong>Datum:</strong> {order['created_at']}</p>
                        </div>
                        <div>
                            <p style="margin: 5px 0; color: #4a5568;"><strong>Ukupno:</strong> {sum(item['price'] * item['quantity'] for item in order['items']):.2f} KM</p>
                        </div>
                    </div>
                    
                    <p style="color: #4a5568; margin-bottom: 0;">
                        <strong>Adresa dostave:</strong> {order['customer']['address']}
                    </p>
                </div>
                
                <div style="text-align: center; padding-top: 20px; border-top: 1px solid #edf2f7;">
                    <p style="color: #718096; margin-bottom: 20px;">Za sva pitanja, slobodno nam se obratite.</p>
                    <a href="mailto:podrska@vaswebshop.com" style="
                        display: inline-block;
                        background-color: #667eea;
                        color: white;
                        text-decoration: none;
                        padding: 12px 24px;
                        border-radius: 4px;
                        font-weight: 600;
                        margin-bottom: 20px;
                    ">Kontaktirajte podršku</a>
                    <p style="color: #a0aec0; font-size: 12px; margin-bottom: 0;">
                        © {datetime.now().year} Mini Webshop. Sva prava pridržana.
                    </p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """