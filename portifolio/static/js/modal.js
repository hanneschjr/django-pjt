const modal = document.getElementById("email-modal");

const openBtn = document.getElementById("open-email-modal");

const closeBtn = document.getElementById("close-email-modal");

const form = document.getElementById("contact-form");

// Abrir o modal
openBtn.addEventListener("click", function(event) {

    event.preventDefault();

    modal.classList.add("active");

});

// Fechar o modal
closeBtn.addEventListener("click", function() {

    modal.classList.remove("active");

});


// Fechar o modal automaticamente após 5 segundos
document.addEventListener("DOMContentLoaded", () => {

    const msgModal = document.getElementById("email-msg-modal");

    if (msgModal) {

        setTimeout(() => {

            msgModal.classList.remove("active");

        }, 5000);

    }

});

// Interceptar o submit para exibir loading
form.addEventListener("submit", function() {
    // Fecha o modal do formulário
    modal.classList.remove("active");

    // Cria e exibe o overlay de loading
    const loadingOverlay = document.createElement("div");
    loadingOverlay.id = "loading-overlay";
    loadingOverlay.innerHTML = `
        <div class="loading-content">
            <div class="spinner"></div>
            <p>Enviando mensagem...</p>
        </div>
    `;
    document.body.appendChild(loadingOverlay);

    // Pequeno delay para garantir que o overlay aparece antes do submit
    // NÃO chame event.preventDefault() — deixa o formulário submeter normalmente
});

