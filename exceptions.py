from chalice import Response

class LivreNonTrouve(Exception):
    def __init__(self,livre_id):
        self.message=f"Livre avec ID {livre_id} est introuvable"
        self.status_code=404

class DonneesInvalides(Exception):
    def __init__(self, message):
        self.message = message
        self.status_code = 400

def handleException(error):
    if isinstance(error,LivreNonTrouve):
        return Response (
            body={"error":error.message},
            status_code=error.status_code,
            headers={"Content-Type":"application/json"}
        )
    else:
        return Response (
            body={"error": "Erreur interne du serveur"},
            status_code=500,
            headers={"Content-Type":"application/json"}
        )


