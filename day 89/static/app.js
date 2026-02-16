const listEl = document.getElementById("list");
const form = document.getElementById("form");
const titleInput = document.getElementById("title");
const filterBtns = document.querySelectorAll(".filters button");

let todos = [];
let filter = "all";

async function fetchTodos() {
	const res = await fetch("/api/todos");
	todos = await res.json();
	render();
}

function render() {
	listEl.innerHTML = "";
	let view = todos;
	if (filter === "active") view = todos.filter((t) => !t.completed);
	if (filter === "completed") view = todos.filter((t) => t.completed);

	view.forEach((t) => {
		const li = document.createElement("li");
		if (t.completed) li.classList.add("completed");

		li.innerHTML = `
      <span>${t.title}</span>
      <div class="actions">
        <button data-toggle="${t.id}">${t.completed ? "Undo" : "Done"}</button>
        <button data-del="${t.id}">Delete</button>
      </div>
    `;

		listEl.appendChild(li);
	});
}

form.addEventListener("submit", async (e) => {
	e.preventDefault();
	const title = titleInput.value.trim();
	if (!title) return;

	const res = await fetch("/api/todos", {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ title }),
	});

	if (res.ok) {
		titleInput.value = "";
		await fetchTodos();
	}
});

listEl.addEventListener("click", async (e) => {
	const id = e.target.dataset.toggle || e.target.dataset.del;
	if (!id) return;

	if (e.target.dataset.toggle) {
		await fetch(`/api/todos/${id}`, { method: "PATCH" });
	}
	if (e.target.dataset.del) {
		await fetch(`/api/todos/${id}`, { method: "DELETE" });
	}

	fetchTodos();
});

filterBtns.forEach((btn) => {
	btn.addEventListener("click", () => {
		filterBtns.forEach((b) => b.classList.remove("active"));
		btn.classList.add("active");
		filter = btn.dataset.filter;
		render();
	});
});

fetchTodos();
