import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';
import { useNavigate } from "react-router-dom";

const AppNavbar = () => {
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('token');
        navigate("/");
    };

    return (
        <Navbar bg="dark" variant="dark" expand="lg">
            <Navbar.Brand>Minha Aplicação</Navbar.Brand>
            <Navbar.Toggle aria-controls="app-navbar-collapse" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="ml-auto">
                    <LinkContainer to="/home">
                        <Nav.Link>Mapa</Nav.Link>
                    </LinkContainer>
                    <LinkContainer to="/perfil">
                        <Nav.Link>Meu Perfil</Nav.Link>
                    </LinkContainer>
                    <Nav.Link onClick={handleLogout}>Logout</Nav.Link>}
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
};

export default AppNavbar;