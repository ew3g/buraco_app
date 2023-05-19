import api from './axiosConfig';

export const auth = async (email, password) => {
    const request = {
        email: email,
        senha: password
    }
    const response = await api.post('/auth', request)
        .catch(function (error) {
            console.log(error)
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