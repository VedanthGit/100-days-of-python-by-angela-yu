const cafesEl = document.getElementById("cafes");
const searchEl = document.getElementById("search");
const addBtn = document.getElementById("add");

let cafes = [];

async function fetchCafes() {
	const res = await fetch("/api/cafes");
	cafes = await res.json();
	render(cafes);
}

function render(list) {
	cafesEl.innerHTML = "";
	list.forEach((c) => {
		const div = document.createElement("div");
		div.className = "card";
		div.innerHTML = `
      <h3>${c.name} — ${c.city}</h3>
      <p>Seats: ${c.seats}</p>
      <div>
        ${c.has_wifi ? `<span class="badge wifi">Wi-Fi</span>` : ""}
        ${c.has_power ? `<span class="badge power">Power</span>` : ""}
      </div>
      <p><a href="${c.map_url}" target="_blank">Open in Maps</a></p>
    `;
		cafesEl.appendChild(div);
	});
}

searchEl.addEventListener("input", (e) => {
	const q = e.target.value.toLowerCase();
	render(
		cafes.filter(
			(c) =>
				c.name.toLowerCase().includes(q) || c.city.toLowerCase().includes(q),
		),
	);
});

addBtn.addEventListener("click", async () => {
	const payload = {
		name: document.getElementById("name").value.trim(),
		city: document.getElementById("city").value.trim(),
		seats: Number(document.getElementById("seats").value || 0),
		map_url: document.getElementById("map").value.trim(),
		has_wifi: document.getElementById("wifi").checked,
		has_power: document.getElementById("power").checked,
	};

	const res = await fetch("/api/cafes", {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify(payload),
	});

	if (res.ok) {
		await fetchCafes();
		["name", "city", "seats", "map"].forEach(
			(id) => (document.getElementById(id).value = ""),
		);
		document.getElementById("wifi").checked = false;
		document.getElementById("power").checked = false;
	} else {
		alert("Invalid input");
	}
});

fetchCafes();
