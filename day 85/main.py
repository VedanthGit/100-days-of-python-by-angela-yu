import tkinter as tk
from tkinter import Image, filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarker")
        self.root.geometry("420x300")
        self.image = None

        self.title = tk.Label(
            root, text="Image Watermarker", font=("Arial", 16, "bold")
        )
        self.title.pack(pady=10)

        self.upload_btn = tk.Button(
            root, text="Upload Image", command=self.upload_image
        )
        self.upload_btn.pack(pady=5)

        self.watermark_label = tk.Label(root, text="Watermark Text:")
        self.watermark_label.pack()

        self.watermark_entry = tk.Entry(root, width=30)
        self.watermark_entry.pack(pady=5)

        self.opacity_label = tk.Label(root, text="Opacity (0.1 - 1.0):")
        self.opacity_label.pack()

        self.opacity_entry = tk.Entry(root, width=10)
        self.opacity_entry.insert(0, "0.5")
        self.opacity_entry.pack(pady=5)

        self.apply_btn = tk.Button(
            root, text="Apply Watermark", command=self.apply_watermark
        )
        self.apply_btn.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
        )
        if file_path:
            self.image = Image.open(file_path).convert("RGBA")
            messagebox.showinfo("Success", "Image uploaded successfully.")

    def apply_watermark(self):
        if not self.image:
            messagebox.showerror("Error", "Please upload an image first.")
            return

        text = self.watermark_entry.get().strip()
        if not text:
            messagebox.showerror("Error", "Watermark text cannot be empty.")
            return

        try:
            opacity = float(self.opacity_entry.get())
            if not (0.1 <= opacity <= 1.0):
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Error", "Opacity must be a number between 0.1 and 1.0."
            )
            return

        watermark_layer = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark_layer)

        try:
            font = ImageFont.truetype("arial.ttf", size=int(self.image.size[0] / 20))
        except:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = self.image.size[0] - text_width - 20
        y = self.image.size[1] - text_height - 20

        draw.text((x, y), text, fill=(255, 255, 255, int(255 * opacity)), font=font)

        combined = Image.alpha_composite(self.image, watermark_layer)

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")],
        )

        if save_path:
            combined.convert("RGB").save(save_path)
            messagebox.showinfo("Success", "Watermarked image saved successfully.")


def main():
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
