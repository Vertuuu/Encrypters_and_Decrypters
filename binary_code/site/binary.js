
const userInput = prompt("Digite 1 para converter texto em binário ou 2 para converter binário em texto:");

if (userInput === "1") {
    const text = prompt("Digite o texto que deseja converter para binário:");
    const binary = textToBinary(text);
    console.log("Texto em Binário:", binary);
} else if (userInput === "2") {
    const binary = prompt("Digite o código binário que deseja converter para texto:");
    const text = binaryToText(binary);
    console.log("Texto Convertido:", text);
} else {
    console.log("Opção inválida. Por favor, recarregue e tente novamente.");
}
function textToBinary(text) {
    return text.split('')
        .map(char => char.charCodeAt(0).toString(2).padStart(8, '0'))
        .join(' ');
}

// Função para converter código binário em texto
function binaryToText(binary) {
    return binary.split(' ')
        .map(bin => String.fromCharCode(parseInt(bin, 2)))
        .join('');
}