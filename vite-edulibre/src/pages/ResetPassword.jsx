import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import Swal from 'sweetalert2';
import '../styles/ResetPassword.css';
import Header from '../components/Header';
import Footer from '../components/Footer';
import { restablecerContrasena } from '../services/api';

const ResetPassword = () => {
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  // Obtener el token de la URL
  const token = new URLSearchParams(location.search).get('token');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Las contraseñas no coinciden',
      });
      return;
    }

    setIsLoading(true);

    try {
      await restablecerContrasena(token, password);
      Swal.fire({
        icon: 'success',
        title: '¡Contraseña restablecida!',
        text: 'Tu contraseña ha sido actualizada exitosamente.',
      });
      navigate('/login');
    } catch (error) {
      console.error('Error al restablecer la contraseña:', error);
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: error.response?.data?.detail || 'Hubo un problema al restablecer tu contraseña. Por favor, intenta de nuevo.',
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <Header />
      <div className="reset-password-page">
        <div className="reset-password-container">
          <h2>Restablecer Contraseña</h2>
          <form onSubmit={handleSubmit} className="reset-password-form">
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Nueva contraseña"
              required
            />
            <input
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder="Confirmar nueva contraseña"
              required
            />
            <button type="submit" disabled={isLoading}>
              {isLoading ? 'Restableciendo...' : 'Restablecer Contraseña'}
            </button>
          </form>
        </div>
      </div>
      <Footer />
    </>
  );
};

export default ResetPassword;
