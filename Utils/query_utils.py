from models import Livre

def livre_filtres(query,params):
    if not params:
        return query
    
    author= params.get("author")
    if author :
        query = query.filter(Livre.author.ilike(f"%{author}%"))

    title = params.get("title")
    if title:
        query = query.filter(Livre.title.ilike(f"%{title}%"))

    return query


def livre_pagination(query, params):
    try:
        limit=int(params.get("limit",10))
        if limit<=0:
            limit=10
    except(ValueError,TypeError):
        limit=10

    return query.limit(limit)

