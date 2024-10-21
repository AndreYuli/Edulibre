import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { getMateriasGeneral } from '../services/api';
import '../styles/Materias.css';
import SelectionPage from '../components/SelectionPage';
import EmojiRain from '../components/EmojiRain';

const EMOJI_MAP = {
  'Matemáticas': '🧮',
  'Lectura Crítica': '📚',
  'Sociales y Ciudadanas': '🌎',
  'Ciencias Naturales': '🔬',
  'Inglés': '🌐'
};

const EMOJIS = ['🧮', '📚', '🌎', '🔬', '🌐', '✏️', '🎨', '🎵', '⚽', '🧠', '🔢', '🗺️', '🧪', '🔭', '🌍'];

const Materias = () => {
  const [materias, setMaterias] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();
  const { gradoId } = useParams();

  useEffect(() => {
    const fetchMaterias = async () => {
      try {
        const data = await getMateriasGeneral();
        setMaterias(data);
      } catch (error) {
        console.error('Error fetching materias:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchMaterias();
  }, []);

  const handleMateriaClick = (materiaId) => {
    if (gradoId) {
      navigate(`/cursos`);
    } else {
      navigate(`/cursos/${materiaId}`);
    }
  };

  if (isLoading) {
    return <div>Cargando materias...</div>;
  }

  const title = gradoId ? `Materias del Grado ${gradoId}` : "Materias Disponibles";
  const introMessage = gradoId 
    ? `¡Vamos a escoger por cuál materia quieres empezar en el grado ${gradoId}!`
    : "¡Vamos a escoger por cuál materia quieres empezar!";

  return (
    <>
      <SelectionPage
        title={title}
        introMessage={introMessage}
        items={materias.map((materia, index) => ({
          id: index,
          value: (
            <div className="materia-content">
              <span className="materia-emoji">{EMOJI_MAP[materia.nombre] || ''}</span>
              <span className="materia-nombre">{materia.nombre}</span>
            </div>
          )
        }))}
        onItemClick={handleMateriaClick}
      />
      <EmojiRain emojis={EMOJIS} count={30} />
    </>
  );
};

export default Materias;
