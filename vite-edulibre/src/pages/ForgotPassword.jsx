import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Swal from 'sweetalert2';
import '../styles/ForgotPassword.css';
import Header from '../components/Header';
import Footer from '../components/Footer';
import { solicitarRestablecimientoContrasena } from '../services/api';

const ForgotPassword = () => {
  const [email, setEmail] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [resetLink, setResetLink] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const response = await solicitarRestablecimientoContrasena(email);
      setResetLink(response.reset_link);
      
      Swal.fire({
        icon: 'success',
        title: '¡Enlace de restablecimiento generado!',
        text: 'En una aplicación real, este enlace se enviaría por correo electrónico. Por ahora, lo mostraremos aquí.',
        confirmButtonText: 'Mostrar enlace'
      }).then(() => {
        Swal.fire({
          title: 'Enlace de restablecimiento',
          text: response.reset_link,
          icon: 'info'
        });
      });
    } catch (error) {
      console.error('Error al solicitar restablecimiento de contraseña:', error);
      
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: error.response?.data?.detail || 'Hubo un problema al procesar tu solicitud. Por favor, intenta de nuevo más tarde.',
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <Header />
      <div className="forgot-password-page">
        <div className="forgot-password-container">
          <h2>¿Olvidaste tu contraseña?</h2>
          <p>Ingresa tu correo electrónico y te enviaremos instrucciones para restablecerla.</p>
          <form onSubmit={handleSubmit} className="forgot-password-form">
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Correo electrónico"
              required
            />
            <button type="submit" disabled={isLoading}>
              {isLoading ? 'Enviando...' : 'Enviar instrucciones'}
            </button>
          </form>
          {resetLink && (
            <div className="reset-link">
              <p>Enlace de restablecimiento (solo para demostración):</p>
              <a href={resetLink} target="_blank" rel="noopener noreferrer">{resetLink}</a>
            </div>
          )}
          <div className="forgot-password-footer">
            <Link to="/login">Volver al inicio de sesión</Link>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
};

export default ForgotPassword;
