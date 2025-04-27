# Unit-Tested Python Scientific Calculator

This project showcases comprehensive set of unit tests that verify the correctness, error handling and edge case testing of calculator functions

---

## 📚 Project Overview

This repository includes:
- A **scientific calculator** application (`calculator.py`) with color-enhanced CLI using `colorama`.
- A complete suite of **unit tests** (`test_calculator.py`) ensuring correctness and stability.
- Demonstration of **best coding practices**, **TDD principles**, and **edge case handling**.

This project demonstrates both functional Python coding skills and disciplined software testing practices.

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Unittest** — Python's built-in testing framework.
- **Colorama** — for colored CLI outputs.

---

## 🚀 Features

The calculator supports the following mathematical operations:

- ➕ **Addition**
- ➖ **Subtraction**
- ✖️ **Multiplication**
- ➗ **Division** (with division-by-zero protection)
- √ **Square Root** (handles negative input safely)
- 🔥 **Power (Exponentiation)**
- % **Modulus** (handles modulus-by-zero errors)

---

## 🧩 Project Structure## 🧪 Testing Approach

The calculator is thoroughly tested using unit tests, covering:
- Normal scenarios (valid operations).
- Edge cases (e.g., division by zero, negative square roots).
- Precision cases (e.g., floating-point operations).

Each test is well-structured, meaningful, and follows best practices:
- Setup and teardown methods for a clean testing environment.
- Color-coded output for improved readability.
- Descriptive assertion messages for faster debugging.

✅ **Test Coverage:**  
- 100% function coverage achieved.
- 50+ individual assertions across different scenarios.

---

## 🧠 Development Approach

- **Test-Driven Development (TDD):**  
  Wrote unit tests first, refined implementation to pass tests.

- **Separation of Concerns:**  
  Kept UI interactions and core logic modular and isolated for easier maintenance.

- **User Experience:**  
  Implemented colorful CLI using `colorama` for a clean and engaging user interface.

---

## 🎯 Challenges Faced & Solutions

| Challenge                          | Solution                                                       |
|:----------------------------------|:---------------------------------------------------------------|
| Colorama integration inside tests  | Initialized `colorama.init()` properly to format test outputs. |
| Floating-point precision errors    | Used `assertAlmostEqual` with a `delta=0.001` tolerance.        |
| Handling division/modulus by zero  | Implemented exception handling and wrote explicit tests.       |
| Aligning text and formatting UI    | Used `str.center()` and consistent design practices.           |

---