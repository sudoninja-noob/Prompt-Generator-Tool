import tkinter as tk
from tkinter import messagebox, scrolledtext
import pyperclip

# Prompt templates
PROMPT_TEMPLATES = {
    "ChatGPT (General)": "Write a detailed and professional explanation about '{subject}'.",
    "Image Generation (AI Art)": "Create a realistic AI image prompt: '{subject}', cinematic lighting, 8K, ultra-detailed.",
    "SEO Blog Prompt": "Generate a blog post outline for the topic: '{subject}', optimized for SEO and readability.",
    "Resume Summary": "Craft a strong resume summary for someone with experience in '{subject}'.",
    "Cybersecurity Report": "Write a professional vulnerability report on '{subject}', covering risk and remediation.",
    "Bug Bounty Report": "Prepare a bug bounty report on '{subject}' including description, POC, and impact.",
    "Custom Prompt": "{subject}"
}

# Generate prompt function
def generate_prompt():
    category = category_var.get()
    subject = subject_entry.get().strip()

    if not subject:
        messagebox.showwarning("Missing Input", "Please enter a subject or keyword.")
        return

    template = PROMPT_TEMPLATES.get(category, "{subject}")
    result = template.format(subject=subject)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)
    pyperclip.copy(result)
    messagebox.showinfo("Prompt Ready", "Prompt copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("🧠 Prompt Generator Tool")
root.geometry("700x400")
root.configure(bg="#1e1e1e")

# Fonts & Colors
label_font = ("Segoe UI", 12)
entry_font = ("Segoe UI", 11)
text_font = ("Consolas", 11)

# Dropdown for category
tk.Label(root, text="Select Prompt Type:", bg="#1e1e1e", fg="white", font=label_font).pack(pady=5)
category_var = tk.StringVar(value="ChatGPT (General)")
tk.OptionMenu(root, category_var, *PROMPT_TEMPLATES.keys()).pack(pady=5)

# Subject entry
tk.Label(root, text="Enter Subject/Keyword:", bg="#1e1e1e", fg="white", font=label_font).pack(pady=5)
subject_entry = tk.Entry(root, width=50, font=entry_font)
subject_entry.pack(pady=5)

# Generate button
tk.Button(root, text="🚀 Generate Prompt", command=generate_prompt, bg="#4CAF50", fg="white", font=label_font).pack(pady=10)

# Result label and output box
tk.Label(root, text="Generated Prompt:", bg="#1e1e1e", fg="white", font=label_font).pack(pady=5)
result_text = scrolledtext.ScrolledText(root, height=6, width=80, font=text_font, wrap=tk.WORD, bg="#2e2e2e", fg="white", insertbackground="white")
result_text.pack(pady=5)

# Signature in bottom-right corner
signature = tk.Label(root, text="Made by Sudoninja", bg="#1e1e1e", fg="#888888", font=("Segoe UI", 9, "italic"))
signature.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

# Run GUI
root.mainloop()
