function showLoadingState() {
    const container = document.getElementById("result-container");
    container.innerHTML = `
        <p class="status-message">Processing your try-on... this can take up to a minute.</p>
    `;
}

function showResultImage(resultUrl) {
    const container = document.getElementById("result-container");
    container.innerHTML = `
        <img src="${resultUrl}" alt="Your try-on result" class="result-image">
    `;
}

function showErrorState(message) {
    const container = document.getElementById("result-container");
    container.innerHTML = `
        <p class="error-message">Something went wrong: ${message}</p>
    `;
}