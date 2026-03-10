const chatBox = document.getElementById("chat-box");
const historyBox = document.getElementById("history-box");

function addMessage(role, text) {
  const div = document.createElement("div");
  div.className = role;
  div.innerText = `${role}: ${text}`;
  chatBox.appendChild(div);
}

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value;
  if (!message) return;

  addMessage("user", message);
  input.value = "";

  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ message })
  });

  const data = await res.json();
  addMessage("assistant", data.reply);
}

async function loadHistory() {
  historyBox.innerHTML = "<h3>Chat History</h3>";

  const res = await fetch("http://127.0.0.1:8000/history-by-date");
  const data = await res.json();

  for (const date in data) {
    const h = document.createElement("h4");
    h.innerText = date;
    historyBox.appendChild(h);

    data[date].forEach(m => {
      const p = document.createElement("p");
      p.innerText = `${m.role}: ${m.content}`;
      historyBox.appendChild(p);
    });
  }
}
