import React, { useState, useEffect } from 'react';
import { Table } from 'react-bootstrap';
import { getTamanhosBuraco } from '../api/tamanhoBuraco';

const TamanhosBuracoList = () => {
  const [tamanhosBuraco, setTamanhosBuraco] = useState([]);

  useEffect(() => {
    const fetchTamanhosBuraco = async () => {
      const data = await getTamanhosBuraco();
      setTamanhosBuraco(data);
    };
    fetchTamanhosBuraco();
  }, []);

  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nome</th>
        </tr>
      </thead>
      <tbody>
        {tamanhosBuraco.map((tamanhoBuraco) => (
          <tr key={tamanhoBuraco.id}>
            <td>{tamanhoBuraco.id}</td>
            <td>{tamanhoBuraco.nome}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
};

export default TamanhosBuracoList;