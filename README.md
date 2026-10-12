# 💻 Laptop Management System

### NET LEGENT LAPTOP STORE | Python CLI Project

A **console-based laptop store and billing project** developed using core Python. Users can browse laptop brands, select a model, view its specifications and listed price, and generate a text-file bill using the customer's name.

## ✨ Features

- **9 laptop brand menus:** HP, Dell, Lenovo, MacBook, ASUS, Acer, MSI, Samsung, and Microsoft.
- **Model selection:** Choose from multiple models under each brand.
- **Laptop details:** Displays brand, model, screen size, CPU information, and price.
- **Customer billing:** Requests the customer's name and saves a `.txt` bill containing the laptop details and price.
- **Menu-based navigation:** Repeat the selection process or exit the program.
- **Basic input handling:** Includes exception handling for some invalid numeric inputs.

> **Note:** This is a learning project with hard-coded product information and prices. It does not currently provide a database, inventory tracking, a graphical interface, or real payment processing.

## 🛠️ Tech Stack

- **Language:** Python 3
- **Interface:** Command-line / terminal
- **Storage:** Plain-text (`.txt`) bills
- **Dependencies:** Python standard library only; no third-party packages required

## 📁 Project Structure

```text
Laptop-Management-System/
├── evaluation.py      # Main Python application
└── README.md          # Project documentation
```

Bill files are generated in the working directory when a customer completes a selection.

## 🚀 Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/sagarmeena004/Laptop-Management-System.git
   ```

2. Open the project directory:

   ```bash
   cd Laptop-Management-System
   ```

3. Run the program:

   ```bash
   python evaluation.py
   ```

   On some systems, use `python3 evaluation.py` instead.

## 📖 How to Use

1. Start the program in a terminal.
2. Enter a number from **1 to 9** to choose a laptop brand.
3. Select one of the available models for that brand.
4. Review the displayed specifications and price.
5. Enter the customer's name when prompted.
6. The application creates a text bill named after the customer (for example, `Customer.txt`).
7. Enter **710** at the exit prompt to close the program, or **0** to continue.

### Example Main Menu

```text
NET LEGENT LAPTOP STORE

HP          press 1
DELL        press 2
LENOVO      press 3
MACBOOK     press 4
ASUS        press 5
ACER        press 6
MSI         press 7
SAMSUNG     press 8
MICROSOFT   press 9
```

## 🧠 Python Concepts Practiced

- `while` loops
- `if` / `elif` / `else` statements
- `input()` and `print()`
- Variables and formatted strings (f-strings)
- `try` / `except` blocks
- File handling with `open()`, `write()`, and `close()`

## ⚠️ Current Limitations

- Laptop details and prices are manually defined in the code, rather than retrieved from a live store catalog.
- Bills are plain-text files; they are not tax-compliant invoices. The GST number in the sample code is a placeholder and should not be used as a real tax registration number.
- Bills use the customer name as the filename, so a repeated name can overwrite an earlier bill.
- Some invalid inputs may not be handled consistently.

## 🔮 Possible Improvements

- Store laptop records in SQLite or another database.
- Add inventory and stock management.
- Refactor repeated brand/model code into functions and data structures.
- Generate unique bill numbers and timestamps.
- Improve input validation and add unit tests.
- Build a graphical or web-based interface.

## 👨‍💻 Author

**GitHub:** [sagarmeena004](https://github.com/sagarmeena004)

---

*Built with Python as a practice project for menu-driven applications and file handling.*
