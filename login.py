import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib


# ============================================================
# COLORS
# ============================================================

BG = "#080D18"
CARD = "#121D30"
CARD2 = "#18253A"
BORDER = "#283A55"

WHITE = "#F8FAFC"
TEXT = "#E2E8F0"
MUTED = "#94A3B8"

BLUE = "#38BDF8"
BLUE_DARK = "#0284C7"
GREEN = "#34D399"
RED = "#FB7185"
PURPLE = "#A78BFA"


# ============================================================
# DATABASE
# ============================================================

DATABASE = "users.db"


def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# ============================================================
# PASSWORD HASH
# ============================================================

def hash_password(password):

    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


# ============================================================
# LOGIN APPLICATION
# ============================================================

class LoginApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "RESUMIND AI | Login"
        )

        self.root.geometry(
            "1100x700"
        )

        self.root.minsize(
            900,
            600
        )

        self.root.configure(
            bg=BG
        )

        self.show_login()

    # ========================================================
    # CLEAR WINDOW
    # ========================================================

    def clear_window(self):

        for widget in self.root.winfo_children():

            widget.destroy()

    # ========================================================
    # LOGIN PAGE
    # ========================================================

    def show_login(self):

        self.clear_window()

        self.root.configure(
            bg=BG
        )

        # Main container
        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            fill="both",
            expand=True
        )

        # ====================================================
        # LEFT BRANDING
        # ====================================================

        left = tk.Frame(
            main,
            bg=SIDEBAR
        )

        left.pack(
            side="left",
            fill="both",
            expand=True
        )

        tk.Label(
            left,
            text="◈",
            font=(
                "Segoe UI",
                60,
                "bold"
            ),
            fg=BLUE,
            bg=SIDEBAR
        ).pack(
            pady=(120, 0)
        )

        tk.Label(
            left,
            text="RESUMIND",
            font=(
                "Segoe UI",
                30,
                "bold"
            ),
            fg=WHITE,
            bg=SIDEBAR
        ).pack(
            pady=(5, 0)
        )

        tk.Label(
            left,
            text="AI CAREER INTELLIGENCE",
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            fg=MUTED,
            bg=SIDEBAR
        ).pack(
            pady=(2, 25)
        )

        tk.Label(
            left,
            text=(
                "Analyze your resume.\n"
                "Discover your strengths.\n"
                "Build your career."
            ),
            font=(
                "Segoe UI",
                14
            ),
            fg=TEXT,
            bg=SIDEBAR,
            justify="center"
        ).pack(
            pady=15
        )

        tk.Label(
            left,
            text="✦  ATS Analysis     ✦  Skill Intelligence\n"
                 "✦  Career Matching  ✦  Resume Insights",
            font=(
                "Segoe UI",
                9
            ),
            fg=BLUE,
            bg=SIDEBAR,
            justify="center"
        ).pack(
            pady=30
        )

        # ====================================================
        # RIGHT LOGIN AREA
        # ====================================================

        right = tk.Frame(
            main,
            bg=BG
        )

        right.pack(
            side="right",
            fill="both",
            expand=True
        )

        login_card = tk.Frame(
            right,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        login_card.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=430,
            height=500
        )

        tk.Label(
            login_card,
            text="Welcome Back 👋",
            font=(
                "Segoe UI",
                24,
                "bold"
            ),
            fg=WHITE,
            bg=CARD
        ).pack(
            pady=(45, 5)
        )

        tk.Label(
            login_card,
            text="Sign in to continue to your dashboard",
            font=(
                "Segoe UI",
                9
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            pady=(0, 30)
        )

        # ====================================================
        # EMAIL
        # ====================================================

        tk.Label(
            login_card,
            text="EMAIL",
            font=(
                "Segoe UI",
                8,
                "bold"
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=45
        )

        self.email_entry = tk.Entry(
            login_card,
            bg=CARD2,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            font=(
                "Segoe UI",
                11
            )
        )

        self.email_entry.pack(
            fill="x",
            padx=45,
            ipady=10,
            pady=(6, 18)
        )

        # ====================================================
        # PASSWORD
        # ====================================================

        tk.Label(
            login_card,
            text="PASSWORD",
            font=(
                "Segoe UI",
                8,
                "bold"
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=45
        )

        password_frame = tk.Frame(
            login_card,
            bg=CARD2
        )

        password_frame.pack(
            fill="x",
            padx=45,
            pady=(6, 18)
        )

        self.password_entry = tk.Entry(
            password_frame,
            bg=CARD2,
            fg=WHITE,
            insertbackground=WHITE,
            show="•",
            relief="flat",
            font=(
                "Segoe UI",
                11
            )
        )

        self.password_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=10,
            padx=(8, 0)
        )

        self.show_password = False

        self.eye_button = tk.Button(
            password_frame,
            text="◉",
            command=self.toggle_password,
            bg=CARD2,
            fg=MUTED,
            activebackground=CARD2,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            cursor="hand2"
        )

        self.eye_button.pack(
            side="right",
            padx=10
        )

        # ====================================================
        # LOGIN BUTTON
        # ====================================================

        tk.Button(
            login_card,
            text="LOGIN",
            command=self.login,
            bg=BLUE_DARK,
            fg=WHITE,
            activebackground=BLUE,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            font=(
                "Segoe UI",
                10,
                "bold"
            ),
            cursor="hand2"
        ).pack(
            fill="x",
            padx=45,
            ipady=11
        )

        # ====================================================
        # SIGNUP
        # ====================================================

        signup_frame = tk.Frame(
            login_card,
            bg=CARD
        )

        signup_frame.pack(
            pady=25
        )

        tk.Label(
            signup_frame,
            text="Don't have an account?",
            font=(
                "Segoe UI",
                9
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            side="left"
        )

        tk.Button(
            signup_frame,
            text="Create Account",
            command=self.show_signup,
            bg=CARD,
            fg=BLUE,
            activebackground=CARD,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            cursor="hand2"
        ).pack(
            side="left",
            padx=5
        )

        tk.Label(
            login_card,
            text="Secure account • SQLite database",
            font=(
                "Segoe UI",
                7
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            side="bottom",
            pady=15
        )

        self.email_entry.focus()

        self.root.bind(
            "<Return>",
            lambda event: self.login()
        )

    # ========================================================
    # SIGNUP PAGE
    # ========================================================

    def show_signup(self):

        self.clear_window()

        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            fill="both",
            expand=True
        )

        card = tk.Frame(
            main,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=470,
            height=590
        )

        tk.Label(
            card,
            text="Create Account",
            font=(
                "Segoe UI",
                25,
                "bold"
            ),
            fg=WHITE,
            bg=CARD
        ).pack(
            pady=(38, 5)
        )

        tk.Label(
            card,
            text="Create your Resumind AI profile",
            font=(
                "Segoe UI",
                9
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            pady=(0, 25)
        )

        # ====================================================
        # NAME
        # ====================================================

        tk.Label(
            card,
            text="FULL NAME",
            font=(
                "Segoe UI",
                8,
                "bold"
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=50
        )

        self.name_entry = tk.Entry(
            card,
            bg=CARD2,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            font=(
                "Segoe UI",
                11
            )
        )

        self.name_entry.pack(
            fill="x",
            padx=50,
            ipady=10,
            pady=(6, 15)
        )

        # ====================================================
        # EMAIL
        # ====================================================

        tk.Label(
            card,
            text="EMAIL",
            font=(
                "Segoe UI",
                8,
                "bold"
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=50
        )

        self.signup_email_entry = tk.Entry(
            card,
            bg=CARD2,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            font=(
                "Segoe UI",
                11
            )
        )

        self.signup_email_entry.pack(
            fill="x",
            padx=50,
            ipady=10,
            pady=(6, 15)
        )

        # ====================================================
        # PASSWORD
        # ====================================================

        tk.Label(
            card,
            text="PASSWORD",
            font=(
                "Segoe UI",
                8,
                "bold"
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=50
        )

        self.signup_password_entry = tk.Entry(
            card,
            bg=CARD2,
            fg=WHITE,
            insertbackground=WHITE,
            show="•",
            relief="flat",
            font=(
                "Segoe UI",
                11
            )
        )

        self.signup_password_entry.pack(
            fill="x",
            padx=50,
            ipady=10,
            pady=(6, 15)
        )

        # ====================================================
        # CONFIRM PASSWORD
        # ====================================================

        tk.Label(
            card,
            text="CONFIRM PASSWORD",
            font=(
                "Segoe UI",
                8,
                "bold"
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=50
        )

        self.confirm_password_entry = tk.Entry(
            card,
            bg=CARD2,
            fg=WHITE,
            insertbackground=WHITE,
            show="•",
            relief="flat",
            font=(
                "Segoe UI",
                11
            )
        )

        self.confirm_password_entry.pack(
            fill="x",
            padx=50,
            ipady=10,
            pady=(6, 20)
        )

        # ====================================================
        # CREATE ACCOUNT
        # ====================================================

        tk.Button(
            card,
            text="CREATE ACCOUNT",
            command=self.signup,
            bg=GREEN,
            fg="#052E1C",
            activebackground="#6EE7B7",
            activeforeground="#052E1C",
            relief="flat",
            bd=0,
            font=(
                "Segoe UI",
                10,
                "bold"
            ),
            cursor="hand2"
        ).pack(
            fill="x",
            padx=50,
            ipady=11
        )

        # ====================================================
        # BACK TO LOGIN
        # ====================================================

        back_frame = tk.Frame(
            card,
            bg=CARD
        )

        back_frame.pack(
            pady=25
        )

        tk.Label(
            back_frame,
            text="Already have an account?",
            font=(
                "Segoe UI",
                9
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            side="left"
        )

        tk.Button(
            back_frame,
            text="Login",
            command=self.show_login,
            bg=CARD,
            fg=BLUE,
            activebackground=CARD,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            cursor="hand2"
        ).pack(
            side="left",
            padx=5
        )

        self.name_entry.focus()

    # ========================================================
    # TOGGLE PASSWORD
    # ========================================================

    def toggle_password(self):

        if self.show_password:

            self.password_entry.config(
                show="•"
            )

            self.show_password = False

        else:

            self.password_entry.config(
                show=""
            )

            self.show_password = True

    # ========================================================
    # SIGNUP
    # ========================================================

    def signup(self):

        name = self.name_entry.get().strip()
        email = self.signup_email_entry.get().strip()
        password = self.signup_password_entry.get()
        confirm = self.confirm_password_entry.get()

        if not name:

            messagebox.showwarning(
                "Missing Name",
                "Please enter your full name."
            )

            return

        if not email:

            messagebox.showwarning(
                "Missing Email",
                "Please enter your email."
            )

            return

        if "@" not in email or "." not in email:

            messagebox.showwarning(
                "Invalid Email",
                "Please enter a valid email address."
            )

            return

        if len(password) < 6:

            messagebox.showwarning(
                "Weak Password",
                "Password must contain at least 6 characters."
            )

            return

        if password != confirm:

            messagebox.showerror(
                "Password Error",
                "Passwords do not match."
            )

            return

        password_hash = hash_password(
            password
        )

        try:

            connection = sqlite3.connect(
                DATABASE
            )

            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO users
                (name, email, password)
                VALUES (?, ?, ?)
                """,
                (
                    name,
                    email,
                    password_hash
                )
            )

            connection.commit()

            connection.close()

            messagebox.showinfo(
                "Account Created",
                "Your account has been created successfully!\n\n"
                "You can now login."
            )

            self.show_login()

            self.email_entry.insert(
                0,
                email
            )

        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Account Exists",
                "An account with this email already exists."
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # ========================================================
    # LOGIN
    # ========================================================

    def login(self):

        email = self.email_entry.get().strip()
        password = self.password_entry.get()

        if not email:

            messagebox.showwarning(
                "Missing Email",
                "Please enter your email."
            )

            return

        if not password:

            messagebox.showwarning(
                "Missing Password",
                "Please enter your password."
            )

            return

        password_hash = hash_password(
            password
        )

        try:

            connection = sqlite3.connect(
                DATABASE
            )

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, name, email
                FROM users
                WHERE email = ?
                AND password = ?
                """,
                (
                    email,
                    password_hash
                )
            )

            user = cursor.fetchone()

            connection.close()

            if user:

                user_id = user[0]
                name = user[1]
                user_email = user[2]

                messagebox.showinfo(
                    "Login Successful",
                    f"Welcome back, {name}! 👋"
                )

                self.open_dashboard(
                    user_id,
                    name,
                    user_email
                )

            else:

                messagebox.showerror(
                    "Login Failed",
                    "Incorrect email or password."
                )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # ========================================================
    # OPEN DASHBOARD
    # ========================================================

    def open_dashboard(
        self,
        user_id,
        name,
        email
    ):

        self.root.destroy()

        import main

        new_root = tk.Tk()

        app = main.ResumeAnalyzerApp(
            new_root
        )

        # Store logged-in user details
        app.user_id = user_id
        app.user_name = name
        app.user_email = email

        new_root.mainloop()


# ============================================================
# CONSTANT
# ============================================================

SIDEBAR = "#0D1627"


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    create_database()

    root = tk.Tk()

    LoginApp(
        root
    )

    root.mainloop()