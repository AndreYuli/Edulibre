import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getGrados } from '../services/api';
import SelectionPage from '../components/SelectionPage';
import '../styles/Grados.css';
import EmojiRain from '../components/EmojiRain';

const EMOJIS = ['🎓', '0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🎓', '🎓', '🎓', '🎓'];

const Grados = () => {
  const [grados, setGrados] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchGrados = async () => {
      const gradosData = await getGrados();
      const formattedGrados = gradosData.map(grado => ({
        id: grado.id,
        value: (
          <div className="grado-content">
            <div className="grado-numero">{grado.numero}</div>
            <div className="grado-nombre">{grado.nombre}</div>
          </div>
        )
      }));
      setGrados(formattedGrados);
      setIsLoading(false);
    };
    fetchGrados();
  }, []);

  const handleGradoClick = (gradoId) => {
    navigate(`/materias/${gradoId}`);
  };

  if (isLoading) {
    return <div>Cargando grados...</div>;
  }

  return (
    <>
      <EmojiRain emojis={EMOJIS} count={30} />
      <SelectionPage
        title="Escoge tu grado"
        introMessage="¡Vamos a escoger por cuál grado quieres empezar!"
        items={grados}
        onItemClick={handleGradoClick}
      />
    </>
  );
};

export default Grados;
