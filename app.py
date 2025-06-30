from chalice import Chalice

app = Chalice(app_name='gestion_biblio')

# Charger les routes
from routes import register_routes
register_routes(app)



