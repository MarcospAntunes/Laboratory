const fs = require('fs');
const PDFParse = require('pdf-parse');

const arquivo1 = "AD1.1 - Engenharia de Software - Marcos Antunes.pdf";
const arquivo2 = 'Modelo-de-Contrato-para-Prestação-de-Serviço.pdf';

async function lerPDF(campo, arquivo) {
    try {
        const dataBuffer = fs.readFileSync(arquivo);
        const data = await PDFParse(dataBuffer);
        const text = data.text

        const result = extrairInfo(campo, text)

        if(result) {
            return result
        } else {
            return
        }

    } catch (err) {
        console.log("Erro ao ler arquivo", err);
        return
    }
}

function extrairInfo(campo, texto) {
    const regex = new RegExp(campo + ":\\s*(.*?)(?=[\\n\r]|$)", "i");
    const match = regex.exec(texto)

    if (match && match.length > 1) {
        const result = match[1].trim().replace(/([a-z])([A-Z])/g, '$1 $2');
        return result
    } else {
        return false
    }
}

async function main(campo, arquivo) {
    const result = await lerPDF(campo, arquivo);
    console.log(result);
}

main('Nome', arquivo1);
main('E de outro lado', arquivo2);
