import React, { useState, useEffect } from 'react';
import { Table } from 'react-bootstrap';
import { getUsuarios } from '../api/usuario';

const UsuariosList = () => {
    const [usuarios, setUsuarios] = useState([]);

    useEffect(() => {
        const fetchUsuarios = async () => {
            const data = await getUsuarios();
            setUsuarios(data);
        };
        fetchUsuarios();
    }, []);

    return (
        <Table striped bordered hover>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                {usuarios.map((usuario) => (
                    <tr key={usuario.id}>
                        <td>{usuario.id}</td>
                        <td>{usuario.nome}</td>
                        <td>{usuario.email}</td>
                    </tr>
                ))}
            </tbody>
        </Table>
    );
};

export default UsuariosList;