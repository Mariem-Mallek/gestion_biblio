from chalice import Chalice

app = Chalice(app_name='gestion_biblio')

# Chargement des routes
from Controllers.livre_controller import register_routes
register_routes(app)



