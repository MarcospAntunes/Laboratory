const ILovePDFApi = require("@ilovepdf/ilovepdf-nodejs/ILovePDFApi");
const fs = require('fs');
const ImagePdfTask = require('@ilovepdf/ilovepdf-js-core/tasks/ImagePdfTask');
const ILovePDFFile = require('@ilovepdf/ilovepdf-nodejs/ILovePDFFile');

const PUBLIC_KEY = 'project_public_14689e398e8d1ee28a598e41ac872151_I4mKrac3ff4af5731fd9ecdfa8d68c10893b0';
const SECRET_KEY = 'secret_key_f0090f3966e94613a014fa8ad576acc4_ckLRQ1543d8864ef347ca8d6a7b336e73b029';

const instance = new ILovePDFApi(PUBLIC_KEY, SECRET_KEY);

async function converteArquivo(arquivo, taskName) {
    const file = new ILovePDFFile(arquivo);
    
    try {
        let task = instance.newTask(taskName);

        await task.start();
        await task.addFile(file)
        await task.process({ merge_after: true });

        const data = await task.download();
        fs.writeFileSync('./alura-cases.pdf', data);

        console.log('Conversão concluída com sucesso!');
    } catch (error) {
        console.error('Erro ao converter imagem para PDF:', error);
    }
}

converteArquivo('./alura-cases.png', 'imagepdf');
