// eslint-disable-next-line no-unused-vars
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/Profile.css';
import SelectionPage from '../components/SelectionPage'; // Importar SelectionPage

const Profile = () => {
  const [user, setUser] = useState(null);
  const [preferenciasEstudio, setPreferenciasEstudio] = useState([]);
  const [materias, setMaterias] = useState([]); // Nuevo estado para materias

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await axios.get('URL_DE_TU_API'); 
        setUser(response.data); 
        setPreferenciasEstudio(response.data.preferenciasEstudio || []);
        setMaterias(response.data.materias || []); // Asumiendo que la API devuelve materias
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    };

    fetchUserData();
  }, []); // El array vacío asegura que se ejecute solo una vez al montar el componente

  const handleEdit = () => {
    // Logic for editing user information
    console.log('Edit button clicked');
  };

  const handleDeleteAccount = () => {
    // Logic for deleting the user account
    console.log('Delete account button clicked');
  };

  if (!user) {
    return <div>Cargando...</div>; // Muestra un mensaje de carga mientras se obtienen los datos
  }

  const handleMateriaClick = (materiaId) => {
    // Lógica para manejar el clic en una materia (puedes navegar a otra página si es necesario)
    console.log(`Materia seleccionada: ${materiaId}`);
  };

  return (
    <div className="user-profile">
      <h1>Perfil de Usuario</h1>
      <div className="profile-info">
        <div className="profile-pic" /> {/* Imagen de perfil */}
        <div className="user-details">
          <p><strong>Nombre:</strong> {user.nombre}</p>
          <p><strong>Correo Electrónico:</strong> {user.correo}</p>
          <p><strong>Cédula:</strong> {user.cedula}</p>
          <p><strong>Edad:</strong> {user.edad}</p>
        </div>
      </div>

      <div className="account-settings">
        <h2>Configuración de Cuenta</h2>
        <div className="button-group">
          <button onClick={handleEdit}>Editar Información</button>
          <button onClick={handleDeleteAccount}>Eliminar Cuenta</button>
        </div>
      </div>

      <div className="study-preferences">
        <h2>Preferencias de Estudio</h2>
        {preferenciasEstudio.length > 0 ? (
          preferenciasEstudio.map((preferencia, index) => (
            <p key={index}><strong>Preferencia {index + 1}:</strong> {preferencia.preferencia}</p>
          ))
        ) : (
          <p>No hay preferencias de estudio disponibles.</p>
        )}
      </div>

      <div className="materias">
        <h2>Materias</h2>
        <SelectionPage
          title="Materias Disponibles"
          introMessage="Selecciona una materia para más detalles."
          items={materias.map((materia) => ({
            id: materia.id,
            value: (
              <div className="materia-content">
                <span className="materia-nombre">{materia.nombre}</span>
              </div>
            )
          }))}
          onItemClick={handleMateriaClick}
        />
      </div>
    </div>
  );
};

export default Profile; 