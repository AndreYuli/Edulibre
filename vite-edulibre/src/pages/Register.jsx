// eslint-disable-next-line no-unused-vars
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { registrarUsuario, saveUserPreferences } from '../services/api';
import Swal from 'sweetalert2';
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
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const validateCedula = (cedula) => {
    return /^\d{10}$/.test(cedula);
  };

  const validateEmail = (email) => {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
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
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newErrors = {};

    if (!validateCedula(formData.cedula)) {
      newErrors.cedula = 'La cédula debe tener 10 dígitos';
    }

    if (!formData.edad) {
      newErrors.edad = 'La edad es requerida';
    } else if (formData.edad < 0 || formData.edad > 120) {
      newErrors.edad = 'La edad debe estar entre 0 y 120';
    }

    if (!formData.nombre) {
      newErrors.nombre = 'El nombre es requerido';
    }

    if (!validateEmail(formData.email)) {
      newErrors.email = 'El correo electrónico no es válido';
    }

    if (!formData.contraseña) {
      newErrors.contraseña = 'La contraseña es requerida';
    }

    if (formData.contraseña !== formData.confirmarContraseña) {
      newErrors.confirmarContraseña = 'Las contraseñas no coinciden';
    }

    if (Object.keys(newErrors).length > 0) {
      for (const key in newErrors) {
        Swal.fire({
          icon: 'error',
          title: 'Error en el formulario',
          text: newErrors[key],
        });
      }
      return;
    }

    setIsLoading(true);
    try {
      const dataToSend = {
        cedula: parseInt(formData.cedula),
        edad: parseInt(formData.edad),
        nombre: formData.nombre,
        correo: formData.email,
        contrasena: formData.contraseña,
        rol: formData.rol
      };
      const user = await registrarUsuario(dataToSend);
      
      // Guardar las preferencias de estudio
      const preferences = {
        userId: user.id,
        preferences: formData.studyPreferences
      };
      saveUserPreferences(  preferences);

      Swal.fire({
        icon: 'success',
        title: 'Registro exitoso',
        text: 'Tu cuenta ha sido creada',
      });
      navigate('/study-preferences'); // Redirigir a la página de preferencias de estudio
    } catch (error) {
      if (error.response && error.response.data && error.response.data.detail) {
        Swal.fire({
          icon: 'error',
          title: 'Error de registro',
          text: error.response.data.detail,
        });
      } else {
        Swal.fire({
          icon: 'error',
          title: 'Error de registro',
          text: 'Ocurrió un error inesperado. Por favor, inténtalo de nuevo más tarde.',
        });
      }
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
              />
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
              />
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