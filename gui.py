#!/usr/bin/env python3
"""Graphical user interface for the Unit Converter application using tkinter."""

import tkinter as tk
from tkinter import ttk, messagebox
from converters.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from converters.distance import kilometers_to_miles, miles_to_kilometers
from converters.weight import kilograms_to_pounds, pounds_to_kilograms
from converters.length import centimeters_to_inches, inches_to_centimeters


class UnitConverterGUI:
    """GUI application for unit conversion."""
    
    def __init__(self, root):
        """Initialize the GUI application.
        
        Args:
            root: The tkinter root window
        """
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        self.conversions = {
            "Celsius → Fahrenheit": celsius_to_fahrenheit,
            "Fahrenheit → Celsius": fahrenheit_to_celsius,
            "Kilometers → Miles": kilometers_to_miles,
            "Miles → Kilometers": miles_to_kilometers,
            "Kilograms → Pounds": kilograms_to_pounds,
            "Pounds → Kilograms": pounds_to_kilograms,
            "Centimeters → Inches": centimeters_to_inches,
            "Inches → Centimeters": inches_to_centimeters,
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface components."""
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame,
            text="Unit Converter",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(expand=True)
        
        main_frame = tk.Frame(self.root, padx=30, pady=30)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        conversion_label = tk.Label(
            main_frame,
            text="Select Conversion Type:",
            font=("Arial", 12)
        )
        conversion_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.conversion_var = tk.StringVar()
        self.conversion_combo = ttk.Combobox(
            main_frame,
            textvariable=self.conversion_var,
            values=list(self.conversions.keys()),
            state="readonly",
            font=("Arial", 11),
            width=30
        )
        self.conversion_combo.pack(pady=(0, 20))
        self.conversion_combo.current(0)
        
        input_label = tk.Label(
            main_frame,
            text="Enter Value:",
            font=("Arial", 12)
        )
        input_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.input_entry = tk.Entry(
            main_frame,
            font=("Arial", 11),
            width=33
        )
        self.input_entry.pack(pady=(0, 20))
        self.input_entry.bind('<Return>', lambda e: self.convert())
        
        convert_button = tk.Button(
            main_frame,
            text="Convert",
            command=self.convert,
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        convert_button.pack(pady=(0, 20))
        
        result_label = tk.Label(
            main_frame,
            text="Result:",
            font=("Arial", 12)
        )
        result_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.result_text = tk.Text(
            main_frame,
            height=3,
            font=("Arial", 11),
            state=tk.DISABLED,
            bg="#ecf0f1",
            relief=tk.FLAT
        )
        self.result_text.pack(fill=tk.X)
    
    def convert(self):
        """Perform the conversion and display the result."""
        try:
            value = float(self.input_entry.get())
            conversion_type = self.conversion_var.get()
            
            if not conversion_type:
                messagebox.showwarning(
                    "No Selection",
                    "Please select a conversion type."
                )
                return
            
            converter_func = self.conversions[conversion_type]
            result = converter_func(value)
            
            from_unit, to_unit = conversion_type.split(" → ")
            result_message = f"{value:.2f} {from_unit} = {result:.2f} {to_unit}"
            
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, result_message)
            self.result_text.config(state=tk.DISABLED)
            
        except ValueError as e:
            if "could not convert" in str(e):
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter a valid number."
                )
            else:
                messagebox.showerror("Conversion Error", str(e))
        except TypeError as e:
            messagebox.showerror("Type Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = UnitConverterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()