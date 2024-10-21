// utils/notifications.js
import Swal from 'sweetalert2';

export const showSuccessNotification = (title, text) => {
  Swal.fire({
    icon: 'success',
    title,
    text,
    confirmButtonText: 'Continuar'
  });
};

export const showAuthenticationError = () => {
  Swal.fire({
    icon: 'error',
    title: 'Error de autenticación',
    text: 'Cédula o contraseña incorrecta',
    confirmButtonText: 'Entendido'
  });
};

export const showTooManyAttemptsError = () => {
  Swal.fire({
    icon: 'error',
    title: 'Demasiados intentos',
    text: 'Por favor, intente de nuevo más tarde',
    confirmButtonText: 'Entendido'
  });
};

export const showServerError = () => {
  Swal.fire({
    icon: 'error',
    title: 'Error del servidor',
    text: 'Hubo un problema al procesar su solicitud',
    confirmButtonText: 'Entendido'
  });
};

export const showConnectionError = () => {
  Swal.fire({
    icon: 'error',
    title: 'Error de conexión',
    text: 'No se pudo conectar con el servidor',
    confirmButtonText: 'Entendido'
  });
};

export const showUnexpectedError = (message) => {
  Swal.fire({
    icon: 'error',
    title: 'Error inesperado',
    text: message || 'Ocurrió un error inesperado',
    confirmButtonText: 'Entendido'
  });
};

export const showFormErrors = (errors) => {
  Swal.fire({
    icon: 'error',
    title: 'Error en el formulario',
    text: errors.join('\n'),
    confirmButtonText: 'Entendido'
  });
};
