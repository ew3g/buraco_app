import { React, useState } from 'react';
import { useNavigate } from "react-router-dom";
import { esqueciSenha } from '../api/usuario';
import { getQuestaoByEmail } from '../api/questao';
import '../style/esqueci-senha.css'

const EsqueciSenha = () => {

    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [questaoUsuarioResposta, setQuestaoUsuarioResposta] = useState('');
    const [novaSenha, setNovaSenha] = useState('');
    const [novaSenhaRepetida, setNovaSenhaRepetida] = useState('');
    const [questaoUsuario, setQuestaoUsuario] = useState('');
    const [info, setInfo] = useState('');

    const fetchQuestaoByEmail = async () => {

        const request = {
            "email": email,
        }

        await getQuestaoByEmail(request).then(response => {
            if (response.status === 200) {
                setQuestaoUsuario(response.data.pergunta);
                setInfo('');
            } else {
                setQuestaoUsuario('');
                setInfo('Usuário não existe');
            }
        }).catch(err => {
            setQuestaoUsuario('');
            setInfo('Usuário não existe');
        });
    };

    const handleTrocarSenha = async (e) => {
        e.preventDefault();

        setInfo('');

        if (email === '' || novaSenha === '' || novaSenhaRepetida === '') {
            setInfo('Preencha todos os campos');
            return;
        }

        if (novaSenha !== novaSenhaRepetida) {
            setInfo('As senhas não coincidem')
            return;
        }

        const request = {
            "email": email,
            "questao_usuario_resposta": questaoUsuarioResposta,
            "nova_senha": novaSenha,
        };

        await esqueciSenha(request).then(response => {
            console.log(response);
            if (response.status === 200) {
                alert('Senha alterada com sucesso');
                navigate('/');
            } else {
                setInfo('Erro: ' + response.data.detail);
            }
        }).catch(err => {
            setInfo('Erro ao trocar a senha')
        });
    };

    return (

        <div>
            <div className="trocar-senha-container">
                <div className='row'>
                    <div className='col-md-12'>
                        <h2>Troque sua senha</h2>
                    </div>
                </div>
                <div className='row'>
                    <div className='col-md-12'>
                        <form>
                            <div className="form-group">
                                <label htmlFor="email">Email</label>
                                <input
                                    type="email"
                                    className="form-control"
                                    required
                                    id="email"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    onBlur={(e) => fetchQuestaoByEmail()}
                                />
                            </div>
                            <br />
                            <div className="form-group">
                                <label htmlFor="questao-usuario">Responda à questão: {questaoUsuario}</label>
                                <input
                                    type="input"
                                    className="form-control"
                                    required
                                    id="questao-usuario"
                                    value={questaoUsuarioResposta}
                                    onChange={(e) => setQuestaoUsuarioResposta(e.target.value)}
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

                                {info && (
                                    <div className='alert'>{info}</div>
                                )}
                            </div>

                        </form>
                    </div>

                </div>
            </div>
        </div>
    )
}

export default EsqueciSenha;