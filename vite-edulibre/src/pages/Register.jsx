// eslint-disable-next-line no-unused-vars
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { registrarUsuario } from '../services/api';
import { showSuccessNotification, showUnexpectedError } from '../utils/notifications';
import '../styles/Register.css';
import Layout from '../components/Layout';
import Form from '../components/Form';
import Input from '../components/Input';
import Button from '../components/Button';
import LogoRegister from '../assets/LogoLogin.svg';

const Register = () => {
  const [formData, setFormData] = useState({
    cedula: '',
    edad: '',
    nombre: '',
    email: '',
    contraseña: '',
    confirmarContraseña: '',
    rol: 'Estudiante'
  });
  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const validateCedula = (cedula) => {
    return /^\d{10}$/.test(cedula);
  };

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    let newValue = type === 'number' ? (value === '' ? '' : Number(value)) : value;
    
    if (name === 'cedula') {
      newValue = value.replace(/\D/g, '').slice(0, 10);
    }

    setFormData(prevState => ({
      ...prevState,
      [name]: newValue
    }));

    if (name === 'cedula') {
      setErrors(prevErrors => ({
        ...prevErrors,
        cedula: validateCedula(newValue) ? '' : 'La cédula debe tener 10 dígitos'
      }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newErrors = {};

    if (!validateCedula(formData.cedula)) {
      newErrors.cedula = 'La cédula debe tener 10 dígitos';
    }

    if (formData.contraseña !== formData.confirmarContraseña) {
      newErrors.confirmarContraseña = 'Las contraseñas no coinciden';
    }

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    setIsLoading(true);
    try {
      const dataToSend = Object.fromEntries(
        Object.entries(formData).filter(([key]) => key !== 'confirmarContraseña')
      );
      await registrarUsuario(dataToSend);
      showSuccessNotification('Registro exitoso', 'Tu cuenta ha sido creada');
      navigate('/login');
    } catch (error) {
      showUnexpectedError('Error de registro', error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Layout>
      <div className='register-page'>
        <div className='register-container'>
          <div className='register-container-img'>
            <img src={LogoRegister} alt="Logo de Registro" />
          </div>
          <div className='register-form-container'>
            <h2> Vamos a crear tu cuenta</h2>
            <Form onSubmit={handleSubmit} className="register-form">
              <Input
                type="text"
                name="cedula"
                placeholder="Cédula (10 dígitos)"
                value={formData.cedula}
                onChange={handleChange}
                required
                className={errors.cedula ? 'input-error' : ''}
              />
              {errors.cedula && <span className="error-message">{errors.cedula}</span>}
              <Input
                type="number"
                name="edad"
                placeholder="Edad"
                value={formData.edad}
                onChange={handleChange}
                required
                min={0}
                max={120}
              />
              <Input
                type="text"
                name="nombre"
                placeholder="Nombre completo"
                value={formData.nombre}
                onChange={handleChange}
                required
              />
              <Input
                type="email"
                name="email"
                placeholder="Correo electrónico"
                value={formData.email}
                onChange={handleChange}
                required
              />
              <Input
                type="password"
                name="contraseña"
                placeholder="Contraseña"
                value={formData.contraseña}
                onChange={handleChange}
                required
              />
              <Input
                type="password"
                name="confirmarContraseña"
                placeholder="Confirmar contraseña"
                value={formData.confirmarContraseña}
                onChange={handleChange}
                required
                className={errors.confirmarContraseña ? 'input-error' : ''}
              />
              {errors.confirmarContraseña && <span className="error-message">{errors.confirmarContraseña}</span>}
              <select
                name="rol"
                value={formData.rol}
                onChange={handleChange}
                required
              >
                <option value="Estudiante">Estudiante</option>
                <option value="Administrador">Administrador</option>
              </select>
              <Button 
                type="submit" 
                className={isLoading ? 'loading' : ''}
                disabled={isLoading}
              >
                {isLoading ? 'Registrando...' : 'Continue aqui'}
              </Button>
            </Form>
            <div className="register-footer">
              <p>¿Ya tienes una cuenta?</p>
              <Link to="/login" className='login-link'>Inicia sesión aquí</Link>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default Register;
