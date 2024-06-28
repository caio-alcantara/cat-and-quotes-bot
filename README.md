<center>
<img src="imgLiti.png" width = 60%>
</center>

# Projeto experimental de BOT desenvolvido em summer job

# 1. Introdução 
&nbsp;&nbsp;&nbsp;&nbsp;A Liti Saúde é uma startup brasileira com foco em fazer com que as pessoas encontrem uma melhor qualidade de vida, fazendo isso por meio da oferta de consultas médicas nas área de nutrição, planos alimentares e um acompanhamento pessoal de todos os clientes que desejam levar um estilo de vida mais saudável. <br> 
&nbsp;&nbsp;&nbsp;&nbsp;Durante o meu *summer job* na startup Liti Saude, tenho como proposta desenvolver um chatbot para Whatsapp que envolva inteligência artificial. O cerne da ideia é relativamente simples: Pessoas podem mandar dúvidas simples relacionadas a saúde e nutrição (Ex: 'Quantas calorias tem em 150g de arroz branco?') e o chatbot retornaria uma resposta que foi gerada, a partir da pergunta do usuário, pelo ChatGPT, o LLM da OpenAI. <br>
&nbsp;&nbsp;&nbsp;&nbsp;A partir do contexto sobre o projeto que irei trabalhar, este documento tem como finalidade apresentar um mini-projeto que foi desenvolvido antes de se começar o projeto do chatbot com ChatGPT.

# 2. Sobre o presente projeto 
&nbsp;&nbsp;&nbsp;&nbsp;O presente projeto tem como objetivo iniciar as minhas práticas no desenvolvimento real de chatbots, além de me familiarizar com o funcionamento de tecnologias como Flask e Twilio, as quais estarão presentes no projeto real. Além disso, durante o desenvolvimento deste projeto, fui capaz de estudar, entender e aplicar diversas boas práticas programação, arquitetura de software e testes unitários, sempre trabalhando com a linguagem Python.
&nbsp;&nbsp;&nbsp;&nbsp;Dessa forma, o projeto que desenvolvi é um chatbot que utiliza da API da plataforma Twilio para lidar com o recebimento e envio de mensagens para um número Whatsapp. No geral, o chatbot apenas responde "sobre gatos e citações". Ou seja, o usuário pode mandar uma mensagem para o número e perguntar sobre algum desses assuntos e o bot lhe retornará uma mensagem com uma citação famosa, ou uma mensagem com uma foto aleatória de um gato, ou até mesmo os dois juntos! Caso o usuário não pergunte sobre gatos ou citações, o bot entrega uma resposta genérica.  
&nbsp;&nbsp;&nbsp;&nbsp;Para construir este projeto, segui o tutorial presente <a href="https://www.twilio.com/en-us/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio">aqui</a>. Entretanto, caso você olhe para a estrutura do projeto aqui disponível, verá que muita coisa está diferente, uma vez que refatorei grande parte, senão todo, o código, adequando o código aos princípios <a href='https://medium.com/desenvolvendo-com-paixao/o-que-%C3%A9-solid-o-guia-completo-para-voc%C3%AA-entender-os-5-princ%C3%ADpios-da-poo-2b937b3fc530'>SOLID</a> e a <a href="https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html">Clean Architecture</a> e escrevendo diversos testes unitários. Vale ressaltar que, apesar de todas as mudanças, o bot funciona da exata mesma maneira que o bot do tutorial

# 3. Tecnologias utilizadas
&nbsp;&nbsp;&nbsp;&nbsp;Em relação às tecnologias que foram utilizadas para o projeto, temos:
- Flask: um potente microframework para a linguagem Python, utilizado para subir um servidor WEB e lidar com requisições HTTP
- Twilio: um serviço que dispõe de números de Whatsapp e uma API que podem ser utilizados para construir toda sorte de bots para Whatsapp.
- PyTest: uma biblioteca Python utilizada para escrever testes unitários para todas as funções, classes e módulos do projeto
- Localhost.run: O Localhost.run é uma ferramenta de tunelamento, e foi utilizada para expor o meu servidor local para a WEB a fim de poder testar o chatbot

# 4. Como executar o código
- Clone este repositório na sua máquina
    ```
    git clone https://github.com/caio-alcantara/cat-and-quotes-bot.git
    ```

- Na raíz do projeto, crie um arquivo .env
- Dentro do arquivo .env, você deve configurar a URL do site que gera imagens de gatos e da API de citações. Sinta-se a vontade para usar URLs diferentes, mas a minha sugestão é:
    ```
    Cole isso dentro de .env
    CAT_IMG_URL="https://cataas.com/cat" 
    QUOTE_API_URL="https://api.quotable.io/random"
    ```

- Crie uma conta Twilio em https://www.twilio.com/pt-br.
- Após criar a conta, você terá um número gratuito. O intuito aqui não é ensinar como se usa o Twilio, então apenas vou dizer para acessar o seu console Twilio, ir até a seção de 'Try it Out' -> 'Send a Whatsapp message'. Assim, você poderá testar o seu número de sandbox. O que você precisa ter em mente é que é para este número que você mandará as mensagens para o bot. 

- Abra uma janela do terminal e instale as dependências: 
    ```bash
    pip install -r requirements.txt
    ```

- Abra uma janela do terminal, navegue até a pasta src e rode o arquivo principal
    ```bash
    cd src
    python main.py
    ```
- Abra uma segunda janela de terminal e rode o comando:
    ```
    ssh -R 80:localhost:4000 nokey@localhost.run
    ```

- Após isso, o bot estará rodando no seu localhost:4000, e o localhost.run estará expondo tal localhost para a WEB. No terminal em que você rodou o localhost.run, você obterá uma URL semelhante a https://23a3d6421f8910.lhr.life/bot. Copie a URL que você recebeu, e, no seu console Twilio, em 'sandbox settings', cole a URL em 'when a message comes in'. Lembre-se de adicionar um /bot no final da URL e salvar.

- Feitos esses passos, você está pronto para enviar uma mensagem para o seu número Twilio Sandbox e testar o bot. 

# 5. Objetivos alcançados
&nbsp;&nbsp;&nbsp;&nbsp;Ao iniciar este projeto, eu possuía alguns objetivos que esperava alcançar ao finalizá-lo. Dentre eles, posso citar:
- Obter um entendimento básico sobre princípios SOLID e Clean Architecture, conceitos que, no começo do projeto, eram completamente desconhecidos para mim.
- Entender melhor como o Twilio funciona e como eu poderia receber uma mensagem de um usuário num servidor, tratá-la e retornar algo. Entendendo isso, acredito que **grande** parte do desenvolvimento de um chatbot é desvendada. 
- Obter um conhecimento um pouco mais aprofundado em boas práticas de desenvolvimento de testes unitários.

Ao final do projeto, posso dizer que todas essas 3 metas foram alcançadas, e, dentre elas, dou um destaque maior à segunda. Entender como o Twilio funciona é um passo gigantesco (e que já foi dado neste projeto) para o chatbot com ChatGPT que desenvolverei no *summer job*.
