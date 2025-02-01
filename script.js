function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    let chatBox = document.getElementById("chat-box");

    if (userInput.trim() === "") return;

    // Add user message to chat with class
    let userMessage = `<div class="message user-message"><b>You:</b> ${userInput}</div>`;
    chatBox.innerHTML += userMessage;

    fetch("/ask", {
        method: "POST",
        body: JSON.stringify({ message: userInput }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        let botMessage = `<div class="message bot-message"><b>Bot:</b> ${data.response}</div>`;
        chatBox.innerHTML += botMessage;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    document.getElementById("user-input").value = "";
}
