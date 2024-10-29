// eslint-disable-next-line no-unused-vars
import React from 'react';
import Home from './pages/Home.jsx';
import { Route, Routes } from 'react-router-dom';
import Login from './pages/Login.jsx';
import Register from './pages/Register.jsx';
import ForgotPassword from './pages/ForgotPassword.jsx';
import ResetPassword from './pages/ResetPassword.jsx';
import StudyPreferences from './pages/StudyPreferences.jsx';
import Materias from './pages/Materias';
import Grados from './pages/Grados';
import Cursos from './pages/Cursos';
import Profile from './pages/Profile.jsx';

function App() {
  return (
    <Routes>
      <Route path='/' element={<Home />} />
      <Route path='/register' element={<Register />} />
      <Route path='/login' element={<Login />} />
      <Route path='/forgot-password' element={<ForgotPassword />} />
      <Route path='/reset-password' element={<ResetPassword />} />
      <Route path='/study-preferences' element={<StudyPreferences />} />
      <Route path='/materias' element={<Materias />} />
      <Route path='/materias/:gradoId' element={<Materias />} />
      <Route path='/grados' element={<Grados />} />
      <Route path='/cursos' element={<Cursos />} />
      <Route path='/cursos/:materiaId' element={<Cursos />} />
      <Route path='/profile' element={<Profile />} />
    </Routes>
  )
}

export default App;
