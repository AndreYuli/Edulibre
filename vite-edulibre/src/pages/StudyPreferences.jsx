import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/StudyPreferences.css';
import '../styles/EmojiRain.css'; // Asegúrate de importar los estilos del EmojiRain
import SelectionPage from '../components/SelectionPage';
import EmojiRain from '../components/EmojiRain';

const EMOJIS = ['📚', '🎓', '✏️', '🖋️', '📝', '🔬', '🧮', '🌎', '💡', '0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣'];

const StudyPreferences = () => {
  const navigate = useNavigate();

  const handleMethodChange = (method) => {
    navigate(`/${method}`);
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
        onItemClick={handleMethodChange}
      />
    </>
  );
};

export default StudyPreferences;
