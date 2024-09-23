// postInformation es una función que se encarga de enviar información a un servidor
// y realizar acciones dependiendo de la respuesta del servidor
export const postInformation = ({ url, dataToSend, inicialAction, responseAction, errorAction, finallyAction }) => {
    // inicialAction es una función que se ejecuta al iniciar la petición
    inicialAction();
    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': dataToSend.get('csrfmiddlewaretoken')
        },
        body: dataToSend
    })
    .then(response => response.json())
    .then(data => {
        // responseAction es una función que se ejecuta cuando la petición se ha realizado correctamente
        responseAction(data);
    })
    .catch((error) => {
        // errorAction es una función que se ejecuta cuando ocurre un error en la petición
        errorAction(error);
    })
    .finally(() => {
        // finallyAction es una función que se ejecuta al finalizar la petición
        finallyAction();
    });
};