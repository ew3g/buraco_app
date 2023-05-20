import { React, useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import { getUsuarioById, trocarSenha } from '../api/usuario';
import '../style/trocar-senha.css'


import AppNavbar from './Navbar';

const TrocarSenha = () => {

    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [senhaAtual, setSenhaAtual] = useState('');
    const [novaSenha, setNovaSenha] = useState('');
    const [novaSenhaRepetida, setNovaSenhaRepetida] = useState('');
    const [trocarSenhaError, setTrocarSenhaError] = useState(false);
    const [trocarSenhaSucesso, setTrocarSenhaSucesso] = useState(false);
    const [senhaIgualError, setSenhaIgualError] = useState(false);

    useEffect(() => {
        const storedToken = localStorage.getItem('token');
        if (!storedToken) {
            navigate("/");
        }

        const fetchUsuario = async () => {
            const usuarioId = localStorage.getItem('usuarioId');
            if (usuarioId) {
                const data = await getUsuarioById(usuarioId);
                setEmail(data.email);
            }

        };
        fetchUsuario();
    }, [navigate]);

    const handleTrocarSenha = async (e) => {
        e.preventDefault();

        if (novaSenha !== novaSenhaRepetida) {
            setSenhaIgualError(true);
            return;
        } else {
            setSenhaIgualError(false);
        }

        const request = {
            "email": email,
            "senha": senhaAtual,
            "nova_senha": novaSenha,
        };

        await trocarSenha(localStorage.getItem('usuarioId'), request).then(response => {
            if (response) {
                console.log(response);
                setTrocarSenhaError(false);
                setTrocarSenhaSucesso(true);
            } else {
                setTrocarSenhaError(true);
                setTrocarSenhaSucesso(false);
            }
        }).catch(err => {
            setTrocarSenhaError(true);
            setTrocarSenhaSucesso(false);
            console.log(err);
        });
    };

    return (

        <div>
            <AppNavbar />
            <div className="trocar-senha-container">
                <div className='row'>
                    <div className='col-md-12'>
                        <h2>Trocar Senha</h2>
                    </div>
                </div>
                <div className='row'>
                    <div className='col-md-12'>
                        <form>
                            <div className="form-group">
                                <label htmlFor="senha-atual">Senha atual</label>
                                <input
                                    type="password"
                                    className="form-control"
                                    required
                                    id="senha-atual"
                                    value={senhaAtual}
                                    onChange={(e) => setSenhaAtual(e.target.value)}
                                />
                            </div>
                            <br />
                            <div className="form-group">
                                <label htmlFor="nova-senha">Nova senha</label>
                                <input
                                    type="password"
                                    className="form-control"
                                    required
                                    id="nova-senha"
                                    value={novaSenha}
                                    onChange={(e) => setNovaSenha(e.target.value)}
                                />
                            </div>
                            <br />
                            <div className="form-group">
                                <label htmlFor="nova-senha-repetida">Repita a nova senha</label>
                                <input
                                    type="password"
                                    className="form-control"
                                    required
                                    id="nova-senha-repetida"
                                    value={novaSenhaRepetida}
                                    onChange={(e) => setNovaSenhaRepetida(e.target.value)}
                                />
                            </div>
                            <br />
                            <div className='row'>
                                <div className='col-md-9'>
                                    <button className="btn btn-primary btn-sm" onClick={handleTrocarSenha}>
                                        Trocar Senha
                                    </button>
                                </div>
                            </div>
                            <div className='row'>
                                {trocarSenhaError && (
                                    <div className='alert'>Erro, verifique sua senha atual.</div>
                                )}
                                {trocarSenhaSucesso && (
                                    <div className='alert'>Senha alterada com sucesso.</div>
                                )}
                                {senhaIgualError && (
                                    <div className='alert'>As senhas não coincidem.</div>
                                )}
                            </div>

                        </form>
                    </div>

                </div>
            </div>
        </div>
    )
}

export default TrocarSenha;