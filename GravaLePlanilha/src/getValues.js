import calcValues from "./calcValues.js";
import sheetData from "./sheetData.js";

// Função que pega os valores da planilha chamando a função sheetData que ira retornar os valores da planilha e, após isso, irá criar um objeto com as respectivas notas e frequência de cada aluno e chamar a função calcValues passando o somatório das notas.

async function getValues() {
    const alunos = {};

    try {
        const values = await sheetData("A2:G");
        
    
        if (values.length > 0) {
            for (let i = 0; i < values.length; i++) {
              const row = values[i];
              const nome = row[0];
              const aulas = row[5];
              const faltas = row[6];
        
              if (!alunos[nome]) {
                alunos[nome] = { notas: {} };
                alunos[nome].frequencia = {
                  aulas: aulas,
                  faltas: faltas
                }
              }
        
              for (let j = 1; j < 3; j++) {
                const notaAtual = `p${j}`;
                const valorAtual = Number(row[j]);
                if(valorAtual != NaN && valorAtual <= 10) {
                  alunos[nome].notas[notaAtual] = valorAtual;
                  alunos[nome].soma ? 
                  alunos[nome].soma += valorAtual
                : 
                  alunos[nome].soma = valorAtual;
                }
              }
              calcValues(nome, alunos[nome].soma, alunos[nome].frequencia);
            }
          } else {
            console.log("Nenhum dado");
          }
    } catch(error) {
        console.log("\nHouve um erro", error);  
    }
}

export default getValues;