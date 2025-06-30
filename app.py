from chalice import Chalice

app = Chalice(app_name='gestion_biblio')

from routes import addLivre, getAllLivres, getLivreById, updateLivre , deleteLivre


@app.route('/livres/addLivre',methods=['POST'])
def route_add_livre():
    return addLivre(app)


@app.route('/livres/getAll',methods=['GET'])
def route_get_livres():
    return getAllLivres()


@app.route('/livres/getLivre/{id}',methods=['GET'])
def route_get_livre_by_id(id):
    return getLivreById(id)


@app.route('/livres/updateLivre/{id}', methods=['PUT'])
def route_update_livre(id):
    return updateLivre(app,id)


@app.route('/livres/deleteLivre/{id}',methods=['DELETE'])
def route_delete_livre(id):
    return deleteLivre(id)




