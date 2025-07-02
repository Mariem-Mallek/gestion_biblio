import Services.auth_service
import Services.livre_service

LIVRES_ROUTE = '/livres'
LOGIN_ROUTE = '/login'

def register_routes(app):
    @app.route(LIVRES_ROUTE,methods=['POST'])
    def route_add_livre():
        return Services.livre_service.addLivre(app)


    @app.route(LIVRES_ROUTE,methods=['GET'])
    def route_get_livres():
        return Services.livre_service.getAllLivres(app)


    @app.route(LIVRES_ROUTE+'/{id}',methods=['GET'])
    def route_get_livre_by_id(id):
        return Services.livre_service.getLivreById(id)


    @app.route(LIVRES_ROUTE+'/{id}', methods=['PUT'])
    def route_update_livre(id):
        return Services.livre_service.updateLivre(app,id)


    @app.route(LIVRES_ROUTE+'/{id}',methods=['DELETE'])
    def route_delete_livre(id):
        return Services.livre_service.deleteLivre(app,id)


    @app.route(LOGIN_ROUTE,methods=['POST'])
    def route_login():
        return Services.auth_service.login(app)