import { React, useState } from 'react'
import { createUsuario } from '../api/usuario';
import { useNavigate } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../style/novo-usuario.css'



const NovoUsuario = () => {

    const navigate = useNavigate();
    const [nomeUsuario, setNomeUsuario] = useState('');
    const [email, setEmail] = useState('');
    const [senha, setSenha] = useState('');
    const [senhaRepetida, setSenhaRepetida] = useState('');
    const [senhaIgualError, setSenhaIgualError] = useState(false);
    const [novoUsuarioError, setNovoUsuarioError] = useState(false);
    const [novoUsuarioErrorDescription, setNovoUsuarioErrorDescription] = useState('');

    const handleCriarUsuario = async (e) => {
        e.preventDefault();

        if (senha !== senhaRepetida) {
            setSenhaIgualError(true);
            return;
        } else {
            setSenhaIgualError(false);
        }

        const request = {
            "nome_usuario": nomeUsuario,
            "email": email,
            "senha": senha,
        };

        await createUsuario(request).then(response => {
            if (response) {
                if (response.status === 201) {
                    setNovoUsuarioError(false);
                    alert('Usuário criado com sucesso');
                    navigate('/');
                } else if (response.status === 409) {
                    setNovoUsuarioError(true);
                    setNovoUsuarioErrorDescription("Usuário já existe");
                } else {
                    setNovoUsuarioError(true);
                    setNovoUsuarioErrorDescription("Erro ao criar usuário: " + response.data.detail);
                }

            } else {
                setNovoUsuarioError(true);
                setNovoUsuarioErrorDescription("Erro ao criar usuário");
            }
        }).catch(err => {
            setNovoUsuarioError(true);
            setNovoUsuarioErrorDescription(err);
        });
    };

    return (
        <div className="novo-usuario-container">
            <div className='row'>
                <div className='col-md-12'>
                    <h2>Novo Usuário</h2>
                </div>
            </div>
            <div className='row'>
                <div className='col-md-12'>
                    <form>
                        <div className="form-group">
                            <label htmlFor="nome-usuario">Nome</label>
                            <input
                                type="input"
                                className="form-control"
                                required
                                id="input"
                                value={nomeUsuario}
                                onChange={(e) => setNomeUsuario(e.target.value)}
                            />
                        </div>
                        <br />
                        <div className="form-group">
                            <label htmlFor="email">Email</label>
                            <input
                                type="email"
                                className="form-control"
                                required
                                id="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                            />
                        </div>
                        <br />
                        <div className="form-group">
                            <label htmlFor="senha">Senha</label>
                            <input
                                type="password"
                                className="form-control"
                                required
                                id="senha"
                                value={senha}
                                onChange={(e) => setSenha(e.target.value)}
                            />
                        </div>
                        <br />
                        <div className="form-group">
                            <label htmlFor="senha-repetida">Repita a senha</label>
                            <input
                                type="password"
                                className="form-control"
                                required
                                id="senha-repetida"
                                value={senhaRepetida}
                                onChange={(e) => setSenhaRepetida(e.target.value)}
                            />
                        </div>
                        <br />
                        <div className='row'>
                            <div className='col-md-9'>
                                <button className="btn btn-primary btn-sm" onClick={handleCriarUsuario}>
                                    Criar usuário
                                </button>
                            </div>
                        </div>
                        <div className='row'>
                            {novoUsuarioError && (
                                <div className='alert'>Ocorreu um erro: {novoUsuarioErrorDescription}</div>
                            )}
                            {senhaIgualError && (
                                <div className='alert'>As senhas não coincidem.</div>
                            )}
                        </div>

                    </form>
                </div>

            </div>
        </div>
    )
}

export default NovoUsuario;