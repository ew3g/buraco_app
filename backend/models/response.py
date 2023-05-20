def Response(data, code, message, error):
    return {"data": data, "code": code, "message": message, "error": error}


def AuthResponse(token, usuarioId):
    return {"token": token, "usuarioId": usuarioId}


def UserResponse(model):
    return {"nomeUsuario": model.nomeUsuario, "email": model.email, "id": model.id}

def TamanhoBuracoResponse(model):
    return {
        "id": model.id,
        "nome": model.nome,
        "cor": model.cor
    }
    
def TamanhoBuracoListResponse(list):
    response = []
    for tamanhoBuraco in list:
        response.append(TamanhoBuracoResponse(tamanhoBuraco))
    return response
    
def BuracoResponse(model):
    return {
        "latitude": model.latitude,
        "longitude": model.longitude,
        "votos": model.votos,
        "id": model.id,
        "tamanho": model.tamanhoBuraco.nome,
        "cor": model.tamanhoBuraco.cor,
    }


def BuracoListResponse(list):
    response = []
    for buraco in list:
        response.append(BuracoResponse(buraco))
    return response
