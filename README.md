# RenomearPDF_IBGE
O projeto tem como objetivo renomear uma lista de mapas em PDF que foram escaneados. O software abre cada PDF, identifica o número do setor ao qual ele pertence e renomeia o respectivo arquivo.
## Executando o projeto com o PyCharm
Para que o software funcione utilizando o PyCharm, é necessário instalar as dependências do projeto como o **Tesseract-ocr** e o **Poppler**. Siga o passo a passo:
1. Instale o tesseract-ocr (_https://sourceforge.net/projects/tesseract-ocr.mirror/_)
   - 1.1. Na tela de instalação do programa, selecione o idioma inglês e avance.
   - 1.2. Na tela "Choose Components" clique no "+" da opção "Additional language data (download)"
   - 1.3. Selecione o idioma "Portuguese" e avance até concluir a instalação.
2. Altere a linha 7 do arquivo RenomearPDF.py para o caminho de instalação do tesseract.
3. Instale o poppler (_https://blog.alivate.com.au/poppler-windows/_) copiando a pasta "poppler-0.68.0" e colando em C:\Program Files (x86)
   - 3.1. Após colar a pasta no destino correto, vá na bandeira do windows procure por "Editar as variáveis de ambiente do sistema" e abra.
   - 3.2. Clique no botão "Variáveis de ambiente..."
   - 3.3. No bloco "Variáveis do sistema" clique duas vezes no nome "Path"
   - 3.4. Na janela que abriu clique em "Novo" e cole o seguinte caminho: C:\Program Files (x86)\poppler-0.68.0\bin
   - 3.5. Clique em OK em todas as janelas abertas.
## Executando o projeto do Windows
Para conseguir executar o arquivo **RenomearPDF.exe** em uma máquina sem o python e sem as dependências instaladas, você precisa ter instalado pelo menos o **tesseract-ocr** e o **poppler**.
Para tudo funcionar, siga os seguintes passos:
1. Siga os passos 1 e 3 da seção anterior.
2. Insira os pdfs que precisa renomear na pasta **pdfs**.
3. Execute o arquivo RenomearPDF.exe
