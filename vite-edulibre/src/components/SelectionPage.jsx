import React from 'react';
import PropTypes from 'prop-types';
import Header from './Header';
import Footer from './Footer';

const SelectionPage = ({ 
  title, 
  introMessage, 
  items, 
  onItemClick
}) => {
  return (
    <>
      <Header />
      <div className="selection-page">
        <div className="background-shape shape1" />
        <div className="background-shape shape2" />
        <h1>{title}</h1>
        <p className="intro-message">{introMessage}</p>
        <div className="selection-grid">
          {items.map((item, index) => (
            <button 
              key={item.id}
              className={`selection-card ${index % 2 === 0 ? 'left' : 'right'}`}
              onClick={() => onItemClick(item.id)}
            >
              {item.value}
            </button>
          ))}
        </div>
      </div>
      <Footer />
    </>
  );
};

SelectionPage.propTypes = {
  title: PropTypes.string.isRequired,
  introMessage: PropTypes.string.isRequired,
  items: PropTypes.arrayOf(PropTypes.shape({
    id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
    value: PropTypes.node.isRequired
  })).isRequired,
  onItemClick: PropTypes.func.isRequired
};

export default SelectionPage;
