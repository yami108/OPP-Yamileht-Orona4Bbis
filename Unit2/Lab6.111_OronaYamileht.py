import tkinter as tk
from tkinter import ttk
import os
from abc import ABC, abstractmethod

# --- CLASE BASE ABSTRACTA ---
class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def turn_on(self) -> str:
        pass

    @abstractmethod
    def turn_off(self) -> str:
        pass



class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Aletsa 5")
    
    def turn_on(self) -> str:
        return f"{self.name} is playing Metalcore music at volume 100."

    def turn_off(self) -> str:
        return f"{self.name} is turned off."


class SmartTv(SmartDevice):
    def __init__(self):
        super().__init__("Samsung TV")

    def turn_on(self) -> str:
        return f"{self.name} is playing The Big Bang Theory."
    
    def turn_off(self) -> str:
        return f"{self.name} is turned off."


class SmartLaptop(SmartDevice):
    def __init__(self):
        super().__init__("HP Laptop")

    def turn_on(self) -> str:
        return f"{self.name} is playing videos on YouTube."
    
    def turn_off(self) -> str:
        return f"{self.name} is turned off."


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Light")

    def turn_on(self) -> str:
        return f"{self.name} is turned on at 100% brightness."

    def turn_off(self) -> str:
        return f"{self.name} is turned off."



class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # 1. Configuración de la Ventana
        self.title("Lab 6.1: Smart Home Center - Polymorphism")
        self.geometry("520x520")
        self.resizable(False, False)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(current_dir, "hogar.png")

        if os.path.exists(icon_dir):
            self.app_icon = tk.PhotoImage(file=icon_dir)
            self.iconphoto(True, self.app_icon)
        else:
            print("The image doesn't exist.")


        self.items = {
            "Speaker": SmartSpeaker(),
            "TV": SmartTv(),
            "Laptop": SmartLaptop(),
            "Smart Light": SmartLight()  
        }

        self._build_interface()

    def _build_interface(self):
        # Título principal
        lbl_header = tk.Label(
            self,
            text="Smart Home Center",
            font=("Times New Roman", 16, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=10)

        group_box = tk.LabelFrame(
            self,
            text=" Select a Device ",
            font=("Times New Roman", 12, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)


        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=2)


        frame_buttons = tk.Frame(self)
        frame_buttons.pack(pady=10)

        btn_turn_on = tk.Button(
            frame_buttons,
            text="Turn On",
            command=lambda: self._handle_action(action="on"),
            bg="#27ae60",
            fg="white",
            font=("Times New Roman", 11, "bold"),
            relief="raised",
            cursor="hand2",
            padx=15,
            pady=5
        )
        btn_turn_on.pack(side="left", padx=10)

        btn_turn_off = tk.Button(
            frame_buttons,
            text="Turn Off",
            command=lambda: self._handle_action(action="off"),
            bg="#c0392b",
            fg="white",
            font=("Times New Roman", 11, "bold"),
            relief="raised",
            cursor="hand2",
            padx=15,
            pady=5
        )
        btn_turn_off.pack(side="left", padx=10)

        lbl_log = tk.Label(
            self,
            text="Activity Log:",
            font=("Times New Roman", 11, "bold"),
            fg="#2c3e50"
        )
        lbl_log.pack(anchor="w", padx=20, pady=(10, 2))

        frame_log = tk.Frame(self)
        frame_log.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        scrollbar = tk.Scrollbar(frame_log)
        scrollbar.pack(side="right", fill="y")

        self.listbox_log = tk.Listbox(
            frame_log,
            font=("Arial", 9),
            yscrollcommand=scrollbar.set,
            selectmode="single"
        )
        self.listbox_log.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.listbox_log.yview)

    def _handle_action(self, action: str):
        chosen_key = self.selected_key.get()
        active_object: SmartDevice = self.items[chosen_key]


        if action == "on":
            result_message = active_object.turn_on()
        else:
            result_message = active_object.turn_off()

        self.listbox_log.insert(tk.END, result_message)
        self.listbox_log.see(tk.END)

if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()