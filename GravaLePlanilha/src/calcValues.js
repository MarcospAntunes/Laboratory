import editSheet from "./editSheet.js";
import sheetData from "./sheetData.js";

// Função para calcular a situação de cada aluno

async function calcValues(aluno, somatorio, frequencia) {
    try {
        const names = await sheetData("A2:A");
        const alunoIndex = names.findIndex(row => row[0] === aluno);
        let situacao;
        const { aulas, faltas } = frequencia;

        if(alunoIndex !== -1) {
            let p3 = 0;
            let nf = somatorio / 2;
            
            switch (true) {
                case faltas > (aulas * 0.25):
                    situacao = "Reprovado por Falta";
                    break

                case nf < 5:
                    situacao = "Reprovado por Nota";
                    break;

                case nf >= 5 && nf < 7:
                    situacao = "Exame Final";
                    p3 = 5;
                    nf = Math.round((somatorio + p3) / 2);
                    break;

                case nf >= 7:
                    situacao = "Aprovado";
                    break;

                default:
                    situacao = "Indefinido";
            } 
            editSheet(alunoIndex, situacao, p3, nf);
        }
    } catch(error) {
        console.log("\nHouve um erro ao editar a planilha!", error);
    }
}

export default calcValues;