import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Profile from './components/Profile'
import Login from './components/Login';
import EsqueciSenha from './components/EsqueciSenha';
import Home from './components/Home';
import TrocarSenha from './components/TrocarSenha';
import NovoUsuario from './components/NovoUsuario'

const App = () => {
  return (
    <div>
      <Router>
        <Routes>
          <Route exact path="/" element={<Login />} />
          <Route exact path="/home" element={<Home />} />
          <Route exact path="/perfil" element={<Profile />} />
          <Route exact path="/esqueci-senha" element={<EsqueciSenha />} />
          <Route exact path="/troca-senha" element={<TrocarSenha />} />
          <Route exact path="/novo-usuario" element={<NovoUsuario />} />
        </Routes>
      </Router>
    </div>
  );
};

export default App;