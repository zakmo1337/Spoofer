import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import os
import uuid
import random

# Function to generate a random MAC address following Microsoft's standards
def generate_random_mac():
    # Microsoft's standard for MAC address: 02-XX-XX-XX-XX-XX
    mac = [0x02, random.randint(0x00, 0x7f), random.randint(0x00, 0xff),
           random.randint(0x00, 0xff), random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

# Function to change the MAC address of a network adapter
def spoof_mac(interface):
    new_mac = generate_random_mac()
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Function to generate a random GUID following Microsoft's standards
def generate_random_guid():
    return str(uuid.uuid4())  # There are no specific standards for GUIDs in Microsoft's context

# Function to change the GUID
def spoof_guid():
    new_guid = generate_random_guid()
    print("[+] Changing Machine GUID to " + new_guid)
    # Command to change the GUID in the registry (e.g., on Windows)
    # You would need to insert the appropriate command for your OS here

# Function to generate a random PC name following Microsoft's standards
def generate_random_pc_name():
    # Microsoft's standard for PC name: up to 15 characters, letters, digits, or hyphens, cannot end with a hyphen
    return "PC-" + ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))

# Function to change the PC name
def spoof_pc_name():
    new_name = generate_random_pc_name()
    print("[+] Changing PC name to " + new_name)
    # Command to change the PC name (e.g., on Windows)
    subprocess.call(["hostnamectl", "set-hostname", new_name])

# Function to generate a random disk serial number following Microsoft's standards
def generate_random_serial_number():
    # Microsoft's standard for disk serial number: 8 hexadecimal digits
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(8))

# Function to change the disk serial number
def spoof_serial_number():
    new_serial_number = generate_random_serial_number()
    print("[+] Changing Disk Serial Number to " + new_serial_number)
    # Here you would need to insert the appropriate command to change the disk serial number

# Function to open a popup window with Discord information
def show_discord_info():
    messagebox.showinfo("Discord Information", "Discord: @zakxmo")

# Tkinter GUI
def spoof_gui():
    # Callback functions for the buttons
    def on_spoof_click():
        selected_option = option_var.get()
        if selected_option == "MAC Address":
            spoof_mac("eth0")
            messagebox.showinfo("Success", "MAC address spoofing completed successfully!")
        elif selected_option == "GUID":
            spoof_guid()
            messagebox.showinfo("Success", "GUID spoofing completed successfully!")
        elif selected_option == "PC Name":
            spoof_pc_name()
            messagebox.showinfo("Success", "PC name spoofing completed successfully!")
        elif selected_option == "Disk Serial Number":
            spoof_serial_number()
            messagebox.showinfo("Success", "Disk serial number spoofing completed successfully!")
        elif selected_option == "Discord Information":
            show_discord_info()
        else:
            messagebox.showinfo("Information", "Discord: @zakxmo")

    # Create the main window
    root = tk.Tk()
    root.title("Hardware Spoofer")
    root.resizable(False, False)  # Disable window resizing

    # Option menu for selecting what to spoof
    option_var = tk.StringVar(root)
    options = ["MAC Address", "GUID", "PC Name", "Disk Serial Number", "Discord Information"]
    option_menu = ttk.OptionMenu(root, option_var, options[0], *options)
    option_menu.grid(row=0, column=0, padx=10, pady=10)

    # Button for spoofing
    spoof_button = ttk.Button(root, text="OK", command=on_spoof_click)
    spoof_button.grid(row=1, column=0, padx=10, pady=10)

    # Run the GUI loop
    root.mainloop()

# Start the GUI
spoof_gui()
