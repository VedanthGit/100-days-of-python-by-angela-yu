const form = document.getElementById("upload-form");
const palette = document.getElementById("palette");

form.addEventListener("submit", async (e) => {
	e.preventDefault();
	palette.innerHTML = "Processing…";

	const fileInput = document.getElementById("image");
	const data = new FormData();
	data.append("image", fileInput.files[0]);

	const res = await fetch("/api/extract", {
		method: "POST",
		body: data,
	});

	const json = await res.json();
	if (!res.ok) {
		palette.innerHTML = json.error || "Failed to extract colors";
		return;
	}

	renderPalette(json.colors);
});

function renderPalette(colors) {
	palette.innerHTML = "";
	colors.forEach((hex) => {
		const card = document.createElement("div");
		card.className = "swatch";
		card.innerHTML = `
      <div class="color" style="background:${hex}"></div>
      <div class="hex">
        <span>${hex}</span>
        <button class="copy" data-hex="${hex}">Copy</button>
      </div>
    `;
		palette.appendChild(card);
	});
}

palette.addEventListener("click", (e) => {
	if (e.target.classList.contains("copy")) {
		const hex = e.target.dataset.hex;
		navigator.clipboard.writeText(hex);
		e.target.textContent = "Copied";
		setTimeout(() => (e.target.textContent = "Copy"), 900);
	}
});
