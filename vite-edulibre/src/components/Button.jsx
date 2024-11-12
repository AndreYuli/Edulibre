// components/Button.jsx
// eslint-disable-next-line no-unused-vars
import React from 'react';
import PropTypes from 'prop-types';
import '../styles/Button.css';

const Button = ({ type, disabled, className, children, onClick }) => (
  <button 
    type={type} 
    disabled={disabled} 
    className={`custom-button ${className}`}
    onClick={onClick}
  >
    {children}
  </button>
);

Button.propTypes = {
  type: PropTypes.string,
  disabled: PropTypes.bool,
  className: PropTypes.string,
  children: PropTypes.node.isRequired,
  onClick: PropTypes.func,
};

Button.defaultProps = {
  type: 'button',
  disabled: false,
  className: '',
  onClick: () => {},
};

export default Button;
