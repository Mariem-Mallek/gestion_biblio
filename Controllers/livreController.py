from models import SessionLocal , Livre
from Auth.jwt_utils import require_auth


def addLivre(app):
    req=app.current_request
    require_auth(req)
    data=req.json_body

    # Validation des données
    if not data.get('title') :
        return {'error': 'Titre est obligatoire !'}
    
    if not data.get('author') :
        return {'error': 'Auteur est obligatoire !'}
    
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

    params=req.query_params 
    limit= int(params.get("limit", 10))
    author = params.get("author")

    session=SessionLocal()
    query = session.query(Livre)

    if author:
        query = query.filter(Livre.author.ilike(f"%{author}%"))

    livres=query.limit(limit).all()

    res=[{'id':l.id , 'title':l.title, 'author':l.author,'year':l.year, 'isbn':l.isbn} for l in livres]
    session.close()
    return res



def getLivreById(id):
    session=SessionLocal()
    try:
        livre=session.query(Livre).filter(Livre.id==int(id)).first()

        if not livre :
            return {'Erreur' : 'Livre introuvable !'},404
        
        return {
            'id':livre.id,
            'title':livre.title,
            'author':livre.author,
            'year':livre.year,
            'isbn':livre.isbn
        }
    
    except Exception as e:
        return {'error': str(e)}, 400
    
    finally:
        session.close()




def updateLivre(app,id):
    req=app.current_request
    require_auth(req)
    data=req.json_body
    session=SessionLocal()
    livre= session.query(Livre).filter(Livre.id == int(id)).first()

    if not livre:
        session.close()
        return{'Erreur' : 'Livre introuvable !'}
    
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
        session.close()
        return{'Erreur' : 'Livre introuvable'}
    
    session.delete(livre)
    session.commit()
    session.close()

    return{'message': 'Livre supprimé avec succés !'}


    












