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
    const response = await api.post('/usuarios', data);
    return response.data;
};

export const updateUsuario = async (id, data) => {
    const response = await api.put(`/usuarios/${id}`, data);
    return response.data;
};

export const deleteUsuario = async (id) => {
    const response = await api.delete(`/usuarios/${id}`);
    return response.data;
};