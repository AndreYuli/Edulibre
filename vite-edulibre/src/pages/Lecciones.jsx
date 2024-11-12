import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { getLeccionesGeneral } from '../services/api';
import '../styles/Lecciones.css';
import SelectionPage from '../components/SelectionPage';
import EmojiRain from '../components/EmojiRain';

const EMOJI_MAP = {
  'Introducción': '📖',
  'Teoría': '📚',
  'Ejercicios': '✏️',
  'Práctica': '💡',
  'Evaluación': '📝'
};

const EMOJIS = ['📖', '📚', '✏️', '💡', '📝', '🎯', '📊', '🔍', '📓', '✨', '📌', '📎', '🗂️', '📋', '📒'];

const Lecciones = () => {
  const [lecciones, setLecciones] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();
  const { cursoId } = useParams();

  useEffect(() => {
    const fetchLecciones = async () => {
      try {
        const data = await getLeccionesGeneral();
        const leccionesFiltradas = cursoId 
          ? data.filter(leccion => leccion.curso_id === parseInt(cursoId))
          : data;
        setLecciones(leccionesFiltradas);
      } catch (error) {
        console.error('Error fetching lecciones:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchLecciones();
  }, [cursoId]);

  const handleLeccionClick = (leccionId) => {
    navigate(`/leccion/${leccionId}`);
  };

  if (isLoading) {
    return <div>Cargando lecciones...</div>;
  }

  const title = cursoId 
    ? "Lecciones del Curso" 
    : "Lecciones Disponibles";
    
  const introMessage = cursoId 
    ? "¡Vamos a explorar las lecciones de este curso!"
    : "¡Selecciona una lección para comenzar!";

  return (
    <>
      <SelectionPage
        title={title}
        introMessage={introMessage}
        items={lecciones.map((leccion, index) => ({
          id: leccion.id,
          value: (
            <div className="leccion-content">
              <span className="leccion-emoji">
                {EMOJI_MAP[leccion.tipo] || '📚'}
              </span>
              <span className="leccion-titulo">{leccion.titulo}</span>
            </div>
          )
        }))}
        onItemClick={handleLeccionClick}
      />
      <EmojiRain emojis={EMOJIS} count={30} />
    </>
  );
};

export default Lecciones;