import { postInformation } from '../../utils/api/postInformation.js';
import { inicialAction, responseAction, errorAction, finallyAction } from './../../help/postControlersRegister/helpPostControlersRegister.js';

const fun = (event) => {
    // event.preventDefault() evita que se envíe el formulario al servidor
    event.preventDefault();
    // form es el formulario que se envia al servidor
    const form = event.target;
    const url = form.action;
    const dataToSend = new FormData(form);
    // postInformation es una función que se encarga de enviar información a un servidor
    // y realizar acciones dependiendo de la respuesta del servidor
    postInformation({ url, dataToSend, inicialAction, responseAction, errorAction, finallyAction });
}
// Se agrega un event listener al formulario para que se ejecute la función cuando se envíe el formulario
document.addEventListener('submit', fun);