import customtkinter as ctk
from tkinter import messagebox

# -----------------------------
# Number System Converter (customTkinter GUI)
# -----------------------------
# Author: Sarvesh Halvadia
# Date: 25 May 2025
# Description: Convert numbers between Binary, Decimal, Octal, and Hexadecimal.
# ------------------------------------------------------------

class NumberConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Number System Converter")
        self.geometry("500x420")
        self.resizable(False, False)
        ctk.set_default_color_theme("blue")  # You can try "green", "dark-blue", etc.

        # Set background color
        self.configure(fg_color="#f0f4fa")

        # Title Label
        ctk.CTkLabel(
            self,
            text="Number System Converter",
            font=("Segoe UI Semibold", 22),
            text_color="#2563eb"
        ).pack(pady=(18, 8))

        # Main Frame
        main_frame = ctk.CTkFrame(self, corner_radius=18, fg_color="#d45252")
        main_frame.pack(padx=30, pady=10, fill="both", expand=True)

        # Input Section
        self.input_label = ctk.CTkLabel(main_frame, text="Enter Number:", font=("Segoe UI", 15))
        self.input_label.pack(pady=(18, 4))

        self.input_entry = ctk.CTkEntry(main_frame, width=320, font=("Segoe UI", 14))
        self.input_entry.pack(ipady=4, pady=(0, 10))

        # Base Selection
        self.base_var = ctk.StringVar(value="decimal")
        base_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        base_frame.pack(pady=8)

        bases = [
            ("Binary", "binary"),
            ("Decimal", "decimal"),
            ("Octal", "octal"),
            ("Hexadecimal", "hexadecimal"),
        ]
        for text, value in bases:
            ctk.CTkRadioButton(
                base_frame,
                text=text,
                variable=self.base_var,
                value=value,
                font=("Segoe UI", 12),
                radiobutton_height=18,
                radiobutton_width=18,
                border_color="#2563eb",
                fg_color="#2563eb",
                hover_color="#60a5fa"
            ).pack(side="left", padx=12)

        # Convert & Clear Buttons
        btn_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        btn_frame.pack(pady=12)

        ctk.CTkButton(
            btn_frame,
            text="Convert",
            command=self.convert,
            width=110,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            font=("Segoe UI Semibold", 13)
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            btn_frame,
            text="Clear",
            command=self.clear,
            width=110,
            fg_color="#64748b",
            hover_color="#334155",
            font=("Segoe UI Semibold", 13)
        ).pack(side="left", padx=10)

        # Output Labels
        self.output_vars = {
            "binary": ctk.StringVar(value="Binary: -"),
            "decimal": ctk.StringVar(value="Decimal: -"),
            "octal": ctk.StringVar(value="Octal: -"),
            "hexadecimal": ctk.StringVar(value="Hexadecimal: -"),
        }

        output_frame = ctk.CTkFrame(main_frame, fg_color="#f1f5f9", corner_radius=12)
        output_frame.pack(padx=18, pady=(10, 18), fill="x")

        for key in ["binary", "decimal", "octal", "hexadecimal"]:
            ctk.CTkLabel(
                output_frame,
                textvariable=self.output_vars[key],
                font=("Segoe UI", 13),
                text_color="#0f172a"
            ).pack(anchor="w", padx=18, pady=3)

    def convert(self):
        user_input = self.input_entry.get().strip()
        if not user_input:
            messagebox.showwarning("Input Error", "Please enter a number to convert.")
            return

        base = self.base_var.get()
        try:
            if base == "binary":
                number = int(user_input, 2)
            elif base == "decimal":
                number = int(user_input, 10)
            elif base == "octal":
                number = int(user_input, 8)
            elif base == "hexadecimal":
                number = int(user_input, 16)
            else:
                raise ValueError("Unknown base selected.")
        except ValueError:
            messagebox.showerror("Conversion Error", f"Invalid {base} number: {user_input}")
            return

        self.output_vars["binary"].set(f"Binary: {format(number, 'b')}")
        self.output_vars["decimal"].set(f"Decimal: {number}")
        self.output_vars["octal"].set(f"Octal: {format(number, 'o')}")
        self.output_vars["hexadecimal"].set(f"Hexadecimal: {format(number, 'X')}")

    def clear(self):
        self.input_entry.delete(0, "end")
        for key in self.output_vars:
            self.output_vars[key].set(f"{key.capitalize()}: -")

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # "Dark", "Light", or "System"
    app = NumberConverterApp()
    app.mainloop()
