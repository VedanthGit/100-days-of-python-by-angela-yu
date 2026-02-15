import tkinter as tk
import time
import random

SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed improves with focused daily practice.",
    "Clean code is better than clever code.",
    "Consistency beats motivation every single day.",
    "Build projects that solve real problems.",
]


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x400")

        self.start_time = None
        self.running = False
        self.target_text = random.choice(SENTENCES)

        self.title_label = tk.Label(
            root, text="Typing Speed Test", font=("Arial", 18, "bold")
        )
        self.title_label.pack(pady=10)

        self.text_label = tk.Label(
            root,
            text=self.target_text,
            wraplength=650,
            font=("Arial", 12),
            justify="center",
        )
        self.text_label.pack(pady=10)

        self.input_box = tk.Text(root, height=5, width=80, font=("Consolas", 11))
        self.input_box.pack(pady=10)
        self.input_box.bind("<KeyPress>", self.start_timer)
        self.input_box.bind("<KeyRelease>", self.check_completion)

        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

        self.reset_btn = tk.Button(root, text="Reset Test", command=self.reset_test)
        self.reset_btn.pack()

    def start_timer(self, event):
        if not self.running:
            self.running = True
            self.start_time = time.time()

    def check_completion(self, event):
        typed_text = self.input_box.get("1.0", "end-1c")

        if typed_text.strip() == self.target_text:
            elapsed_time = time.time() - self.start_time
            words = len(self.target_text.split())
            wpm = round((words / elapsed_time) * 60)

            accuracy = self.calculated_accuracy(typed_text, self.target_text)

            self.result_label.config(
                text=f"WPM: {wpm} | Accuracy: {accuracy}% | Time: {round(elapsed_time, 2)}s"
            )

            self.running = False

    def calculated_accuracy(self, typed, target):
        correct_chars = sum(1 for t, c in zip(typed, target) if t == c)
        accuracy = (correct_chars / len(target)) * 100
        return round(accuracy, 2)

    def reset_test(self):
        self.target_text = random.choice(SENTENCES)
        self.text_label.config(text=self.target_text)
        self.input_box.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.running = False
        self.start_time = None


def main():
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
