
    import { getInformation } from '../../utils/api/getInformation.js';

    export const getControllers = (url) => {
        return getInformation(url);
    };