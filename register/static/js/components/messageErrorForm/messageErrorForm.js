export const createMessageErrorForm = ({ keyName, mensajeErrors }) => {
    const messageErrorForm = document.createElement('p');
    messageErrorForm.classList.add("text-naranja_claro", "error-message-input-persona");
    messageErrorForm.innerHTML = `${mensajeErrors}`;
    document.querySelector(`[name="${keyName}"]`).parentNode.appendChild(messageErrorForm);
    return messageErrorForm;
};