import { createLoader } from '../../components/loader/loader.js';
import { createMessageErrorForm } from '../../components/messageErrorForm/messageErrorForm.js';
let loader;
// inicialAction es una función que se ejecuta al iniciar la petición
export const inicialAction = () => {
    loader = createLoader();
};

// mensajeErrorFuncHandler es una función que se ejecuta cuando ocurre un error en la petición
const mensajeErrorFuncHandler = ({mensajeError}) => {
    let message = '';
    // Se recorre cada elemento del array mensajeError
    for (let i = 0; i < mensajeError.length; i++) {
        message += `${i + 1}: ${mensajeError[i].message}<br>`;
    }
    return message;
}

// messageDataFuncHandler es una función que se ejecuta cuando ocurre un error en la petición

const messageDataFuncHandler = ({messageData}) => {
    // Se borran los elementos del array messageErrorForm
    let errorMessageInputPersona = document.querySelectorAll('.error-message-input-persona');
    if (errorMessageInputPersona) errorMessageInputPersona.forEach(element => element.remove());
    // Se recorre cada elemento del array messageData
    for (let key in messageData) {
        let mensajeError = mensajeErrorFuncHandler({ mensajeError: messageData[key] });
        createMessageErrorForm({ keyName: key, mensajeErrors: mensajeError })
    }
}

// responseAction es una función que se ejecuta cuando la petición se ha realizado correctamente
export const responseAction = (data) => {
    // Si la petición se ha realizado correctamente, se redirige al usuario a la página de inicio
    if (data.success) {
        window.location.href = data.redirect;
        return;
    }
    // Si ocurre un error, se muestra un mensaje de error en la pantalla
    if (data.error) {
        let messageData = JSON.parse(data.error);
        messageDataFuncHandler({messageData});
        return;
    }
};
// errorAction es una función que se ejecuta cuando ocurre un error en la petición
export const errorAction = (error) => {
    document.getElementById('error-message').innerHTML = error;
};


// finallyAction es una función que se ejecuta al finalizar la petición
export const finallyAction = () => {
    loader.remove();
};
