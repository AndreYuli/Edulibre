// eslint-disable-next-line no-unused-vars
import React from 'react';
import '../styles/Footer.css';

const Footer = () => {
    return (
        <footer className="footer">
            <div className="footer-content">
                <p>&copy; {new Date().getFullYear()} Todos los derechos reservados EduLibre.</p>
            </div>
        </footer>
    );
}

export default Footer;
