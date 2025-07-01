from chalice import Chalice

app = Chalice(app_name='gestion_biblio')

# Chargement des routes
from Controllers.routes import register_routes
register_routes(app)



