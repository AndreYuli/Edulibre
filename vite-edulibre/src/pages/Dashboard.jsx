import React, { useEffect, useState } from 'react';
import { getUserCourses, getUserProgress } from '../services/api';

const Dashboard = () => {
  const [courses, setCourses] = useState([]);
  const [progress, setProgress] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const coursesData = await getUserCourses();
      const progressData = await getUserProgress();
      setCourses(coursesData);
      setProgress(progressData);
    };
    fetchData();
  }, []);

  return (
    <div className="dashboard">
      <h1>Mi Dashboard</h1>
      <section className="courses-in-progress">
        <h2>Mis Cursos en Progreso</h2>
        {courses.map(course => (
          <div key={course.id} className="course-card">
            <h3>{course.nombre}</h3>
            <p>Progreso: {progress[course.id]}%</p>
            {/* Añadir más detalles y un enlace al curso */}
          </div>
        ))}
      </section>
      {/* Añadir más secciones según sea necesario */}
    </div>
  );
};

export default Dashboard;
