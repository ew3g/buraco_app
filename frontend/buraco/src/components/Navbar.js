import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

const AppNavbar = () => {
    const handleLogout = () => {
        localStorage.removeItem('token');
        window.location.reload();
    };

    return (
        <Navbar bg="dark" variant="dark" expand="lg">
            <Navbar.Brand>Minha Aplicação</Navbar.Brand>
            <Navbar.Toggle aria-controls="app-navbar-collapse" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="ml-auto">
                    <LinkContainer to="/buraco">
                        <Nav.Link>Buracos</Nav.Link>
                    </LinkContainer>
                    <LinkContainer to="/tamanho-buraco">
                        <Nav.Link>Tamanhos de Buraco</Nav.Link>
                    </LinkContainer>
                    <LinkContainer to="/usuario">
                        <Nav.Link>Usuários</Nav.Link>
                    </LinkContainer>
                    <Nav.Link onClick={handleLogout}>Logout</Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
};

export default AppNavbar;