import splunklib.client as client
import json
from jinja2 import Environment, FileSystemLoader
import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Chemin du fichier de suivi
SENT_ALERTS_FILE = 'alerts_sent.json'

# Charger les alertes déjà envoyées
if os.path.exists(SENT_ALERTS_FILE):
    with open(SENT_ALERTS_FILE, 'r') as f:
        sent_alerts = json.load(f)
else:
    sent_alerts = []

# Connexion à Splunk
service = client.connect(
    host='172.10.80.102',
    port='8089',
    scheme='https',
    username='joshua.guyot',
    password='akn3RkNr'
)

# Requête de recherche Splunk
search_query = 'search index=alerts'
search_results = service.jobs.oneshot(search_query, output_mode='json')
print(search_results.read())
jsout = json.loads(search_results.read())

# Filtrer les alertes non envoyées
new_alerts = [alert for alert in jsout['results'] if alert['_cd'] not in sent_alerts]

# Si des alertes sont nouvelles, générer le rapport et l'envoyer
if new_alerts:
    # Charger le template Jinja depuis un fichier
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('alert_template.jinja')
    formatted_report = template.render(jsout={'results': new_alerts}, datetime=datetime)

    # Écriture du rapport dans un fichier HTML
    with open('rapport_alertes_splunk', 'w', encoding='utf-8') as file:
        file.write(formatted_report)

    # Mettre à jour la liste des alertes envoyées
    sent_alerts.extend(alert['_cd'] for alert in new_alerts)
    with open(SENT_ALERTS_FILE, 'w') as f:
        json.dump(sent_alerts, f)

# Déconnexion de Splunk
service.logout()
