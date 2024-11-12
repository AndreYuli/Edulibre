// eslint-disable-next-line no-unused-vars
import React from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000/';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Función para manejar errores de manera consistente
const handleError = (error) => {
  console.error('Error en la llamada a la API:', error.response || error);
  throw error;
};

export const registrarUsuario = async (userData) => {
  try {
    const response = await api.post('api/v1/usuarios', userData);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const loginUsuario = async (credentials) => {
  try {
    const formData = new URLSearchParams();
    formData.append('username', credentials.username);
    formData.append('password', credentials.password);

    const response = await api.post('api/v1/usuarios/token', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Nueva función para solicitar el restablecimiento de contraseña
export const solicitarRestablecimientoContrasena = async (email) => {
  try {
    const response = await api.post('api/v1/usuarios/forgot-password', { correo: email });
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Nueva función para restablecer la contraseña
export const restablecerContrasena = async (token, newPassword) => {
  try {
    const response = await api.post('api/v1/usuarios/reset-password', { token, nueva_contrasena: newPassword });
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const saveUserPreferences = async (preferences) => {
  try {
    const response = await api.post('api/v1/study-preferences', preferences);
    return response.data;
  } catch (error) {
    handleError(error);
    throw error;
  }
};


// Nueva función para obtener las preferencias de estudio del usuario
export const getUserPreferences = async () => {
  try {
    const response = await api.get('api/v1/user-preferences');
    return response.data;
  } catch (error) {
    handleError(error);
  }
};


export const getMateriasGeneral = async () => {
  try {
    const response = await api.get('/api/v1/materias');
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const getUserProgress = async () => {
  try {
    const response = await api.get('api/v1/user-progress');
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const getCourses = async (materiaId) => {
  try {
    const response = await api.get(`/api/v1/cursos?materia_id=${materiaId}`);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};
export const createCourse = async (courseData) => {
  try {
    const response = await api.post('api/v1/cursos', courseData);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const getSubjects = async () => {
  try {
    const response = await api.get('/api/v1/materias');
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const updateCourse = async (courseId, courseData) => {
  try {
    const response = await api.put(`api/v1/cursos/${courseId}`, courseData);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const deleteCourse = async (courseId) => {
  try {
    const response = await api.delete(`api/v1/cursos/${courseId}`);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const getGrados = async () => {
  try {
    const response = await api.get('/api/v1/grados');
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export default api;