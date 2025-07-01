from models import SessionLocal , Livre
from Utils.jwt_utils import require_auth
import exceptions
import Utils.query_utils
import messages


def addLivre(app):
    req=app.current_request
    require_auth(req)
    data=req.json_body

    if not data.get('title') :
        raise exceptions.DonneesInvalides(messages.TITRE_OBLIGATOIRE)
    
    if not data.get('author') :
        raise exceptions.DonneesInvalides(messages.AUTEUR_OBLIGATOIRE)
    
    champs_livre = [c.name for c in Livre.__table__.columns if c.name != 'id']
    livre_data = {champ: data.get(champ) for champ in champs_livre}
    
    session = SessionLocal()

    try:
        newLivre= Livre(**livre_data)
        session.add(newLivre)
        session.commit()
        session.refresh(newLivre)
        return {'message': messages.LIVRE_AJOUTE}
    
    except Exception as e:
        return exceptions.handleException(e)

    finally:
        session.close()



def getAllLivres(app):
    req=app.current_request
    require_auth(req)

    params = req.query_params or {}

    session=SessionLocal()
    query = session.query(Livre)

    query=Utils.query_utils.livre_filtres(query,params)
    query=Utils.query_utils.livre_pagination(query,params)

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
            raise exceptions.LivreNonTrouve(id)
        
        champs_livre = {k: v for k, v in vars(livre).items() if not k.startswith('_')}
        return champs_livre
        
    
    except Exception as e:
        return exceptions.handleException(e)
    
    finally:
        session.close()




def updateLivre(app,id):
    req=app.current_request
    require_auth(req)
    data=req.json_body
    session=SessionLocal()
    livre= session.query(Livre).filter(Livre.id == int(id)).first()

    if not livre:
        raise exceptions.LivreNonTrouve(livre.id)

    
    livre.title=data.get('title',livre.title)
    livre.author=data.get('author',livre.author)
    livre.year=data.get('year',livre.year)
    livre.isbn=data.get('isbn',livre.isbn)

    session.commit()
    session.refresh(livre)
    session.close()

    return {'message': messages.LIVRE_MIS_A_JOUR}




def deleteLivre(app,id):
    require_auth(app.current_request)
    session= SessionLocal()
    livre= session.query(Livre).filter(Livre.id == int(id)).first()
    if not livre:
        raise exceptions.LivreNonTrouve(id)
    
    session.delete(livre)
    session.commit()
    session.close()

    return{'message': messages.LIVRE_SUPPRIME}


    












