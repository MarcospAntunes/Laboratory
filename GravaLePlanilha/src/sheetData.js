import { auth, sheetID, sheets } from "../index.js";

async function sheetData(range) {
    try {
        const sheet = await sheets.spreadsheets.values.get({
            auth: await auth.getClient(),
            spreadsheetId: sheetID,
            range: `Página1!${range}`
        });
        return sheet.data.values;
    
    } catch(error) {
        console.log("Erro ao coletar dados da planilha", error);
    }
}

export default sheetData;