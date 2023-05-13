import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import AppNavbar from './components/Navbar';
import BuracosList from './pages/BuracosList';
import BuracoForm from './pages/BuracoForm';
import TamanhosBuracoList from './pages/TamanhosBuracoList';
import UsuariosList from './pages/UsuariosList';
import LoginPage from './pages/LoginPage';
import Mapa from './components/Mapa';


const App = () => {
  return (
    <Router>
      <div>
        <AppNavbar />
        <Routes>
          <Route exact path="/" component={BuracosList} />
          <Route exact path="/buracos" component={BuracosList} />
          <Route exact path="/buracos/adicionar" component={BuracoForm} />
          <Route exact path="/buracos/editar/:id" component={BuracoForm} />
          <Route exact path="/tamanhos-buraco" component={TamanhosBuracoList} />
          <Route exact path="/usuarios" component={UsuariosList} />
          <Route exact path="/login" component={LoginPage} />
        </Routes>
        <Mapa />
      </div>
    </Router>



  );
};

export default App;