import React from 'react'
import Logo from '../assets/Logo.svg';
import EduLibre from '../assets/EduLibre.svg';
import '../styles/Header.css';

const Header = () => {
  return (
    <div className='header'>
        <div className='header-content'>
            <img src={Logo} alt='Logo de EduLibre' />
            <img src={EduLibre} alt='letras de  EduLibre' />
        </div>
    </div>
  )
}

export default Header