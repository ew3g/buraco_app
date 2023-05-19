import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { getUsuarioById } from '../api/usuario';
import Login from './Login';
import AppNavbar from './Navbar';
import '../style/profile.css'


const Profile = () => {
    const [usuario, setUsuario] = useState([]);

    useEffect(() => {
        const fetchUsuario = async () => {
            const usuarioId = localStorage.getItem('usuarioId');
            if (usuarioId) {
                const data = await getUsuarioById(usuarioId);
                setUsuario(data)
            }

        };
        fetchUsuario();
    }, []);


    return (
        <div>
            {usuario ?
                <div>
                    <AppNavbar />
                    <div className="profile-container">
                        <h2>Perfil de Usuário</h2>
                        <div className="row">
                            <div className="col-md-12">
                                <p>Usuário: {usuario.nomeUsuario}</p>
                                <p>Email: {usuario.email}</p>
                            </div>
                        </div>
                        <div>
                            <button className="btn btn-primary" onClick={undefined}>
                                Trocar senha
                            </button>
                        </div>
                    </div>
                </div> : <Login />
            }
        </div>
    )
}

export default Profile