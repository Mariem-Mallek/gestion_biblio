from models import SessionLocal , Livre
from exceptions import LivreNonTrouve , DonneesInvalides , handleException
from Utils.jwt_utils import require_auth
from Utils.query_utils import livre_filtres,livre_pagination


def addLivre(app):
    req=app.current_request
    require_auth(req)
    data=req.json_body

    if not data.get('title') :
        raise DonneesInvalides("Le titre est obligatoire.")
    
    if not data.get('author') :
        raise DonneesInvalides("L'auteur est obligatoire.")
    
    session = SessionLocal()
    newLivre= Livre(
        title=data.get('title'),
        author=data.get('author'),
        year=data.get('year'),
        isbn=data.get('isbn')
    )
    session.add(newLivre)
    session.commit()
    session.refresh(newLivre)
    session.close()

    return  {'message' : 'Livre ajouté avec succés !' , 'id':newLivre.id}



def getAllLivres(app):
    req=app.current_request
    require_auth(req)

    params = req.query_params or {}

    session=SessionLocal()
    query = session.query(Livre)

    query=livre_filtres(query,params)
    query=livre_pagination(query,params)

    livres=query.all()
    session.close()
    
    return [{
                'id': l.id,
                'title': l.title,
            } for l in livres]
    


def getLivreById(id):
    session=SessionLocal()
    try:
        livre=session.query(Livre).filter(Livre.id==int(id)).first()

        if not livre :
            raise LivreNonTrouve(id)
        
        return {
            'id':livre.id,
            'title':livre.title,
            'author':livre.author,
            'year':livre.year,
            'isbn':livre.isbn
        }
    
    except Exception as e:
        return handleException(e)
    
    finally:
        session.close()




def updateLivre(app,id):
    req=app.current_request
    require_auth(req)
    data=req.json_body
    session=SessionLocal()
    livre= session.query(Livre).filter(Livre.id == int(id)).first()

    if not livre:
        raise LivreNonTrouve(livre.id)

    
    livre.title=data.get('title',livre.title)
    livre.author=data.get('author',livre.author)
    livre.year=data.get('year',livre.year)
    livre.isbn=data.get('isbn',livre.isbn)

    session.commit()
    session.refresh(livre)
    session.close()

    return{'message': 'Livre mis a jours avec succés '}



def deleteLivre(id):
    session= SessionLocal()
    livre= session.query(Livre).filter(Livre.id == int(id)).first()
    if not livre:
        raise LivreNonTrouve(livre.id)
    
    session.delete(livre)
    session.commit()
    session.close()

    return{'message': 'Livre supprimé avec succés !'}


    












