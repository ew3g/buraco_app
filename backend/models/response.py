def Response(data, code, message, error):
    return {"data": data, "code": code, "message": message, "error": error}


def AuthResponse(token, usuarioId):
    return {"token": token, "usuarioId": usuarioId}


def UserResponse(model):
    return {"nomeUsuario": model.nomeUsuario, "email": model.email, "id": model.id}


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
