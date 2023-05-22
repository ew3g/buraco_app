import api from './axiosConfig';

export const getQuestaoByEmail = async (data) => {
    const response = await api.post("/questao/usuario", data)
        .then(function (res) {
            return res;
        })
        .catch(function (error) {
            return error.response;
        });
    return response;
};

export const getQuestoes = async () => {
    const response = await api.get("/questao",)
        .then(function (res) {
            return res.data;
        })
        .catch(function (error) {
            return error.response;
        });
    return response;
};