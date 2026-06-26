import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# डेटाबेस फ़ाइल पाथ
DB_FILE = "krishi_vyapar_db.json"

class KrishiVyaparERP:
    def __init__(self, root):
        self.root = root
        self.root.title("माँ ट्रेडर्स भातमाहुल ERP - Advanced Python Edition")
        self.root.geometry("1100x700")
        
        # डिफ़ॉल्ट डेटा स्टोर स्ट्रक्चर
        self.data_store = {
            "profile": {"name": "लक्ष्मी कृषि सेवा केंद्र", "address": "नवीन मंडी परिसर, रायपुर (छ.ग.)", "state": "CG", "gst": "22ABCDE1234F1Z0", "mobile": "9827112345"},
            "kisan": [], "company": [], "items": [], "purchase": [], "sale": [], "payments": [], "receipts": []
        }
        
        self.load_database()
        self.create_auth_screen()

    # --- डेटाबेस फ़ंक्शन ---
    def load_database(self):
        if os.path.exists(DB_FILE):
            try:
                with open(DB_FILE, "r", encoding="utf-8") as f:
                    self.data_store = json.load(f)
            except Exception as e:
                messagebox.showerror("Error", f"डेटाबेस लोड करने में त्रुटि: {e}")

    def save_database(self):
        try:
            with open(DB_FILE, "w", encoding="utf-8") as f:
                json.dump(self.data_store, f, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"डेटा सुरक्षित करने में त्रुटि: {e}")

    # --- लॉगिन स्क्रीन ---
    def create_auth_screen(self):
        self.auth_frame = tk.Frame(self.root, bg="#263238")
        self.auth_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        card = tk.Frame(self.auth_frame, bg="white", bd=2, relief="groove")
        card.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

        tk.Label(card, text="कृषि व्यापार लॉगिन", font=("Arial", 16, "bold"), fg="#1b5e20", bg="white").pack(pady=15)
        
        tk.Label(card, text="यूज़रनेम / ID", bg="white", font=("Arial", 10)).pack(anchor="w", px=20)
        self.user_ent = tk.Entry(card, font=("Arial", 11))
        self.user_ent.insert(0, "admin")
        self.user_ent.pack(fill="x", padx=20, pady=5)

        tk.Label(card, text="पासवर्ड", bg="white", font=("Arial", 10)).pack(anchor="w", px=20)
        self.pass_ent = tk.Entry(card, show="*", font=("Arial", 11))
        self.pass_ent.insert(0, "1234")
        self.pass_ent.pack(fill="x", padx=20, pady=5)

        btn = tk.Button(card, text="प्रवेश करें (Login)", bg="#1b5e20", fg="white", font=("Arial", 11, "bold"), command=self.handle_login)
        btn.pack(fill="x", padx=20, pady=20)

    def handle_login(self):
        if self.user_ent.get() == "admin" and self.pass_ent.get() == "1234":
            self.auth_frame.destroy()
            self.create_main_dashboard()
        else:
            messagebox.showerror("त्रुटि", "गलत यूज़रनेम या पासवर्ड!")

    # --- मुख्य ERP डैशबोर्ड ---
    def create_main_dashboard(self):
        # मुख्य विंडो लेआउट विभाजन
        self.sidebar = tk.Frame(self.root, bg="#263238", width=250)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.main_content = tk.Frame(self.root, bg="#f5f7fa")
        self.main_content.pack(side="right", fill="both", expand=True)

        # फर्म हेडर इन्फो
        self.header_frame = tk.Frame(self.main_content, bg="white", height=70, bd=1, relief="flat")
        self.header_frame.pack(fill="x", side="top")
        self.header_frame.pack_propagate(False)
        
        self.lbl_firm = tk.Label(self.header_frame, text=self.data_store["profile"]["name"], font=("Arial", 14, "bold"), fg="#1b5e20", bg="white")
        self.lbl_firm.pack(side="left", padx=15, pady=5)

        # साइडबार मेनू बटन्स
        tk.Label(self.sidebar, text="🚜 माँ ट्रेडर्स ERP", font=("Arial", 14, "bold"), fg="#81c784", bg="#1c272b", pady=15).pack(fill="x")
        
        menus = [
            ("📊 आकर्षक डैशबोर्ड", self.show_dashboard_pane),
            ("🧑‍🌾 1. किसान विवरण", self.show_kisan_pane),
            ("🏢 2. कंपनी विवरण", self.show_company_pane),
            ("📦 3. ITEM का विवरण", self.show_items_pane),
            ("📥 4. PURCHASE आवक", self.show_under_construction),
            ("📤 5. SALE बिक्री बिल", self.show_under_construction),
            ("💸 6. PAYMENT विवरण", self.show_under_construction),
            ("🧾 7. RECIEPT विवरण", self.show_under_construction)
        ]

        for text, cmd in menus:
            btn = tk.Button(self.sidebar, text=text, fg="#cfd8dc", bg="#263238", activebackground="#37474f", activeforeground="white", bd=0, font=("Arial", 11), anchor="w", padx=20, pady=10, command=cmd)
            btn.pack(fill="x")

        # डिफ़ॉल्ट रूप से डैशबोर्ड लोड करें
        self.current_pane = None
        self.show_dashboard_pane()

    def clear_main_content(self):
        if self.current_pane:
            self.current_pane.destroy()
        self.current_pane = tk.Frame(self.main_content, bg="#f5f7fa")
        self.current_pane.pack(fill="both", expand=True, padx=20, pady=20)

    # --- 1. लाइव डैशबोर्ड समरी पैन ---
    def show_dashboard_pane(self):
        self.clear_main_content()
        tk.Label(self.current_pane, text="व्यापार का लाइव विवरण (Dashboard Summary)", font=("Arial", 14, "bold"), bg="#f5f7fa", fg="#212121").pack(anchor="w", pady=10)
        
        grid_frame = tk.Frame(self.current_pane, bg="#f5f7fa")
        grid_frame.pack(fill="x", pady=10)

        metrics = [
            ("कुल पंजीकृत किसान", str(len(self.data_store["kisan"])), "#4caf50"),
            ("संबद्ध कंपनियां", str(len(self.data_store["company"])), "#2196f3"),
            ("कुल ITEM स्टॉक प्रकार", str(len(self.data_store["items"])), "#ff9800"),
            ("कुल PURCHASE (आवक)", f"₹{sum(float(x.get('total', 0)) for x in self.data_store['purchase'])}", "#009688"),
            ("कुल SALE (बिक्री)", f"₹{sum(float(x.get('total', 0)) for x in self.data_store['sale'])}", "#e91e63")
        ]

        row, col = 0, 0
        for title, val, color in metrics:
            card = tk.Frame(grid_frame, bg="white", bd=1, relief="raised")
            card.grid(row=row, column=col, padx=10, pady=10, ipadx=20, ipady=15)
            
            # टॉप कलर्ड स्ट्रिप
            strip = tk.Frame(card, bg=color, height=4)
            strip.pack(fill="x", side="top")
            
            tk.Label(card, text=title, font=("Arial", 10), fg="#777777", bg="white").pack(pady=5)
            tk.Label(card, text=val, font=("Arial", 16, "bold"), fg="#212121", bg="white").pack()
            
            col += 1
            if col > 2:
                col = 0
                row += 1

    # --- 2. किसान मॉड्यूल पैन ---
    def show_kisan_pane(self):
        self.clear_main_content()
        
        # फॉर्म फ़्रेम
        form_frame = tk.LabelFrame(self.current_pane, text="🧑‍🌾 किसान का नया विवरण", bg="white", font=("Arial", 11, "bold"), pading=10)
        form_frame.pack(fill="x", pady=10)

        tk.Label(form_frame, text="किसान का नाम *", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        k_name = tk.Entry(form_frame, font=("Arial", 11))
        k_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="मोबाइल नंबर *", bg="white").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        k_mob = tk.Entry(form_frame, font=("Arial", 11))
        k_mob.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="राज्य (State)", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        k_state = ttk.Combobox(form_frame, values=["CG", "MP", "UP", "MH", "BR"], font=("Arial", 10))
        k_state.set("CG")
        k_state.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="पता (Address)", bg="white").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        k_addr = tk.Entry(form_frame, font=("Arial", 11))
        k_addr.grid(row=1, column=3, padx=5, pady=5)

        def save_kisan():
            if not k_name.get() or not k_mob.get():
                messagebox.showwarning("चेतावनी", "कृपया अनिवार्य फ़ील्ड भरें!")
                return
            new_kisan = {
                "id": len(self.data_store["kisan"]) + 1001,
                "name": k_name.get(), "mobile": k_mob.get(),
                "state": k_state.get(), "address": k_addr.get(), "balance": 0.0
            }
            self.data_store["kisan"].append(new_kisan)
            self.save_database()
            messagebox.showinfo("सफलता", "किसान डेटा सुरक्षित कर लिया गया है।")
            self.show_kisan_pane()

        tk.Button(form_frame, text="💾 डेटा सुरक्षित करें", bg="#1b5e20", fg="white", font=("Arial", 10, "bold"), command=save_kisan).grid(row=2, column=3, pady=10)

        # किसान लिस्ट टेबल
        list_frame = tk.LabelFrame(self.current_pane, text="दर्ज किसानों की सूची", bg="white", font=("Arial", 11, "bold"))
        list_frame.pack(fill="both", expand=True, pady=10)

        columns = ("id", "name", "state", "address", "mobile", "balance")
        tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        tree.heading("id", text="खाता संख्या")
        tree.heading("name", text="पूर्ण नाम")
        tree.heading("state", text="राज्य")
        tree.heading("address", text="पता")
        tree.heading("mobile", text="मोबाइल")
        tree.heading("balance", text="करेंट बैलेंस")
        
        for k in self.data_store["kisan"]:
            tree.insert("", "end", values=(k["id"], k["name"], k["state"], k["address"], k["mobile"], f"₹{k['balance']}"))
        
        tree.pack(fill="both", expand=True)

    # --- 3. कंपनी मॉड्यूल पैन ---
    def show_company_pane(self):
        self.clear_main_content()
        # इसी तरह कंपनी के लिए भी GUI फॉर्म और तालिका तैयार की जा सकती है...
        tk.Label(self.current_pane, text="🏢 कंपनी प्रबंधन मॉड्यूल यहाँ लोड होगा।", font=("Arial", 12), bg="#f5f7fa").pack(pady=20)

    # --- 4. आइटम स्टॉक मॉड्यूल पैन ---
    def show_items_pane(self):
        self.clear_main_content()
        form_frame = tk.LabelFrame(self.current_pane, text="📦 ITEM का मास्टर विवरण बनाएं", bg="white", font=("Arial", 11, "bold"), padx=10, pady=10)
        form_frame.pack(fill="x", pady=10)

        tk.Label(form_frame, text="ITEM का नाम *", bg="white").grid(row=0, column=0, padx=5, pady=5)
        i_name = tk.Entry(form_frame, font=("Arial", 11))
        i_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Unit (बैग/लीटर)", bg="white").grid(row=0, column=2, padx=5, pady=5)
        i_unit = tk.Entry(form_frame, font=("Arial", 11))
        i_unit.insert(0, "Bag")
        i_unit.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="TAX RATE (%)", bg="white").grid(row=1, column=0, padx=5, pady=5)
        i_tax = tk.Entry(form_frame, font=("Arial", 11))
        i_tax.insert(0, "18")
        i_tax.grid(row=1, column=1, padx=5, pady=5)

        def save_item():
            if not i_name.get(): return
            self.data_store["items"].append({"name": i_name.get(), "unit": i_unit.get(), "tax": i_tax.get()})
            self.save_database()
            self.show_items_pane()

        tk.Button(form_frame, text="➕ आइटम सुरक्षित करें", bg="#1b5e20", fg="white", command=save_item).grid(row=1, column=3, pady=10)

    def show_under_construction(self):
        self.clear_main_content()
        tk.Label(self.current_pane, text="🚧 यह मॉड्यूल (Purchase/Sale/Voucher) अभी निर्मित हो रहा है।", font=("Arial", 12, "italic"), fg="gray", bg="#f5f7fa").pack(pady=50)

if __name__ == "__main__":
    root = tk.Tk()
    app = KrishiVyaparERP(root)
    root.mainloop()