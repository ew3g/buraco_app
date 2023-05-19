import React, { useState } from 'react';
import { Button, Form } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
//import { login } from '../api/auth';
//import { AuthContext } from '../AuthContext';

const LoginPage = () => {
    const [email, setEmail] = useState('');
    const [senha, setSenha] = useState('');
    const [erro, setErro] = useState(null);

    //const { login } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            //const token = await login(email, senha);
            navigate.navigate('/')
        } catch (err) {
            setErro(err.message);
        }
    };

    return (
        <Form onSubmit={handleSubmit}>
            <h1>Login</h1>
            {erro && <p>{erro}</p>}
            <Form.Group controlId="formEmail">
                <Form.Label>Email</Form.Label>
                <Form.Control
                    type="email"
                    placeholder="Digite o email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
            </Form.Group>
            <Form.Group controlId="formSenha">
                <Form.Label>Senha</Form.Label>
                <Form.Control
                    type="password"
                    placeholder="Digite a senha"
                    value={senha}
                    onChange={(e) => setSenha(e.target.value)}
                    required
                />
            </Form.Group>
            <Button variant="primary" type="submit">
                Login
            </Button>
        </Form>
    );
};

export default LoginPage;