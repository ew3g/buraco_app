import React, { useState, useEffect } from 'react';
import { Form, Button } from 'react-bootstrap';
import { useNavigate, useParams } from 'react-router-dom';
import { createBuraco, getBuracoById, updateBuraco } from '../api/buraco';
import { getTamanhosBuraco } from '../api/tamanhoBuraco';
import { Table } from 'react-bootstrap';

const BuracoForm = () => {
    const navigate = useNavigate();
    const { id } = useParams();
    const isAddMode = !id;
    const [buraco, setBuraco] = useState({
        tamanhoBuraco: '',
        latitude: '',
        longitude: '',
    });
    const [tamanhosBuraco, setTamanhosBuraco] = useState([]);
    const [submitted, setSubmitted] = useState(false);

    useEffect(() => {
        const fetchTamanhosBuraco = async () => {
            const data = await getTamanhosBuraco();
            setTamanhosBuraco(data);
        };
        fetchTamanhosBuraco();
    }, []);

    return (
        <Form>
            <Form.Group controlId="formTamanhoBuraco">
                <Form.Label>Tamanho do Buraco</Form.Label>
                <Form.Control
                    as="select"
                    value={buraco.tamanhoBuraco}
                    onChange={handleChange}
                    name="tamanhoBuraco"
                    required
                >
                    <option value="" disabled>
                        Selecione um tamanho
                    </option>
                    {tamanhosBuraco.map((tamanho) => (
                        <option key={tamanho.id} value={tamanho.id}>
                            {tamanho.descricao}
                        </option>
                    ))}
                </Form.Control>
            </Form.Group>
            <Form.Group controlId="formLatitude">
                <Form.Label>Latitude</Form.Label>
                <Form.Control
                    type="number"
                    placeholder="Digite a latitude"
                    value={buraco.latitude}
                    onChange={handleChange}
                    name="latitude"
                    required
                />
            </Form.Group>
            <Form.Group controlId="formLongitude">
                <Form.Label>Longitude</Form.Label>
                <Form.Control
                    type="number"
                    placeholder="Digite a longitude"
                    value={buraco.longitude}
                    onChange={handleChange}
                    name="longitude"
                    required
                />
            </Form.Group>
            <Button variant="primary" type="submit">
                {isAddMode ? 'Adicionar' : 'Editar'}
            </Button>
        </Form>



    );
};

export default BuracoForm;