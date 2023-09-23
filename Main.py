import tkinter as tk
import smtplib
from tkinter import messagebox

def send_email():
    try:
        # Get user inputs from the GUI
        sender_email = entry_sender.get()
        password = entry_password.get()
        recipient_email = entry_recipient.get()
        subject = entry_subject.get()
        message = text_message.get("1.0", tk.END)

        # Connect to the SMTP server (e.g., for Gmail)
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to the email account
        server.login(sender_email, password)

        # Create the email message
        email_message = f'Subject: {subject}\n\n{message}'

        # Send the email
        server.sendmail(sender_email, recipient_email, email_message)

        # Close the SMTP server
        server.quit()

        # Display a success message
        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the GUI window
window = tk.Tk()
window.title("Email Application")

# Labels and Entry fields for email details
label_sender = tk.Label(window, text="Sender Email:")
entry_sender = tk.Entry(window)
label_password = tk.Label(window, text="Password:")
entry_password = tk.Entry(window, show="*")
label_recipient = tk.Label(window, text="Recipient Email:")
entry_recipient = tk.Entry(window)
label_subject = tk.Label(window, text="Subject:")
entry_subject = tk.Entry(window)
label_message = tk.Label(window, text="Message:")
text_message = tk.Text(window, height=5, width=30)

# Send button
send_button = tk.Button(window, text="Send Email", command=send_email)

# Layout the GUI elements
label_sender.pack()
entry_sender.pack()
label_password.pack()
entry_password.pack()
label_recipient.pack()
entry_recipient.pack()
label_subject.pack()
entry_subject.pack()
label_message.pack()
text_message.pack()
send_button.pack()

# Start the GUI application
window.mainloop()
