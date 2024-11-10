import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai
import pyperclip 

genai.configure(api_key="AIzaSyBsCw7_w-E_RBq-hF2mI8p9t51fHbp8xdw")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
system_prompt = "Whenever someone enters a python code, you should design a Beautiful UI in Python using PyQT5. You should not add any comments in the code. You should not explain it. You should not write anything except the python code, it should be ready to run after copying"

def generate_response():
    user_input = input_field.get()
    if user_input.lower() == "bye":
        window.destroy()
        return
    query = system_prompt + " " + user_input
    response = model.generate_content(query)
    
    output_text.insert(tk.END, "You: " + user_input + "\n", "user")
    output_text.insert(tk.END, "Bot: " + response.text + "\n\n", "bot")
    
    copy_button.pack_forget()  
    copy_button.pack(pady=5)   
    generated_code.set(response.text) 
    
    input_field.delete(0, tk.END)
    
def copy_to_clipboard():
    pyperclip.copy(generated_code.get())  
window = tk.Tk()
window.title("Python UI Designer")
window.geometry("1200x900")
window.configure(bg="#2C2F33")
label_font = ("Courier", 10, "bold")
button_font = ("Courier", 10)
output_font = ("Courier", 10)
input_bg = "#7289DA"  
button_bg = "#99AAB5" 

input_label = tk.Label(window, text="Enter your query:", font=label_font, fg="#99AAB5", bg="#2C2F33")
input_label.pack(pady=(10, 0))
input_field = tk.Entry(window, width=90, font=output_font, bg=input_bg, fg="#FFFFFF", insertbackground="#FFFFFF")
input_field.pack(pady=5)
submit_button = tk.Button(window, text="Submit", command=generate_response, font=button_font, bg=button_bg, fg="#2C2F33")
submit_button.pack(pady=5)
output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=140, height=28, font=output_font, bg="#23272A", fg="#FFFFFF", border=0)
output_text.pack(pady=10)
output_text.tag_config("user", foreground="#7289DA")
output_text.tag_config("bot", foreground="#99AAB5")   
generated_code = tk.StringVar()
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, font=button_font, bg="#7289DA", fg="#2C2F33")
window.mainloop()
