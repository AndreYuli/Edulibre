// eslint-disable-next-line no-unused-vars
import React from 'react';
import Header from '../components/Header';
import emojis from '../assets/Emojis.svg';
import '../styles/Home.css';
import information from '../assets/information.svg';

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
                    <div classname='information-text'>
                        <h1>Nuestros cursos y herramientas de estudio están diseñados para ayudarte a entender el material y estar listo para tu examen con éxito.</h1>
                    </div>
                    <div className='information-image'>
                        <img src={information} alt='Información' />
                    </div>
                </div>
             </section>
          </main>
      </div>
    )
  }

export default Home;
