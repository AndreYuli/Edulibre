import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/StudyPreferences.css';
import '../styles/EmojiRain.css'; // Asegúrate de importar los estilos del EmojiRain
import SelectionPage from '../components/SelectionPage';
import EmojiRain from '../components/EmojiRain';
import { saveUserPreferences } from '../services/api';
import { showPreferencesSaveSuccess, showPreferencesSaveError } from '../utils/notifications';

const EMOJIS = ['📚', '🎓', '✏️', '🖋️', '📝', '🔬', '🧮', '🌎', '💡', '0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣'];

const StudyPreferences = () => {
  const navigate = useNavigate();

  const handleMethodChange = async (method) => {
    // Aquí debes obtener el ID del usuario actual
    const userId = 1; // Reemplaza esto con el ID real del usuario

    // Guarda la preferencia en la base de datos
    const preferences = {
      usuario_id: userId,
      preferencia: method, // 'grados' o 'materias'
    };

    try {
      await saveUserPreferences(preferences); // Espera a que se guarden las preferencias
      console.log('Preferencias guardadas correctamente:', preferences);

      // Muestra un mensaje de éxito
      showPreferencesSaveSuccess();

      // Navega a la página correspondiente
      navigate(`/${method}`);
    } catch (error) {
      console.error('Error al guardar preferencias:', error);

      // Muestra un mensaje de error
      showPreferencesSaveError();
    }
  };

  const items = [
    { id: 'materias', value: (
      <>
        <div className="emoji-container">
          <span className="emoji">📚</span>
        </div>
        <div className="option-title-container">
          <span className="option-title">Por Materias</span>
        </div>
      </>
    )},
    { id: 'grados', value: (
      <>
        <div className="emoji-container">
          <span className="emoji">🎓</span>
        </div>
        <div className="option-title-container">
          <span className="option-title">Por Grados</span>
        </div>
      </>
    )}
  ];

  return (
    <>
      <EmojiRain emojis={EMOJIS} count={30} />
      <SelectionPage
        title="¿Cómo te gustaría estudiar?"
        introMessage="Elige tu método preferido"
        items={items}
        onItemClick={handleMethodChange} // Asegúrate de que esta función se pase correctamente
      />
    </>
  );
};

export default StudyPreferences;