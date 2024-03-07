import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import os
import uuid
import random

# Function to change the MAC address of a network adapter
def spoof_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Function to change the GUID
def spoof_guid():
    new_guid = str(uuid.uuid4())  # Generates a random GUID
    print("[+] Changing Machine GUID to " + new_guid)
    # Command to change the GUID in the registry (e.g., on Windows)
    # You would need to insert the appropriate command for your OS here

# Function to change the PC name
def spoof_pc_name(new_name):
    print("[+] Changing PC name to " + new_name)
    # Command to change the PC name (e.g., on Windows)
    subprocess.call(["hostnamectl", "set-hostname", new_name])

# Function to change the disk serial number
def spoof_serial_number():
    print("[+] Changing Disk Serial Number")
    # Here you would need to insert the appropriate command to change the disk serial number

# Main function to spoof all hardware identifications
def spoof_all():
    spoof_mac("eth0", "00:11:22:33:44:55")
    spoof_guid()
    spoof_pc_name("new_pc_name")
    spoof_serial_number()

# Tkinter GUI
def spoof_gui():
    # Callback functions for the buttons
    def on_spoof_click():
        spoof_all()
        messagebox.showinfo("Success", "Hardware spoofing completed successfully!")
    
    # Create the main window
    root = tk.Tk()
    root.title("Hardware Spoofer")
    
    # Label for instructions
    instructions_label = ttk.Label(root, text="Click the 'Spoof' button to spoof hardware identifiers:")
    instructions_label.grid(row=0, column=0, padx=10, pady=10)
    
    # Button for spoofing
    spoof_button = ttk.Button(root, text="Spoof", command=on_spoof_click)
    spoof_button.grid(row=1, column=0, padx=10, pady=10)
    
    # Run the GUI loop
    root.mainloop()

# Start the GUI
spoof_gui()
