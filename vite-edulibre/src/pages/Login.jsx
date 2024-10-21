// pages/Login.jsx
import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { loginUsuario } from '../services/api';
import { 
  showSuccessNotification, 
  showAuthenticationError, 
  showTooManyAttemptsError, 
  showServerError, 
  showConnectionError, 
  showUnexpectedError
} from '../utils/notifications';
import '../styles/Login.css';
import Layout from '../components/Layout';
import Form from '../components/Form';
import Input from '../components/Input';
import Button from '../components/Button';
import LogoLogin from '../assets/LogoLogin.svg';

const Login = () => {
  const [credentials, setCredentials] = useState({ username: '', password: '' });
  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const validateForm = () => {
    let tempErrors = {};
    if (!credentials.username.trim()) tempErrors.username = "La cédula es requerida";
    if (!/^\d+$/.test(credentials.username)) tempErrors.username = "La cédula debe contener solo números";
    if (!credentials.password) tempErrors.password = "La contraseña es requerida";
    if (credentials.password.length < 6) tempErrors.password = "La contraseña debe tener al menos 6 caracteres";
    setErrors(tempErrors);
    return Object.keys(tempErrors).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCredentials(prevState => ({ ...prevState, [name]: value }));
    if (errors[name]) {
      setErrors(prevErrors => ({ ...prevErrors, [name]: null }));
    }
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    if (!validateForm()) {
      showUnexpectedError('Por favor, corrija los errores en el formulario');
      return;
    }

    setIsLoading(true);
    try {
      const response = await loginUsuario(credentials);
      if (response && response.access_token) {
        localStorage.setItem('token', response.access_token);
        showSuccessNotification('¡Bienvenido!', 'Has iniciado sesión correctamente');
        if (response.is_first_login) {
          navigate('/study-preferences');
        } else {
          navigate('/profile');
        }
      } else {
        throw new Error('No se recibió un token de acceso válido');
      }
    } catch (error) {
      console.error('Error durante el inicio de sesión:', error);
      if (error.response) {
        switch (error.response.status) {
          case 401:
            showAuthenticationError();
            break;
          case 429:
            showTooManyAttemptsError();
            break;
          default:
            showServerError();
        }
      } else if (error.request) {
        showConnectionError();
      } else {
        showUnexpectedError(error.message);
      }
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Layout>
      <div className='login-page'>
        <div className='login-container'>
          <div className='login-container-img'>
            <img src={LogoLogin} alt="Logo de Login" />
          </div>
          <div className='login-form-container'>
            <h2>¿Ya está aprendiendo con nosotros?</h2>
            <Form onSubmit={handleLogin}>
              <Input
                type="text"
                name="username"
                placeholder="Cédula"
                value={credentials.username}
                onChange={handleChange}
                error={errors.username}
                required
              />
              <Input
                type="password"
                name="password"
                placeholder="Contraseña"
                value={credentials.password}
                onChange={handleChange}
                error={errors.password}
                required
              />
              <div className="forgot-password">
                <Link to="/forgot-password">¿Olvidaste tu contraseña?</Link>
              </div>
              <Button 
                type="submit" 
                className={isLoading ? 'loading' : ''}
                disabled={isLoading}
              >
                {isLoading ? 'Cargando...' : 'Continuar aquí'}
              </Button>
            </Form>
            <div className="login-footer">
              <p>¿No tienes una cuenta?</p>
              <Link to="/register" className='register-link'>Regístrate aquí</Link>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default Login;
