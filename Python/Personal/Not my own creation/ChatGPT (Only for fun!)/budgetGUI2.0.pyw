#ChatGPT
import tkinter as tk

def transfer_funds():
    budget = 4000
    absa_monthly = 1000
    investec_available = investec_input.get()

    if investec_available.isdigit() and int(investec_available) >= budget:
        investec_available = int(investec_available)
        absa_available = absa_input.get()

        if absa_available.isdigit() and int(absa_available) <= absa_monthly:
            absa_available = int(absa_available)
            transfer_absa = absa_monthly - absa_available
            transfer_savings = investec_available - transfer_absa - budget

            if transfer_savings >= 0:
                x = f'Transfer R{transfer_savings} to your savings account and R{transfer_absa} to your Absa account!'
                result_label.config(text=x)
            else:
                x = f'Transfer R{investec_available-budget} (and R{abs(transfer_savings)} from your savings account) to your Absa account!'
                result_label.config(text=x)
        else:
            result_label.config(text=f'Amount in the Absa account must be equal or less than R{absa_monthly}!')
    else:
        result_label.config(text=f'Amount in the Investec account must be equal or more than R{budget}!')

# Create main window
root = tk.Tk()
root.title("Transfer Funds")

# Set window to not resizable
root.resizable(False, False)

# Create input fields
investec_label = tk.Label(root, text="Investec Available: R")
investec_label.grid(column=0, row=0, padx=5, pady=5)

investec_input = tk.Entry(root)
investec_input.grid(column=1, row=0, padx=5, pady=5)

absa_label = tk.Label(root, text="Absa Available: R")
absa_label.grid(column=0, row=1, padx=5, pady=5)

absa_input = tk.Entry(root)
absa_input.grid(column=1, row=1, padx=5, pady=5)

# Create button to transfer funds
transfer_button = tk.Button(root, text="Transfer Funds", command=transfer_funds)
transfer_button.grid(column=0, row=2, columnspan=2, padx=5, pady=5)

# Create label for results
result_label = tk.Label(root, text="")
result_label.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

root.mainloop()
