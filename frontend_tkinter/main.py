import tkinter as tk
from tkinter import ttk, messagebox
from db_connect import connect_db

# ---------- Certificate Verification ----------
def verify_certificate():
    cert_hash = entry_hash.get().strip()
    if cert_hash == placeholder_text or cert_hash == "":
        result_label.config(text="⚠️ Please enter a valid certificate hash.", fg="#ffcc00")
        return

    connection = connect_db()
    if connection is None:
        result_label.config(text="❌ Database connection failed.", fg="#ff4c4c")
        return

    cursor = connection.cursor()
    try:
        cursor.callproc("verify_certificate", [cert_hash])
        for result in cursor._stored_results:
            output = result.fetchall()
            if output:
                message = output[0][0]
                result_label.config(
                    text=message,
                    fg="#00ff99" if "VALID" in message else "#ffcc00" if "REVOKED" in message else "#ffaa00"
                )
            else:
                result_label.config(text="No response from procedure.", fg="#888888")
    except Exception as e:
        result_label.config(text=f"⚠️ Error: {e}", fg="#ff4c4c")
    finally:
        cursor.close()
        connection.close()

# ---------- Show All Certificates ----------
def show_all_certificates():
    connection = connect_db()
    if connection is None:
        messagebox.showerror("Connection Error", "Cannot connect to the database.")
        return

    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT c.cert_id, h.name, h.email, i.name, i.organization, c.cert_hash, c.issue_date, c.status 
            FROM certificate c
            JOIN holder h ON c.holder_id = h.holder_id
            JOIN issuer i ON c.issuer_id = i.issuer_id
            ORDER BY c.issue_date DESC;
        """)
        rows = cursor.fetchall()

        table.delete(*table.get_children())
        for row in rows:
            table.insert("", "end", values=row)

    except Exception as e:
        messagebox.showerror("Error", f"Error fetching certificates:\n{e}")
    finally:
        cursor.close()
        connection.close()

# ---------- Search Certificates by Email ----------
def search_by_email():
    email = search_entry.get().strip()
    if email == "" or email == email_placeholder:
        messagebox.showwarning("Input Error", "Please enter an email ID to search.")
        return

    connection = connect_db()
    if connection is None:
        messagebox.showerror("Connection Error", "Database connection failed.")
        return

    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT c.cert_id, h.name, h.email, i.name, i.organization, c.cert_hash, c.issue_date, c.status
            FROM certificate c
            JOIN holder h ON c.holder_id = h.holder_id
            JOIN issuer i ON c.issuer_id = i.issuer_id
            WHERE h.email = %s;
        """, (email,))
        rows = cursor.fetchall()

        table.delete(*table.get_children())
        if not rows:
            messagebox.showinfo("No Results", "No certificates found for this email.")
        else:
            for row in rows:
                table.insert("", "end", values=row)

    except Exception as e:
        messagebox.showerror("Error", f"Error searching data:\n{e}")
    finally:
        cursor.close()
        connection.close()

# ---------- Placeholder Handling ----------
def on_entry_click(event):
    if entry_hash.get() == placeholder_text:
        entry_hash.delete(0, "end")
        entry_hash.config(fg="white")

def on_focusout(event):
    if entry_hash.get() == "":
        entry_hash.insert(0, placeholder_text)
        entry_hash.config(fg="#777777")

def on_search_click(event):
    if search_entry.get() == email_placeholder:
        search_entry.delete(0, "end")
        search_entry.config(fg="white")

def on_search_focusout(event):
    if search_entry.get() == "":
        search_entry.insert(0, email_placeholder)
        search_entry.config(fg="#777777")

# ---------- UI Setup ----------
root = tk.Tk()
root.title("Digital Certificate Verification System")
root.geometry("1000x650")
root.configure(bg="#101010")
root.resizable(False, False)

# ---------- Title ----------
title = tk.Label(root, text="Digital Certificate Verification System",
                 font=("Segoe UI", 18, "bold"), bg="#101010", fg="#00ffff")
title.pack(pady=(20, 10))

# ---------- Verify Section ----------
frame_top = tk.Frame(root, bg="#101010")
frame_top.pack(pady=10)

tk.Label(frame_top, text="Enter Certificate Hash:", font=("Segoe UI", 12),
         bg="#101010", fg="#cccccc").pack()

placeholder_text = "e.g. HASH1234ABC"
entry_hash = tk.Entry(frame_top, font=("Consolas", 12), width=40, bg="#181818",
                      fg="#777777", insertbackground="white", relief="flat", justify="center")
entry_hash.pack(ipady=8, pady=5)
entry_hash.insert(0, placeholder_text)
entry_hash.bind("<FocusIn>", on_entry_click)
entry_hash.bind("<FocusOut>", on_focusout)

verify_btn = tk.Button(frame_top, text="VERIFY", font=("Segoe UI", 11, "bold"),
                       bg="#00b3b3", fg="white", width=20, relief="flat",
                       activebackground="#009999", activeforeground="white",
                       command=verify_certificate)
verify_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Segoe UI", 12, "bold"), bg="#101010",
                        fg="#cccccc", wraplength=700, justify="center")
result_label.pack(pady=5)

# ---------- Search Section ----------
search_frame = tk.Frame(root, bg="#101010")
search_frame.pack(pady=(10, 5))

email_placeholder = "Enter email ID to search certificates"
search_entry = tk.Entry(
    search_frame,
    font=("Consolas", 11),
    width=40,
    bg="#181818",
    fg="#777777",
    insertbackground="white",
    relief="flat",
    justify="center"
)
search_entry.insert(0, email_placeholder)
search_entry.bind("<FocusIn>", on_search_click)
search_entry.bind("<FocusOut>", on_search_focusout)
search_entry.grid(row=0, column=0, padx=10, ipady=6)

search_btn = tk.Button(
    search_frame,
    text="Search by Email",
    font=("Segoe UI", 10, "bold"),
    bg="#00b3b3",
    fg="white",
    width=18,
    relief="flat",
    activebackground="#009999",
    activeforeground="white",
    command=search_by_email
)
search_btn.grid(row=0, column=1, padx=5)

view_all_btn = tk.Button(
    search_frame,
    text="Show All Certificates",
    font=("Segoe UI", 10, "bold"),
    bg="#00b3b3",
    fg="white",
    width=20,
    relief="flat",
    activebackground="#009999",
    activeforeground="white",
    command=show_all_certificates
)
view_all_btn.grid(row=0, column=2, padx=5)

# ---------- Divider Line ----------
divider = tk.Frame(root, bg="#00b3b3", height=2, width=920)
divider.pack(pady=(8, 5))

# ---------- Table Section ----------
table_frame = tk.Frame(root, bg="#101010")
table_frame.pack(pady=(5, 10), fill="both", expand=True)

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background="#181818", foreground="white",
                rowheight=22, fieldbackground="#181818", bordercolor="#101010")
style.map("Treeview", background=[('selected', '#00b3b3')])

cols = ["Cert ID", "Holder Name", "Email", "Issuer", "Organization",
        "Cert Hash", "Issue Date", "Status"]
table = ttk.Treeview(table_frame, columns=cols, show="headings")
table.pack(fill="both", expand=True, padx=10, pady=5)

for col in cols:
    table.heading(col, text=col)
    table.column(col, anchor="center", width=120)

# ---------- Footer ----------
footer = tk.Label(root, text="Made with ❤️ by Swaroop Kumar",
                  font=("Segoe UI", 10), bg="#101010", fg="#666666")
footer.pack(side="bottom", pady=10)

# Load all certificates initially
show_all_certificates()

root.mainloop()
