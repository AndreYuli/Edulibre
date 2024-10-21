// components/Form.jsx
import React from 'react';
import PropTypes from 'prop-types';
import '../styles/Form.css';

const Form = ({ onSubmit, children, className }) => (
  <form onSubmit={onSubmit} className={`custom-form ${className}`}>
    {children}
  </form>
);

Form.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  children: PropTypes.node.isRequired,
  className: PropTypes.string,
};

Form.defaultProps = {
  className: '',
};

export default Form;
