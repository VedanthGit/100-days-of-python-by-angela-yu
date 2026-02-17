const form = document.getElementById("search-form");
const queryInput = document.getElementById("query");
const resultsDiv = document.getElementById("results");

form.addEventListener("submit", async (e) => {
	e.preventDefault();
	const q = queryInput.value.trim();
	if (!q) return;

	resultsDiv.innerHTML = `<p>Searching for "${q}" </p>`;

	try {
		const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
		const data = await res.json();
		renderResults(data);
	} catch (error) {
		resultsDiv.innerHTML = `<p>Error fetching data.</p>`;
	}
});

function renderResults(breweries) {
	if (!Array.isArray(breweries) || !breweries.length) {
		resultsDiv.innerHTML = `<p>No breweries found.</p>`;
		return;
	}

	resultsDiv.innerHTML = "";
	breweries.forEach((brew) => {
		const card = document.createElement("div");
		card.className = "brewery-card";

		card.innerHTML = `
            <h2>${brew.name}</h2>
            <div class="card-footer">
                <span>Type: ${brew.brewery_type || "N/A"}</span>
                <span>${brew.city}, ${brew.state}</span>
                ${brew.website_url ? `<a href="${brew.website_url}" target="_blank">Visit Website</a>` : ""}
                ${
									brew.latitude && brew.longitude
										? `<a href="https://www.google.com/maps/search/?api=1&query=${brew.latitude},${brew.longitude}" target="_blank">View on Map</a>`
										: ""
								}
                ${brew.phone ? `<span>☎️ ${brew.phone}</span>` : ""}
            </div>
        `;
		resultsDiv.appendChild(card);
	});
}
