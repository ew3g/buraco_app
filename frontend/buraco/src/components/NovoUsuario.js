import { React, useState, useEffect } from 'react'
import { createUsuario } from '../api/usuario';
import { useNavigate } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../style/novo-usuario.css';
import { getQuestoes } from '../api/questao';




const NovoUsuario = () => {

    const navigate = useNavigate();
    const [nomeUsuario, setNomeUsuario] = useState('');
    const [email, setEmail] = useState('');
    const [senha, setSenha] = useState('');
    const [senhaRepetida, setSenhaRepetida] = useState('');
    const [questoes, setQuestoes] = useState([]);
    const [questaoSelecionada, setQuestaoSelecionada] = useState('');
    const [resposta, setResposta] = useState('');
    const [info, setInfo] = useState('');

    useEffect(() => {
        const fetchQuestoes = async () => {
            const data = await getQuestoes();
            setQuestoes(data);
        };
        fetchQuestoes();
    }, []);

    const handleCriarUsuario = async (e) => {
        e.preventDefault();

        if (nomeUsuario === '' || email === '' || senha === '' || senhaRepetida === '' || questaoSelecionada === '' || resposta === '') {
            setInfo('Por favor, preencha todos os campos');
            return;
        }

        if (senha !== senhaRepetida) {
            setInfo('As senhas não conferem');
            return;
        }

        const request = {
            "nome_usuario": nomeUsuario,
            "email": email,
            "senha": senha,
            "questao_usuario_id": questaoSelecionada,
            "questao_usuario_resposta": resposta
        };

        await createUsuario(request).then(response => {
            if (response) {
                if (response.status === 201) {
                    setInfo('');
                    alert('Usuário criado com sucesso');
                    navigate('/');
                } else if (response.status === 409) {
                    setInfo("Usuário já existe");
                } else {
                    setInfo("Erro ao criar usuário: " + response.data.detail);
                }

            } else {
                setInfo("Erro ao criar usuário");
            }
        }).catch(err => {
            setInfo(err);
        });
    };

    const handleQuestaoSelecionadaSelectChange = (event) => {
        console.log(event.target.value);
        setQuestaoSelecionada(event.target.value);
    }

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
                        <div className="row">
                            <div className="col-md-12">
                                <select className='form-select' value={questaoSelecionada} onChange={handleQuestaoSelecionadaSelectChange}>
                                    <option value="null">Selecione uma questão de segurança</option>
                                    {questoes.map(questao => (
                                        <option key={questao.id} value={questao.id}>
                                            {questao.pergunta}
                                        </option>
                                    ))}
                                </select>
                            </div>
                        </div>
                        <br />
                        <div className="form-group">
                            <label htmlFor="resposta">Resposta</label>
                            <input
                                type="input"
                                className="form-control"
                                required
                                id="resposta"
                                value={resposta}
                                onChange={(e) => setResposta(e.target.value)}
                            />
                        </div>
                        <br />
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
                            {info && (
                                <div className='alert'>{info}</div>
                            )}
                        </div>

                    </form>
                </div>

            </div>
        </div>
    )
}

export default NovoUsuario;