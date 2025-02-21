// Definição das perguntas e opções
const questions = [
    "São 6h00 da manhã e seu despertador tocou. Mais um dia se inicia, você: ",
    "Depois de seu descanso você se levanta para sair, qual estilo de roupa você prefere?",
    "Qual é a sua primeira atividade do dia?",
    "Qual é a sua atividade favorita?",
    "Você gosta de viajar?",
    "Prefere filmes ou séries?"
];

const options = [
    ["Desliga o despertador e volta a dormir", 
        "Pensa ´só mais uns minutinhos´ e coloca o despertador em modo soneca", 
        "Desliga o despertador e se levanta, preparado para mais um dia"],

    ["Gosto de vestir roupas fluidas e leves", 
        "Me visto com roupas confortáveis e esportivas", 
        "Criativa, gosto de mostrar meu estilo", 
        "Uso roupas básicas, mas alinhadas ao dia a dia"],

    ["Sempre levanto cedo para ir à academia",
        "Conversar pelo celular",
        "Ir trabalhar/estudar"],

    ["Tecnologia", "Arte", "Dormir"],

    ["Sim", "Não", "Depende"],

    ["Filmes", "Séries", "Nenhum"]
];

// Objeto para armazenar as respostas do usuário
let userAnswers = {};

// Função para exibir as perguntas no chat
function displayQuestion(questionIndex) {
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML = '';  // Limpa o conteúdo do chat antes de adicionar novos elementos.

    if (questionIndex < questions.length) {
        chatBox.innerHTML += `<div class="bot-message">${questions[questionIndex]}</div>`;  // Exibe a pergunta
        options[questionIndex].forEach(option => {
            chatBox.innerHTML += `<div class="user-option" onclick="selectOption('${option}', ${questionIndex}, this)">${option}</div>`;
        });
    } else {
        displayResult();  // Quando as perguntas acabarem, exibe o resultado.
    }
}

// Função que registra a resposta do usuário e avança para a próxima pergunta
function selectOption(option, questionIndex, element) {
    // Registra a resposta
    if (userAnswers[option]) {
        userAnswers[option]++;  // Incrementa se a opção já foi escolhida
    } else {
        userAnswers[option] = 1;  // Inicializa a contagem
    }

    element.classList.add('selected');  // Marca a opção como selecionada

    // Desabilita as outras opções para evitar múltiplas seleções
    const optionsDivs = document.querySelectorAll('.user-option');
    optionsDivs.forEach(div => div.onclick = null);

    // Avança para a próxima pergunta
    setTimeout(() => displayQuestion(questionIndex + 1), 500);
}

// Função para exibir o resultado final
function displayResult() {
    const chatBox = document.getElementById('chat-box');
    const result = determineResult(userAnswers);
    chatBox.innerHTML = `<div class="bot-message">Você é compatível com: ${result}!</div>`;
}

// Lógica para determinar qual garoto é mais compatível
function determineResult(answers) {
    const boys = {
        "Xavier": ["Desliga o despertador e volta a dormir", "Gosto de vestir roupas fluidas e leves", "Conversar pelo celular", "Dormir", "Depende", "Filmes"],
        "Zayne": ["Desliga o despertador e se levanta, preparado para mais um dia", "Uso roupas básicas, mas alinhadas ao dia a dia", "Ir trabalhar/estudar", "Tecnologia", "Sim", "Filmes"],
        "Rafayel": ["Pensa 'só mais uns minutinhos' e coloca o despertador em modo soneca", "Criativa, gosto de mostrar meu estilo", "Conversar pelo celular", "Arte", "Depende", "Séries"],
        "Caleb": ["Desliga o despertador e volta a dormir", "Me visto com roupas confortáveis e esportivas", "Sempre levanto cedo para ir à academia", "Tecnologia", "Sim", "Séries"],
        "Sylus": ["Desliga o despertador e volta a dormir", "Criativa, gosto de mostrar meu estilo", "Sempre levanto cedo para ir à academia", "Tecnologia", "Sim", "Filmes"]
    };

    let bestMatch = "";
    let maxScore = 0;

    for (let boy in boys) {
        let score = boys[boy].reduce((acc, answer) => acc + (answers[answer] || 0), 0);
        if (score > maxScore) {
            maxScore = score;
            bestMatch = boy;
        }
    }

    return bestMatch || "Nenhum garoto compatível encontrado";
}

// Inicia o questionário na primeira pergunta quando a página carregar
window.onload = () => displayQuestion(0);