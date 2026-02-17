const cart = JSON.parse(localStorage.getItem("cart") || "[]");

document.querySelectorAll("button[data-id]").forEach((btn) => {
	btn.addEventListener("click", () => {
		const id = btn.dataset.id;
		const existing = cart.find((i) => i.id === id);
		if (existing) existing.qty += 1;
		else cart.push({ id, qty: 1 });
		localStorage.setItem("cart", JSON.stringify(cart));
		alert("Added to cart");
	});
});

document.getElementById("checkout").addEventListener("click", async () => {
	if (!cart.length) return alert("Cart is empty");

	const res = await fetch("/create-checkout-session", {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ cart }),
	});

	const { url } = await res.json();
	window.location.href = url;
});
