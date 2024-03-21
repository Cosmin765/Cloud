const HOSTNAME = 'localhost';
const PORT = 8000;
const SERVER = `http://${HOSTNAME}:${PORT}`;

const PILOTS_GET = `${SERVER}/pilots`;
const SCORES_GET = `${SERVER}/scores`;

export { 
    SERVER,
    PILOTS_GET,
    SCORES_GET
 };
