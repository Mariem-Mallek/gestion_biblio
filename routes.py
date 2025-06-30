from Controllers.livreController import addLivre, getAllLivres, getLivreById, updateLivre , deleteLivre 
from Controllers.authController import login 


def register_routes(app):
    @app.route('/livres/addLivre',methods=['POST'])
    def route_add_livre():
        return addLivre(app)


    @app.route('/livres/getAll',methods=['GET'])
    def route_get_livres():
        return getAllLivres(app)


    @app.route('/livres/getLivre/{id}',methods=['GET'])
    def route_get_livre_by_id(id):
        return getLivreById(id)


    @app.route('/livres/updateLivre/{id}', methods=['PUT'])
    def route_update_livre(id):
        return updateLivre(app,id)


    @app.route('/livres/deleteLivre/{id}',methods=['DELETE'])
    def route_delete_livre(id):
        return deleteLivre(id)


    @app.route('/login',methods=['POST'])
    def route_login():
        return login(app)