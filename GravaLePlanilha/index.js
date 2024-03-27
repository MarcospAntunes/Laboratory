import { google } from 'googleapis';
import credentials from './credentials.json' assert { type: 'json' };
import getValues from './src/getValues.js'

const sheets = google.sheets('v4');
const sheetID = "1cu7II1W6V0q5rIKdbdTw6Z-uuX39AaS3hWN31Cd_5ug" ;
const auth = new google.auth.GoogleAuth({
    credentials: credentials,
    scopes: ["https://www.googleapis.com/auth/spreadsheets"]
});

async function main() {
    console.log("Iniciando Programa...");
    await getValues();
    console.log("Programa finalizado!");
}

main();

export {sheets, sheetID, auth};