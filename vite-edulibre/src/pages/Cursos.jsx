// eslint-disable-next-line no-unused-vars
import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getCourses } from '../services/api';
import SelectionPage from '../components/SelectionPage';
import EmojiRain from '../components/EmojiRain';

const EMOJIS = ['📚', '✏️', '🎓', '🖊️', '📝', '📖', '🧠', '💡', '🔍', '🗂️'];

const Cursos = () => {
  const [cursos, setCursos] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const { materiaId } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCursos = async () => {
      try {
        console.log('Fetching courses for materiaId:', materiaId);
        const data = await getCourses(materiaId);
        console.log('Received data:', data);
        
        const formattedCursos = data.map(curso => ({
          id: curso.id,
          value: (
            <div className="curso-content">
              <span className="curso-emoji">📘</span>
              <span className="curso-nombre">{curso.nombre}</span>
            </div>
          )
        }));
        console.log('Formatted courses:', formattedCursos);
        
        setCursos(formattedCursos);
        setError(null);
      } catch (error) {
        console.error('Error al obtener cursos:', error);
        setError('No se pudieron cargar los cursos. Por favor, intente más tarde.');
      } finally {
        setIsLoading(false);
      }
    };

    fetchCursos();
  }, [materiaId]);

  const handleCursoClick = (cursoId) => {
    navigate(`/curso/${cursoId}`);
  };

  if (isLoading) {
    return <div>Cargando cursos...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (cursos.length === 0) {
    return <div>No se encontraron cursos para esta materia.</div>;
  }

  return (
    <>
      <SelectionPage
        title="Cursos Disponibles"
        introMessage="Selecciona un curso para comenzar"
        items={cursos}
        onItemClick={handleCursoClick}
      />
      <EmojiRain emojis={EMOJIS} count={30} />
    </>
  );
};

export default Cursos;