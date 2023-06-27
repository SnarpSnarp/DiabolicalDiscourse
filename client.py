import customtkinter
import loginauth from loginauth.py

#Set apperances
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

#Set size
root = customtkinter.CTk()
root.geometry("1000x600")

global frame  # Declare 'frame' as global during creation
frame = customtkinter.CTkFrame(root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame, text="Diabolical Login")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="OTP", show="*")
entry3.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=loginauth) 
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)

root.mainloop()