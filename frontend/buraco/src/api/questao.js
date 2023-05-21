import api from './axiosConfig';

export const getQuestaoByEmail = async (email) => {
    const request = {
        "email": email,
    }
    const response = await api.post("/questao/usuario", request)
        .then(function (res) {
            return res;
        })
        .catch(function (error) {
            return error.response;
        });
    return response;
};