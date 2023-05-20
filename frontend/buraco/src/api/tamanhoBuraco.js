import api from './axiosConfig';

export const getTamanhosBuraco = async () => {
    const response = await api.get('/tamanho-buraco')
        .catch(function (error) {
            console.log(error)
        });
    return response.data
};

export const getTamanhoBuracoById = async (id) => {
    const response = await api.put(`/tamanhosBuraco/${id}`);
    return response.data;
};

export const createTamanhoBuraco = async (data) => {
    const response = await api.post('/tamanho-buraco', data);
    return response.data;
};

export const updateTamanhoBuraco = async (id, data) => {
    const response = await api.put(`/tamanhosBuraco/${id}`, data);
    return response.data;
};

export const deleteTamanhoBuraco = async (id) => {
    const response = await api.delete(`/tamanhosBuraco/${id}`);
    return response.data;
};