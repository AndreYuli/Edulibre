// eslint-disable-next-line no-unused-vars
import React from "react";// Si no usas Link, considera eliminarlo

import { useState } from 'react';

const Profile = () => {
  // Estado inicial del perfil del usuario
  const [user, setUser] = useState({
    name: 'Juan Pérez',
    email: 'juan.perez@example.com',
    phone: '+123456789',
    registrationDate: '01/01/2022',
    lastAccess: '15/03/2023',
    completedCourses: 5,
    ongoingCourses: 2,
    achievements: 3,
  });

  // Función para manejar la edición de la información del usuario
  const handleEdit = () => {
    // Example of updating user information
    setUser({ ...user, name: 'Nuevo Nombre' }); // Update the user's name
    console.log('Edit user information');
  };

  // Función para manejar la eliminación de la cuenta
  const handleDeleteAccount = () => {
    // Implementa la lógica para eliminar la cuenta del usuario
    console.log('Delete user account');
  };

  return (
    <div className="user-profile">
      <h1>Perfil de Usuario</h1>
      <div className="profile-info">
        <img src="path/to/profile-pic.jpg" alt="Foto de Perfil" className="profile-pic" /> {/* Verifica la ruta de la imagen */}
        <p><strong>Nombre:</strong> {user.name}</p>
        <p><strong>Correo Electrónico:</strong> {user.email}</p>
        <p><strong>Teléfono:</strong> {user.phone}</p>
        <p><strong>Fecha de Registro:</strong> {user.registrationDate}</p>
        <p><strong>Último Acceso:</strong> {user.lastAccess}</p>
      </div>

      <div className="account-settings">
        <h2>Configuración de Cuenta</h2>
        <button onClick={handleEdit}>Editar Información</button>
        <button onClick={handleDeleteAccount}>Eliminar Cuenta</button>
      </div>

      <div className="user-activity">
        <h2>Actividad del Usuario</h2>
        <p><strong>Cursos Completados:</strong> {user.completedCourses}</p>
        <p><strong>Cursos en Progreso:</strong> {user.ongoingCourses}</p>
        <p><strong>Logros:</strong> {user.achievements}</p>
      </div>

      <div className="social-interaction">
        <h2>Interacción Social</h2>
        <p><strong>Comentarios:</strong> 10</p>
        <p><strong>Participación en Foros:</strong> 3</p>
      </div>
    </div>
  );
};

export default Profile; 