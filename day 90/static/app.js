const editor = document.getElementById("editor");
const timerEl = document.getElementById("timer");
const wordsEl = document.getElementById("words");
const resetBtn = document.getElementById("reset");

const TIMEOUT_MS = 5000; // 5 seconds of inactivity
let lastTypeAt = Date.now();
let interval = null;

function wordCount(text) {
	const trimmed = text.trim();
	if (!trimmed) return 0;
	return trimmed.split(/\s+/).length;
}

function updateStatus() {
	const elapsed = Date.now() - lastTypeAt;
	const remaining = Math.max(0, (TIMEOUT_MS - elapsed) / 1000);
	timerEl.textContent = `${remaining.toFixed(1)}s`;
	wordsEl.textContent = `${wordCount(editor.value)} words`;

	if (elapsed >= TIMEOUT_MS) {
		editor.value = "";
		wordsEl.textContent = "0 words";
		lastTypeAt = Date.now(); // reset timer after wipe
		alert("You stopped. Your work is gone.");
	}
}

editor.addEventListener("input", () => {
	lastTypeAt = Date.now();
	if (!interval) {
		interval = setInterval(updateStatus, 100);
	}
});

resetBtn.addEventListener("click", () => {
	editor.value = "";
	lastTypeAt = Date.now();
	wordsEl.textContent = "0 words";
});

setInterval(updateStatus, 100);
