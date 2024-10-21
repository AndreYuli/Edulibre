// components/Input.jsx
import React from 'react';
import PropTypes from 'prop-types';
import '../styles/Input.css';

const Input = ({ type, name, value, onChange, placeholder, required, className, min, max }) => (
  <input
    type={type}
    name={name}
    value={value}
    onChange={onChange}
    placeholder={placeholder}
    required={required}
    className={`custom-input ${className}`}
    min={min}
    max={max}
  />
);

Input.propTypes = {
  type: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
  onChange: PropTypes.func.isRequired,
  placeholder: PropTypes.string,
  required: PropTypes.bool,
  className: PropTypes.string,
  min: PropTypes.number,
  max: PropTypes.number,
};

Input.defaultProps = {
  placeholder: '',
  required: false,
  className: '',
  min: undefined,
  max: undefined,
};

export default Input;
