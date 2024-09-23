// createLoader es una función que crea un elemento div con la clase loader-div-container-container
export const createLoader = () => {
    const loader = document.createElement('div');
    loader.classList.add("loader-div-container");
    loader.innerHTML = '<div class="loader"></div>';
    document.body.appendChild(loader);
    return loader;
}