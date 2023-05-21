import api from './axiosConfig';

export const getUsuarios = async () => {
    const response = await api.get('/usuarios');
    return response.data;
};

export const getUsuarioById = async (id) => {
    const response = await api.get(`/usuario/${id}`)
        .catch(function (error) {
            console.log(error)
        });
    return response.data
};

export const createUsuario = async (data) => {
    const response = await api.post("/usuario", data)
        .then(function (res) {
            return res;
        })
        .catch(function (error) {
            return error.response;
        });
    return response;
};

export const updateUsuario = async (id, data) => {
    const response = await api.put(`/usuarios/${id}`, data);
    return response.data;
};

export const deleteUsuario = async (id) => {
    const response = await api.delete(`/usuarios/${id}`);
    return response.data;
};

export const trocarSenha = async (id, data) => {
    const response = await api.post(`/usuario/nova-senha/${id}`, data)
        .then(function (res) {
            return true;
        })
        .catch(function (error) {
            return false;
        });
    return response;
};

export const esqueciSenha = async (data) => {
    console.log(data)
    const response = await api.post("/usuario/esqueci-senha", data)
        .then(function (res) {
            return res;
        })
        .catch(function (error) {
            return error.response;
        });
    return response;
};