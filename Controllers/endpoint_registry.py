import Services.auth_service
import Services.livre_service

def register_routes(app):
    @app.route('/livres',methods=['POST'])
    def route_add_livre():
        return Services.livre_service.addLivre(app)


    @app.route('/livres',methods=['GET'])
    def route_get_livres():
        return Services.livre_service.getAllLivres(app)


    @app.route('/livres/{id}',methods=['GET'])
    def route_get_livre_by_id(id):
        return Services.livre_service.getLivreById(id)


    @app.route('/livres/{id}', methods=['PUT'])
    def route_update_livre(id):
        return Services.livre_service.updateLivre(app,id)


    @app.route('/livres/{id}',methods=['DELETE'])
    def route_delete_livre(id):
        return Services.livre_service.deleteLivre(app,id)


    @app.route('/login',methods=['POST'])
    def route_login():
        return Services.auth_service.login(app)