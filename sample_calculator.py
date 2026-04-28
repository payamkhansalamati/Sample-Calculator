import math
import tkinter as tk
from tkinter import messagebox


def calculate_required_samples(d: int, epsilon: float, beta: float) -> int:
    """
    Scenario approach sample bound:

    N = ceil((2 / epsilon) * (ln(1 / beta) + d))

    where:
    - d is the number of decision variables
    - epsilon is the allowed violation probability
    - beta is the confidence parameter
    """
    return math.ceil((2.0 / epsilon) * (math.log(1.0 / beta) + d))


def on_calculate() -> None:
    try:
        d_raw = entry_d.get().strip()
        epsilon_raw = entry_epsilon.get().strip()
        beta_raw = entry_beta.get().strip()

        # Validate d: positive integer
        d = int(d_raw)
        if d <= 0:
            raise ValueError("d must be a positive integer.")

        # Validate epsilon: 0 < epsilon < 1
        epsilon = float(epsilon_raw)
        if not (0.0 < epsilon < 1.0):
            raise ValueError("epsilon must be between 0 and 1 (exclusive).")

        # Validate beta: 0 < beta < 1
        beta = float(beta_raw)
        if not (0.0 < beta < 1.0):
            raise ValueError("beta must be between 0 and 1 (exclusive).")

        n_value = calculate_required_samples(d, epsilon, beta)
        result_var.set(f"Required number of samples N = {n_value}")

    except ValueError as exc:
        result_var.set("")
        messagebox.showerror("Invalid Input", str(exc))
    except Exception:
        result_var.set("")
        messagebox.showerror("Error", "Please enter valid numeric values.")


# Build GUI
root = tk.Tk()
root.title("Number of Required Samples")
root.geometry("460x260")
root.resizable(False, False)

frame = tk.Frame(root, padx=16, pady=16)
frame.pack(fill="both", expand=True)

label_title = tk.Label(
    frame,
    text="Number of Required Samples",
    font=("Segoe UI", 11, "bold"),
)
label_title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 12))

# Input: number of decision variables d
tk.Label(frame, text="Decision variables (d):", anchor="w").grid(
    row=1, column=0, sticky="w", pady=4
)
entry_d = tk.Entry(frame, width=24)
entry_d.grid(row=1, column=1, sticky="w", pady=4)

# Input: epsilon
tk.Label(frame, text="Violation probability (epsilon):", anchor="w").grid(
    row=2, column=0, sticky="w", pady=4
)
entry_epsilon = tk.Entry(frame, width=24)
entry_epsilon.grid(row=2, column=1, sticky="w", pady=4)

# Input: beta
tk.Label(frame, text="Confidence parameter (beta):", anchor="w").grid(
    row=3, column=0, sticky="w", pady=4
)
entry_beta = tk.Entry(frame, width=24)
entry_beta.grid(row=3, column=1, sticky="w", pady=4)

# Optional defaults to make first run easy
entry_d.insert(0, "10")
entry_epsilon.insert(0, "0.1")
entry_beta.insert(0, "1e-6")

btn_calculate = tk.Button(frame, text="Calculate N", command=on_calculate, width=16)
btn_calculate.grid(row=4, column=0, columnspan=2, pady=(14, 10))

result_var = tk.StringVar(value="")
label_result = tk.Label(frame, textvariable=result_var, fg="#0a5", font=("Segoe UI", 10, "bold"))
label_result.grid(row=5, column=0, columnspan=2, sticky="w", pady=(6, 0))

formula_text = "Formula: N = ceil((2 / epsilon) * (ln(1 / beta) + d))"
tk.Label(frame, text=formula_text, fg="#444").grid(
    row=6, column=0, columnspan=2, sticky="w", pady=(14, 0)
)

root.mainloop()
