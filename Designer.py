import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai
import pyperclip 

genai.configure(api_key="AIzaSyBsCw7_w-E_RBq-hF2mI8p9t51fHbp8xdw")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
system_prompt = "Whenever someone enters a python code, you should design a simple UI in Python using tkinter. You should explain the code only in comments, it should be ready to run after copying"

def generate_response():
    user_input = input_field.get()
    if user_input.lower() == "bye":
        window.destroy()
        return
    query = system_prompt + " " + user_input
    response = model.generate_content(query)
    
    # Insert user and bot messages into output text area
    output_text.insert(tk.END, "You: " + user_input + "\n", "user")
    output_text.insert(tk.END, "Bot: " + response.text + "\n\n", "bot")
    
    # Display the generated code with the copy button
    copy_button.pack_forget()  # Hide the copy button if it's already there
    copy_button.pack(pady=5)   # Show the copy button when a response is ready
    generated_code.set(response.text)  # Set the code in the variable
    
    input_field.delete(0, tk.END)

# Function to copy the generated code to the clipboard
def copy_to_clipboard():
    pyperclip.copy(generated_code.get())  # Copy the generated code to clipboard

# Create main window with a robotic theme
window = tk.Tk()
window.title("Python UI Designer")
window.geometry("1200x900")
window.configure(bg="#2C2F33")  # Dark gray background for a robotic feel

# Customize fonts and colors for a futuristic, robotic look
label_font = ("Courier", 10, "bold")
button_font = ("Courier", 10)
output_font = ("Courier", 10)
input_bg = "#7289DA"  # Slightly robotic blue for input field
button_bg = "#99AAB5"  # Light gray for button

# Input label
input_label = tk.Label(window, text="Enter your Code:", font=label_font, fg="#99AAB5", bg="#2C2F33")
input_label.pack(pady=(10, 0))

# Input field
input_field = tk.Entry(window, width=90, font=output_font, bg=input_bg, fg="#FFFFFF", insertbackground="#FFFFFF")
input_field.pack(pady=5)

# Submit button
submit_button = tk.Button(window, text="Generate", command=generate_response, font=button_font, bg=button_bg, fg="#2C2F33")
submit_button.pack(pady=5)

# Output area with scroll
output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=140, height=28, font=output_font, bg="#23272A", fg="#FFFFFF", border=0)
output_text.pack(pady=10)
output_text.tag_config("user", foreground="#7289DA")  # Blue for user text
output_text.tag_config("bot", foreground="#99AAB5")   # Gray for bot text

# Variable to hold the generated code
generated_code = tk.StringVar()

# Copy button (initially hidden)
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, font=button_font, bg="#7289DA", fg="#2C2F33")

# Run the application
window.mainloop()