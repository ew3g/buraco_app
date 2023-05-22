import { React, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { auth } from '../api/auth'
import logo from '../img/pothole.png'
import '../style/login.css'
import { useNavigate } from "react-router-dom";



const Login = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [loginError, setLoginError] = useState(false)

    const asyncLocalStorage = {
        setItem: async function (key, value) {
            await null
            return localStorage.setItem(key, value)
        },
        getItem: async function (key) {
            await null
            return localStorage.getItem(key)
        }
    }

    const handleLogin = async (e) => {
        e.preventDefault()
        const response = await auth(email, password);
        if (response && response.data && response.data.token) {
            setLoginError(false)
            asyncLocalStorage.setItem('token', response.data.token).then(data => {
                asyncLocalStorage.setItem('usuarioId', response.data.usuarioId).then(data => {
                    asyncLocalStorage.setItem('email', response.data.email).then(data => {
                        navigate("/home");
                    })
                })
            })
        } else {
            console.log('falhou');
            setLoginError(true);
        }



    }

    return (
        <div className="login-container">
            <div className='row'>
                <div className='col-md-12'>
                    <h2>Olha o Buraco! <img src={logo} className="logo-icon" alt="Logo da aplicação de um carro caindo em um buraco" /></h2>
                </div>
            </div>
            <div className='row'>
                <div className='col-md-12'>
                    <form>
                        <div className="form-group">
                            <label htmlFor="username">Email</label>
                            <input
                                type="email"
                                className="form-control"
                                required
                                id="username"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                            />
                        </div>
                        <br />
                        <div className="form-group">
                            <label htmlFor="password">Senha</label>
                            <input
                                type="password"
                                className="form-control"
                                required
                                id="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                        </div>
                        <br />
                        {loginError && (
                            <div className='alert'>Falha no login. Verifique suas credenciais e tente novamente.</div>
                        )}
                        <div className='row'>
                            <div className='col-md-12'>
                                <button className="btn btn-primary" onClick={handleLogin}>
                                    Login
                                </button>

                            </div>
                        </div>
                        <br />
                        <div className='row'>
                            <div className='col-md-6'>
                                <a className='btn btn-primary' href='/novo-usuario'>Novo Usuário</a>
                            </div>
                            <div className='col-md-6'>
                                <a href='/esqueci-senha'>Esqueci minha senha</a>
                            </div>
                        </div>
                    </form>
                </div>

            </div>
        </div>
    );
}

export default Login