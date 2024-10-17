// eslint-disable-next-line no-unused-vars
import React from 'react';
import Home from './pages/Home.jsx';
import { Route, Routes } from 'react-router-dom';

function App() {

  return (
    <Routes>
      <Route path='/' element={<Home />} />
    </Routes>
  )
}

export default App;
