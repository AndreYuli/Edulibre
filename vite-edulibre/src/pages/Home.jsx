// eslint-disable-next-line no-unused-vars
import React from 'react';
import Header from '../components/Header';
import emojis from '../assets/Emojis.svg';
import '../styles/Home.css';
import information from '../assets/information.svg';
import '../styles/Benefits.css';
import Footer from '../components/Footer';

const Home = () => {
    return (
      <div>
          <Header />
          <main>
             <section className='introduction-section'>
              <div className='introduction-content'>
                  <div className='introduction-image'>
                      <img src={emojis} alt='Emojis' />
                  </div>
                  <div className='introduction-text'>
                      <h1>Completa tu bachillerato de forma divertida, efectiva y sin costo.</h1>
                      <button>Comienza ahora</button>
                  </div>
              </div>
             </section>
             <section className='information-section'>
                <div className='information-content'>
                    <div className='information-text'>
                        <h1>Nuestros cursos y herramientas de estudio están diseñados para ayudarte a entender el material y estar listo para tu examen con éxito.</h1>
                    </div>
                    <div className='information-image'>
                        <img src={information} alt='Información' />
                    </div>
                </div>
                <p className='centered-text'>Aprende cuando quieras</p>
             </section>
             <section className='benefits-section'>
                <div className='benefits-content'>
                    <div className='benefit-item'>
                        <h2>Educación Accesible</h2>
                        <p>Accede a cursos gratuitos y refuerza tus conocimientos.</p>
                    </div>
                    <div className='benefit-item'>
                        <h2>Estudia a tu Ritmo</h2>
                        <p>Organiza tu propio plan de estudio y sigue tu progreso.</p>
                    </div>
                    <div className='benefit-item'>
                        <h2>Título Oficial</h2>
                        <p>Prepárate para obtener tu título de bachiller con nuestros recursos.</p>
                    </div>
                </div>
             </section>
          </main>
          <Footer />
      </div>
    )
  }

export default Home;
