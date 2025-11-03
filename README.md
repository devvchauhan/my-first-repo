# 💰 Micro-Loan Ledger & EMI Tracker

A simple **command-line Python application** for managing micro-loans and tracking EMIs.  
Designed for first-year students to practice **core Python concepts** like functions, loops, conditionals, dictionaries, sets, and lists.

---

## 🚀 Features
- 🔐 Password-protected login system  
- ➕ Add, view, update, and delete loan records  
- 👤 Track unique borrowers automatically using sets  
- 💵 Calculate EMI for each loan based on user input  
- 📊 Generate loan reports (summary, borrowers, and payments)  
- 🧮 Phase 1 uses in-memory data (temporary storage)

---

## 🧠 Learning Objectives
- Data structures (lists, tuples, sets, dictionaries)  
- Modular programming with functions  
- CRUD (Create, Read, Update, Delete) operations  
- Program control using loops and conditionals  
- Data persistence concepts (for future MySQL phase)

---

## ⚙️ How It Works
1. Run the program  
2. Enter the password to access the menu  
3. Choose an option to:
   - Add a new loan  
   - View loan details  
   - Modify existing loans  
   - Delete a loan  
   - Generate reports  
4. Continue until you choose to exit

---

## 🧩 Tech Stack
- **Language:** Python 3  
- **Phase 1:** In-memory storage  
- **Phase 2 (Future):** MySQL database integration

---

## 📈 Future Enhancements
- Database persistence using MySQL  
- EMI overdue detection  
- Enhanced reporting and analytics  
- GUI or web-based dashboard

---

## 👩‍💻 Example Data Structures

```python
# Loans stored in a dictionary
loans = {
    1: ("Ravi Sharma", 10000, 10, 12, 879.16)
}

# Borrower names stored in a set
borrowers = {"Ravi Sharma"}

# Payment records stored in a list
payments = [(1, 1, 879.16, "2025-11-03")]

---

🧾 Author
Dev Chauhan
