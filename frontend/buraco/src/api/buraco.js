import api from './axiosConfig';

export const getBuracos = async () => {
    const response = await api.get('/buraco')
        .catch(function (error) {
            console.log(error)
        });
    return response.data;
};

export const getBuracoById = async (id) => {
    const response = await api.put(`/buracos/${id}`);
    return response.data;
};

export const createBuraco = async (data) => {
    const response = await api.post('/buraco', data)
        .catch(function (error) {
            console.log(error)
        });
    return response.data;
};

export const updateBuraco = async (id, data) => {
    const response = await api.put(`/buracos/${id}`, data);
    return response.data;
};

export const deleteBuraco = async (id) => {
    const response = await api.delete(`/buracos/${id}`);
    return response.data;
};

export const votoBuraco = async (id) => {
    const response = await api.post(`/buraco/${id}`)
        .catch(function (error) {
            console.log(error)
        });
    return response.data;
};