import tkinter as tk
from tkinter import filedialog
import csv
import smtplib
from tkinter import messagebox
import os
class EmailBotGUI:
    
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        '''Please Setup your Gmail for Bulk sending.'''
        self.smtp_username = "Your Email Address Here"
        # for More Security please use environment Variables : 
        # self.smtp_password = os.environ.get('PASS')
        self.smtp_password = "Password Here"
        self.email_list = []
        self.subject = ""
        self.message = ""
        self.count= 1

        self.root = tk.Tk()
        self.root.title("Email Bot by Huzaifa Antule")
        self.root.geometry("480x500")
        
        # Create the UI elements

        tk.Label(self.root, text="Email From :").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text=self.smtp_username).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Subject :").grid(row=1, column=0, padx=10, pady=10)
        self.subject_entry = tk.Entry(self.root,width=40)
        self.subject_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="To :").grid(row=2, column=0, padx=10, pady=10)
        self.to_entry = tk.Entry(self.root, width=40)

        tk.Label(self.root, text="Message :").grid(row=3, column=0, padx=10, pady=10)
        self.message_text = tk.Text(self.root, height=5, width=30)
        self.message_text.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Email Address :").grid(row=4, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(self.root, width=40)
        self.email_entry.grid(row=4, column=1, padx=10, pady=10)
        
        tk.Button(self.root, text="Add", command=self.add_email).grid(row=4, column=2, padx=5, pady=10)
        self.email_listbox = tk.Listbox(self.root, width=40,height=5)
        self.email_listbox.grid(row=5, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Remove", command=self.remove_email).grid(row=5, column=2, padx=5, pady=10)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_emails)
        self.send_button.grid(row=6, column=1, padx=10, pady=10)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_inputs)
        self.clear_button.grid(row=6, column=2, padx=10, pady=10)
         # Create the back button and configure it to go back to the main GUI
        tk.Button(self.root, text="Back", command=self.back_to_main_gui).grid(row=10, column=0, padx=10, pady=10)

    def back_to_main_gui(self):
        # Unhide the main GUI and destroy the current GUI
        self.root.withdraw()
        main_gui = MainGUI(tk.Tk())
        main_gui.root.mainloop()

    def clear_inputs(self):
        self.email_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.email_listbox.delete(0,tk.END)
        self.message_text.delete("1.0", tk.END)
        self.display_message("All Fields Are Cleared.")

    def add_email(self):
        email = self.email_entry.get()
        if email:
            self.email_list.append(email)
            self.email_listbox.insert(tk.END,f"- {email}")
            self.email_entry.delete(0, tk.END)
            self.count +=1
            self.display_message(f"{email} added to the email list")
        else:
            self.display_message("Please enter an email address.")

    def remove_email(self):
        selection = self.email_listbox.curselection()
        if selection:
            index = selection[0]
            email_with_dash = self.email_listbox.get(index)
            email = email_with_dash[2:]  # remove the "-" character from the email
            self.email_listbox.delete(index)
            self.email_list.remove(email)
            self.count -=1
            self.display_message(f"{email} removed from the email list")
        else:
            self.display_message( "Please select an email address to remove.")

    def send_emails(self):
     try:
        if not self.email_list:
            self.display_message("Please add at least one email address.")
            return
        smtp_connection = smtplib.SMTP(self.smtp_server, self.smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(self.smtp_username, self.smtp_password)
        # Get the subject
        from_email_address = self.smtp_username
        email_subject = self.subject_entry.get()
        email_message = self.message_text.get("1.0", "end-1c")
        # Loop through the email list and send emails to them
        for email in self.email_list:
            # Set up email message
            message = f"From: {from_email_address}\nTo: {email}\nSubject: {email_subject}\n\n{email_message}"
            smtp_connection.sendmail(self.smtp_username, email, message)
        # Close the SMTP connection
        smtp_connection.quit()
        self.display_message("Emails sent successfully!")
     except smtplib.SMTPException as e:
        self.display_message(f"An error occurred while sending emails: {str(e)}")
    def display_message(self, message):
    # Create a label widget for the message
                message_label = tk.Label(self.root, text=message)
                message_label.grid(row=7, column=1, padx=10, pady=10)
    # Update the label text after 3 seconds
                self.root.after(2000, message_label.config, {"text": ""})
class EmailBotGUI_2:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.smtp_username = "businesswork836@gmail.com"
        self.smtp_password = os.environ.get('PASS')
        self.subject = ""
        self.message = ""
        self.root = tk.Tk()
        self.root.title("Email Bot by Huzaifa Antule ")
        self.root.geometry("480x450")

        tk.Label(self.root, text="Email From :").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text=self.smtp_username).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Subject :").grid(row=1, column=0, padx=10, pady=10)
        self.subject_entry = tk.Entry(self.root,width=40)
        self.subject_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Message :").grid(row=2, column=0, padx=10, pady=10)
        self.message_text = tk.Text(self.root, height=8, width=30)
        self.message_text.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Upload CSV File :").grid(row=3, column=0, padx=10, pady=10)
        self.csv_file_path = tk.Entry(self.root, width=40)
        self.csv_file_path.grid(row=3, column=1, padx=10, pady=10)

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=3, column=2, padx=10, pady=10)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_email)
        self.send_button.grid(row=4, column=1, padx=10, pady=10)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=4, column=2, padx=10, pady=10)
         # Create the back button and configure it to go back to the main GUI
        tk.Button(self.root, text="Back", command=self.back_to_main_gui).grid(row=5, column=0, padx=10, pady=10)

    def back_to_main_gui(self):
        # Unhide the main GUI and destroy the current GUI
        self.root.withdraw()
        main_gui = MainGUI(tk.Tk())
        main_gui.root.mainloop()
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.csv_file_path.delete(0, tk.END)
        self.csv_file_path.insert(0, file_path)
    def send_email(self):
     try:
        from_email_address = self.smtp_username
        email_subject = self.subject_entry.get()
        email_message = self.message_text.get("1.0", "end-1c")
        csv_file = self.csv_file_path.get()
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            email_addresses = [row[0] for row in reader]
        for email_address in email_addresses:
            message = f"From: {from_email_address}\nTo: {email_address}\nSubject: {email_subject}\n\n{email_message}"
            try:
                smtpObj = smtplib.SMTP(self.smtp_server, self.smtp_port)
                smtpObj.starttls()
                smtpObj.login(self.smtp_username, self.smtp_password)
                smtpObj.sendmail(from_email_address, email_address, message)
                smtpObj.quit()
            except smtplib.SMTPException as e:
                pass
        self.display_message("Success .. Emails sent successfully!")
     except Exception as e:
        self.display_message(f"An Error :{str(e)}")
  
    def clear_fields(self):
        self.subject_entry.delete(0, tk.END)
        self.csv_file_path.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)
    def display_message(self, message):
    # Create a label widget for the message
                message_label = tk.Label(self.root, text=message)
                message_label.grid(row=7, column=1, padx=10, pady=10)
    # Update the label text after 3 seconds
                self.root.after(2000, message_label.config, {"text": ""})

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Bot by Huzaifa Antule")
        self.root.geometry("400x450")
        # # Create the options buttons
        tk.Label(self.root,text="Welcome to Email Bot", font=("Arial", 18)).pack(pady=40)
        tk.Label(self.root,text="Select an option :").pack(pady=20)
        tk.Button(self.root, text="Send Manually", command=self.option1).pack(pady=10)
        tk.Button(self.root, text="Send From CSV", command=self.option2).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.option3).pack(pady=10)

    def option1(self):
        self.root.withdraw()
        email_bot_gui = EmailBotGUI()
        email_bot_gui
        # self.root.wait_window(email_bot_gui.root)

    def option2(self):
        self.root.withdraw()
        email_bot_gui = EmailBotGUI_2()
        email_bot_gui
        # self.root.wait_window(email_bot_gui.root)

    def option3(self):
        self.root.quit
        self.root.destroy()
if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()