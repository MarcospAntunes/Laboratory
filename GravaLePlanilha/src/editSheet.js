import { sheets, auth, sheetID } from '../index.js'

// Função para editar os valores da planilha

async function editSheet(alunoIndex, situacao, p3, nf) {
    async function result(column, value) {
        await sheets.spreadsheets.values.update({
            auth: await auth.getClient(),
            spreadsheetId: sheetID,
            range: `Página1!${column}${alunoIndex + 2}`,
            valueInputOption: "RAW",
            resource: {
                values: [[value]]
            }
        });
    }
    await result("D", p3); // Altera os valores da nota p3 de cada aluno.
    await result("E", nf); // Altera os valores da nota final de cada aluno.
    await result("H", situacao); // altera os valores da Situação de cada aluno.

    if(situacao === "Exame Final") {
        if(5 <= nf) {
            await result("H", "Aprovado");
        } else {
            await result("H", "Reprovado");
        }
    }
}
    

export default editSheet;