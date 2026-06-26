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
        self.root.geometry("1200x750")
        
        # डिफ़ॉल्ट डेटा स्टोर स्ट्रक्चर
        self.data_store = {
            "profile": {"name": "लक्ष्मी कृषि सेवा केंद्र", "address": "नवीन मंडी परिसर, रायपुर (छ.ग.)", "state": "CG", "gst": "22ABCDE1234F1Z0", "mobile": "9827112345"},
            "kisan": [], "company": [], "items": [], "purchase": [], "sale": [], "payments": [], "receipts": []
        }
        
        self.temp_pur_items = []
        self.temp_sale_items = []
        
        self.load_database()
        self.create_auth_screen()

    def load_database(self):
        if os.path.exists(DB_FILE):
            try:
                with open(DB_FILE, "r", encoding="utf-8") as f:
                    self.data_store = json.load(f)
            except Exception as e:
                messagebox.showerror("Error", f"डेटाबेस लोड त्रुटि: {e}")

    def save_database(self):
        try:
            with open(DB_FILE, "w", encoding="utf-8") as f:
                json.dump(self.data_store, f, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"डेटा सुरक्षित करने में त्रुटि: {e}")

    def create_auth_screen(self):
        self.auth_frame = tk.Frame(self.root, bg="#263238")
        self.auth_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        card = tk.Frame(self.auth_frame, bg="white", bd=2, relief="groove")
        card.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

        tk.Label(card, text="कृषि व्यापार लॉगिन", font=("Arial", 16, "bold"), fg="#1b5e20", bg="white").pack(pady=15)
        
        tk.Label(card, text="यूज़रनेम / ID", bg="white", font=("Arial", 10)).pack(anchor="w", padx=20)
        self.user_ent = tk.Entry(card, font=("Arial", 11))
        self.user_ent.insert(0, "admin")
        self.user_ent.pack(fill="x", padx=20, pady=5)

        tk.Label(card, text="पासवर्ड", bg="white", font=("Arial", 10)).pack(anchor="w", padx=20)
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

    def create_main_dashboard(self):
        self.sidebar = tk.Frame(self.root, bg="#263238", width=250)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.main_content = tk.Frame(self.root, bg="#f5f7fa")
        self.main_content.pack(side="right", fill="both", expand=True)

        self.header_frame = tk.Frame(self.main_content, bg="white", height=60, bd=1, relief="flat")
        self.header_frame.pack(fill="x", side="top")
        self.header_frame.pack_propagate(False)
        
        prof = self.data_store["profile"]
        self.lbl_firm = tk.Label(self.header_frame, text=f"🏢 {prof['name']} | Mob: {prof['mobile']}", font=("Arial", 12, "bold"), fg="#1b5e20", bg="white")
        self.lbl_firm.pack(side="left", padx=15, pady=15)

        tk.Label(self.sidebar, text="🚜 माँ ट्रेडर्स ERP", font=("Arial", 14, "bold"), fg="#81c784", bg="#1c272b", pady=15).pack(fill="x")
        
        menus = [
            ("📊 आकर्षक डैशबोर्ड", self.show_dashboard_pane),
            ("🧑‍🌾 1.  किसान विवरण", self.show_kisan_pane),
            ("🏢 2. कंपनी विवरण", self.show_company_pane),
            ("📦 3. ITEM का विवरण", self.show_items_pane),
            ("📥 4. PURCHASE विवरण", self.show_purchase_pane),
            ("📤 5. SALE विवरण", self.show_sale_pane),
            ("💸 6. PAYMENT वाउचर", self.show_payment_pane),
            ("🧾 7. RECEIPT वाउचर", self.show_receipt_pane),
            ("📈 8 & 9. P&L और लेजर", self.show_reports_pane)
        ]

        for text, cmd in menus:
            btn = tk.Button(self.sidebar, text=text, fg="#cfd8dc", bg="#263238", activebackground="#37474f", activeforeground="white", bd=0, font=("Arial", 11), anchor="w", padx=20, pady=8, command=cmd)
            btn.pack(fill="x")

        self.current_pane = None
        self.show_dashboard_pane()

    def clear_main_content(self):
        if self.current_pane:
            self.current_pane.destroy()
        self.current_pane = tk.Frame(self.main_content, bg="#f5f7fa")
        self.current_pane.pack(fill="both", expand=True, padx=20, pady=15)

    def get_party_name(self, pid):
        for k in self.data_store["kisan"]:
            if k["id"] == pid: return f"🧑‍🌾 {k['name']}"
        for c in self.data_store["company"]:
            if c["id"] == pid: return f"🏢 {c['name']}"
        return pid

    def compute_party_balance(self, party_id):
        debit = 0.0
        credit = 0.0
        for s in self.data_store["sale"]:
            if s["partyId"] == party_id: debit += float(s["grandTotal"])
        for pay in self.data_store["payments"]:
            if pay["partyId"] == party_id: debit += float(pay["amount"])
        for p in self.data_store["purchase"]:
            if p["partyId"] == party_id: credit += float(p["grandTotal"])
        for r in self.data_store["receipts"]:
            if r["partyId"] == party_id: credit += float(r["amount"])
        return debit - credit

    def show_dashboard_pane(self):
        self.clear_main_content()
        tk.Label(self.current_pane, text="व्यापार का लाइव विवरण (Dashboard Summary)", font=("Arial", 14, "bold"), bg="#f5f7fa", fg="#212121").pack(anchor="w", pady=10)
        
        grid_frame = tk.Frame(self.current_pane, bg="#f5f7fa")
        grid_frame.pack(fill="x", pady=5)

        p_tot = sum(float(x["grandTotal"]) for x in self.data_store["purchase"])
        s_tot = sum(float(x["grandTotal"]) for x in self.data_store["sale"])
        pay_tot = sum(float(x["amount"]) for x in self.data_store["payments"])
        rec_tot = sum(float(x["amount"]) for x in self.data_store["receipts"])
        net_pl = s_tot - p_tot

        metrics = [
            ("कुल पंजीकृत किसान", str(len(self.data_store["kisan"])), "#4caf50"),
            ("संबद्ध कंपनियां", str(len(self.data_store["company"])), "#2196f3"),
            ("कुल ITEM स्टॉक प्रकार", str(len(self.data_store["items"])), "#ff9800"),
            ("कुल PURCHASE (आवक)", f"₹{p_tot:.2f}", "#009688"),
            ("कुल SALE (बिक्री)", f"₹{s_tot:.2f}", "#e91e63"),
            ("कुल PAYMENT राशि", f"₹{pay_tot:.2f}", "#9c27b0"),
            ("कुल RECEIPT राशि", f"₹{rec_tot:.2f}", "#673ab7"),
            ("व्यापार लाभ / हानि", f"₹{net_pl:.2f}", "#ff5722")
        ]

        row, col = 0, 0
        for title, val, color in metrics:
            card = tk.Frame(grid_frame, bg="white", bd=1, relief="groove")
            card.grid(row=row, column=col, padx=10, pady=10, ipadx=15, ipady=10, sticky="nsew")
            strip = tk.Frame(card, bg=color, height=4)
            strip.pack(fill="x", side="top")
            tk.Label(card, text=title, font=("Arial", 10), fg="#777777", bg="white").pack(pady=5)
            tk.Label(card, text=val, font=("Arial", 14, "bold"), fg="#212121", bg="white").pack()
            col += 1
            if col > 3:
                col = 0
                row += 1

    def show_kisan_pane(self):
        self.clear_main_content()
        form_frame = tk.LabelFrame(self.current_pane, text="🧑‍🌾 किसान का नया विवरण दर्ज करें", bg="white", font=("Arial", 11, "bold"))
        form_frame.pack(fill="x", pady=5, ipady=10, ipadx=10)

        tk.Label(form_frame, text="पूर्ण नाम *", bg="white").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        k_name = tk.Entry(form_frame, font=("Arial", 11))
        k_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="मोबाइल नंबर *", bg="white").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        k_mob = tk.Entry(form_frame, font=("Arial", 11))
        k_mob.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="पता", bg="white").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        k_addr = tk.Entry(form_frame, font=("Arial", 11))
        k_addr.grid(row=1, column=1, padx=5, pady=5)

        def save():
            if not k_name.get() or not k_mob.get(): return
            pid = f"KISAN-{len(self.data_store['kisan']) + 1001}"
            self.data_store["kisan"].append({"id": pid, "name": k_name.get(), "mobile": k_mob.get(), "address": k_addr.get(), "state": "CG"})
            self.save_database()
            self.show_kisan_pane()

        tk.Button(form_frame, text="💾 किसान सुरक्षित करें", bg="#1b5e20", fg="white", command=save).grid(row=1, column=3, pady=5, padx=5)

        tree = ttk.Treeview(self.current_pane, columns=("id", "name", "mobile", "address", "bal"), show="headings")
        for col, head in [("id", "खाता सं"), ("name", "नाम"), ("mobile", "मोबाइल"), ("address", "पता"), ("bal", "बैलेंस")]:
            tree.heading(col, text=head)
        for k in self.data_store["kisan"]:
            bal = self.compute_party_balance(k["id"])
            tree.insert("", "end", values=(k["id"], k["name"], k["mobile"], k["address"], f"₹{bal:.2f}"))
        tree.pack(fill="both", expand=True, pady=10)

    def show_company_pane(self):
        self.clear_main_content()
        form_frame = tk.LabelFrame(self.current_pane, text="🏢 कंपनी / सप्लायर का नया विवरण दर्ज करें", bg="white", font=("Arial", 11, "bold"))
        form_frame.pack(fill="x", pady=5, ipady=10, ipadx=10)

        tk.Label(form_frame, text="कंपनी नाम *", bg="white").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        c_name = tk.Entry(form_frame, font=("Arial", 11))
        c_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="GST नंबर", bg="white").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        c_gst = tk.Entry(form_frame, font=("Arial", 11))
        c_gst.grid(row=0, column=3, padx=5, pady=5)

        def save():
            if not c_name.get(): return
            pid = f"COMP-{len(self.data_store['company']) + 2001}"
            self.data_store["company"].append({"id": pid, "name": c_name.get(), "gst": c_gst.get(), "mobile": "", "address": "", "state": "CG"})
            self.save_database()
            self.show_company_pane()

        tk.Button(form_frame, text="💾 कंपनी सुरक्षित करें", bg="#1b5e20", fg="white", command=save).grid(row=1, column=3, pady=5, padx=5)

        tree = ttk.Treeview(self.current_pane, columns=("id", "name", "gst", "bal"), show="headings")
        for col, head in [("id", "COMPANY ID"), ("name", "कंपनी का नाम"), ("gst", "GSTIN"), ("bal", "बैलेंस")]:
            tree.heading(col, text=head)
        for c in self.data_store["company"]:
            bal = self.compute_party_balance(c["id"])
            tree.insert("", "end", values=(c["id"], c["name"], c["gst"], f"₹{bal:.2f}"))
        tree.pack(fill="both", expand=True, pady=10)

    def show_items_pane(self):
        self.clear_main_content()
        form_frame = tk.LabelFrame(self.current_pane, text="📦 ITEM का मास्टर विवरण बनाएं", bg="white", font=("Arial", 11, "bold"))
        form_frame.pack(fill="x", pady=5, ipady=10, ipadx=10)

        tk.Label(form_frame, text="ITEM का नाम *", bg="white").grid(row=0, column=0, padx=5, pady=5)
        i_name = tk.Entry(form_frame, font=("Arial", 11))
        i_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="यूनिट (Unit)", bg="white").grid(row=0, column=2, padx=5, pady=5)
        i_unit = tk.Entry(form_frame, font=("Arial", 11))
        i_unit.insert(0, "Bag")
        i_unit.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="GST TAX (%)", bg="white").grid(row=1, column=0, padx=5, pady=5)
        i_tax = tk.Entry(form_frame, font=("Arial", 11))
        i_tax.insert(0, "18")
        i_tax.grid(row=1, column=1, padx=5, pady=5)

        def save():
            if not i_name.get(): return
            self.data_store["items"].append({"name": i_name.get(), "unit": i_unit.get(), "tax": float(i_tax.get())})
            self.save_database()
            self.show_items_pane()

        tk.Button(form_frame, text="➕ आइटम जोड़ें", bg="#1b5e20", fg="white", command=save).grid(row=1, column=3, pady=5, padx=5)

        tree = ttk.Treeview(self.current_pane, columns=("name", "unit", "tax"), show="headings")
        tree.heading("name", text="Item नाम"); tree.heading("unit", text="यूनिट"); tree.heading("tax", text="Tax %")
        for i in self.data_store["items"]:
            tree.insert("", "end", values=(i["name"], i["unit"], f"{i['tax']}%"))
        tree.pack(fill="both", expand=True, pady=10)

    def show_purchase_pane(self):
        self.clear_main_content()
        self.temp_pur_items = []

        form_frame = tk.LabelFrame(self.current_pane, text="📥 PURCHASE विवरण फॉर्म (आवक एंट्री)", bg="white", font=("Arial", 11, "bold"))
        form_frame.pack(fill="x", pady=5, ipady=10, ipadx=10)

        tk.Label(form_frame, text="कंपनी/किसान चुनें *", bg="white").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        parties = [k["id"] for k in self.data_store["kisan"]] + [c["id"] for c in self.data_store["company"]]
        p_party = ttk.Combobox(form_frame, values=parties, font=("Arial", 10))
        p_party.grid(row=0, column=1, padx=5, pady=5)

        inv_no = f"PUR-{len(self.data_store['purchase']) + 5001}"
        tk.Label(form_frame, text=f"इनवॉइस सं: {inv_no}", font=("Arial", 10, "bold"), bg="white", fg="blue").grid(row=0, column=2, padx=10)

        item_frame = tk.Frame(form_frame, bg="#f4f6f7")
        item_frame.grid(row=1, column=0, columnspan=4, fill="x", pady=10, padx=5)

        tk.Label(item_frame, text="Item नाम", bg="#f4f6f7").grid(row=0, column=0, padx=2, pady=2)
        i_select = ttk.Combobox(item_frame, values=[i["name"] for i in self.data_store["items"]], width=15)
        i_select.grid(row=0, column=1, padx=2, pady=2)

        tk.Label(item_frame, text="मात्रा", bg="#f4f6f7").grid(row=0, column=2, padx=2, pady=2)
        i_qty = tk.Entry(item_frame, width=8)
        i_qty.insert(0, "1")
        i_qty.grid(row=0, column=3, padx=2, pady=2)

        tk.Label(item_frame, text="रेट", bg="#f4f6f7").grid(row=0, column=4, padx=2, pady=2)
        i_rate = tk.Entry(item_frame, width=8)
        i_rate.grid(row=0, column=5, padx=2, pady=2)

        tk.Label(item_frame, text="बैच नं *", bg="#f4f6f7").grid(row=0, column=6, padx=2, pady=2)
        i_batch = tk.Entry(item_frame, width=8)
        i_batch.insert(0, "B-01")
        i_batch.grid(row=0, column=7, padx=2, pady=2)

        tree = ttk.Treeview(form_frame, columns=("name", "qty", "rate", "batch", "total"), show="headings", height=4)
        for col, h in [("name", "Item"), ("qty", "Qty"), ("rate", "Rate"), ("batch", "Batch"), ("total", "Total")]:
            tree.heading(col, text=h)
        tree.grid(row=2, column=0, columnspan=4, fill="x", pady=5, padx=5)

        lbl_tot = tk.Label(form_frame, text="कुल परचेस: ₹0.00", font=("Arial", 11, "bold"), bg="white", fg="green")
        lbl_tot.grid(row=3, column=0, sticky="w", padx=5, pady=5)

        def add_item():
            if not i_select.get() or not i_rate.get(): return
            q = float(i_qty.get()); r = float(i_rate.get())
            tot = q * r
            self.temp_pur_items.append({"name": i_select.get(), "qty": q, "rate": r, "batch": i_batch.get(), "total": tot})
            tree.insert("", "end", values=(i_select.get(), q, r, i_batch.get(), f"₹{tot:.2f}"))
            grand = sum(x["total"] for x in self.temp_pur_items)
            lbl_tot.config(text=f"कुल परचेस: ₹{grand:.2f}")

        tk.Button(item_frame, text="➕ लिस्ट में जोड़े", bg="#0288d1", fg="white", command=add_item).grid(row=0, column=8, padx=5, pady=2)

        def save_invoice():
            if not p_party.get() or not self.temp_pur_items: return
            grand = sum(x["total"] for x in self.temp_pur_items)
            self.data_store["purchase"].append({
                "invNo": inv_no, "date": datetime.now().strftime("%Y-%m-%d"),
                "partyId": p_party.get(), "items": self.temp_pur_items, "grandTotal": grand
            })
            self.save_database()
            messagebox.showinfo("सफलता", f"इनवॉइस {inv_no} सुरक्षित किया गया!")
            self.show_purchase_pane()

        tk.Button(form_frame, text="💾 Purchase सुरक्षित करें", bg="#1b5e20", fg="white", font=("Arial", 11, "bold"), command=save_invoice).grid(row=3, column=3, pady=10, padx=5)

    def show_sale_pane(self):
        self.clear_main_content()
        self.temp_sale_items = []

        form_frame = tk.LabelFrame(self.current_pane, text="📤 SALE विवरण फॉर्म (बिक्री बिलिंग)", bg="white", font=("Arial", 11, "bold"))
        form_frame.pack(fill="x", pady=5, ipady=10, ipadx=10)

        tk.Label(form_frame, text="क्रेता चुनें *", bg="white").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        parties = [k["id"] for k in self.data_store["kisan"]] + [c["id"] for c in self.data_store["company"]]
        s_party = ttk.Combobox(form_frame, values=parties, font=("Arial", 10))
        s_party.grid(row=0, column=1, padx=5, pady=5)

        inv_no = f"SAL-{len(self.data_store['sale']) + 7001}"
        tk.Label(form_frame, text=f"सेल बिल सं: {inv_no}", font=("Arial", 10, "bold"), bg="white", fg="red").grid(row=0, column=2, padx=10)

        item_frame = tk.Frame(form_frame, bg="#fffde7", bd=1, relief="groove")
        item_frame.grid(row=1, column=0, columnspan=4, fill="x", pady=10, padx=5)

        tk.Label(item_frame, text="Item नाम", bg="#fffde7").grid(row=0, column=0, padx=2, pady=2)
        i_select = ttk.Combobox(item_frame, values=[i["name"] for i in self.data_store["items"]], width=15)
        i_select.grid(row=0, column=1, padx=2, pady=2)

        tk.Label(item_frame, text="Qty", bg="#fffde7").grid(row=0, column=2, padx=2, pady=2)
        i_qty = tk.Entry(item_frame, width=6)
        i_qty.insert(0, "1")
        i_qty.grid(row=0, column=3, padx=2, pady=2)

        tk.Label(item_frame, text="बिक्री दर", bg="#fffde7").grid(row=0, column=4, padx=2, pady=2)
        i_rate = tk.Entry(item_frame, width=8)
        i_rate.grid(row=0, column=5, padx=2, pady=2)

        tree = ttk.Treeview(form_frame, columns=("name", "qty", "rate", "total"), show="headings", height=4)
        for col, h in [("name", "Item"), ("qty", "Qty"), ("rate", "Rate"), ("total", "Total")]: tree.heading(col, text=h)
        tree.grid(row=2, column=0, columnspan=4, fill="x", pady=5, padx=5)

        lbl_tot = tk.Label(form_frame, text="कुल सेल नेट राशि: ₹0.00", font=("Arial", 11, "bold"), bg="white", fg="darkorange")
        lbl_tot.grid(row=3, column=0, sticky="w", padx=5, pady=5)

        def add_item():
            if not i_select.get() or not i_rate.get(): return
            q = float(i_qty.get()); r = float(i_rate.get()); tot = q * r
            self.temp_sale_items.append({"name": i_select.get(), "qty": q, "rate": r, "total": tot})
            tree.insert("", "end", values=(i_select.get(), q, r, f"₹{tot:.2f}"))
            grand = sum(x["total"] for x in self.temp_sale_items)
            lbl_tot.config(text=f"कुल सेल नेट राशि: ₹{grand:.2f}")

        tk.Button(item_frame, text="➕ बिक्री लिस्ट में जोड़ें", bg="#ff9800", fg="white", command=add_item).grid(row=0, column=6, padx=5, pady=2)

        def save_sale():
            if not s_party.get() or not self.temp_sale_items: return
            grand = sum(x["total"] for x in self.temp_sale_items)
            self.data_store["sale"].append({
                "invNo": inv_no, "date": datetime.now().strftime("%Y-%m-%d"),
                "partyId": s_party.get(), "items": self.temp_sale_items, "grandTotal": grand
            })
            self.save_database()
            
            p_name = self.get_party_name(s_party.get())
            msg = f"*बिक्री इनवॉइस*\nफर्म: {self.data_store['profile']['name']}\nग्राहक: {p_name}\nबिल संख्या: {inv_no}\nकुल राशि: ₹{grand:.2f}\nधन्यवाद!"
            messagebox.showinfo("बिल जनरेट हुआ", f"व्हाट्सएप टेक्स्ट संदेश तैयार है:\n\n{msg}")
            self.show_sale_pane()

        tk.Button(form_frame, text="💾 GST सेल बिल सुरक्षित करें", bg="#1b5e20", fg="white", font=("Arial", 11, "bold"), command=save_sale).grid(row=3, column=3, pady=10, padx=5)

    def show_payment_pane(self):
        self.clear_main_content()
        form_frame = tk.LabelFrame(self.current_pane, text="💸 PAYMENT विवरण वाउचर (राशि भुगतान)", bg="white", font=("Arial", 11, "bold"))
        form_frame.pack(fill="x", pady=5, ipady=10, ipadx=10)

        tk.Label(form_frame, text="पार्टी चयन करें *", bg="white").grid(row=0, column=0, padx=5, pady=5)
        parties = [k["id"] for k in self.data_store["kisan"]] + [c["id"] for c in self.data_store["company"]]
        p_party = ttk.Combobox(form_frame, values=parties)
        p_party.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="भुगतान राशि (₹) *", bg="white").grid(row=1, column=0, padx=5, pady=5)
        p_amt = tk.Entry(form_frame, font=("Arial", 11))
        p_amt.grid(row=1, column=1, padx=5, pady=5)

        def save():
            if not p_party.get() or not p_amt.get(): return
            v_no = f"PAY-{len(self.data_store['payments']) + 1001}"
            self.data_store["payments"].append({
                "vNo": v_no, "date": datetime.now().strftime("%Y-%m-%d"),
                "partyId": p_party.get(), "amount": float(p_amt.get())
            })
            self.save_database()
            messagebox.showinfo("सफलता", f"भुगतान सुरक्षित हुआ! वाउचर संख्या: {v_no}")
            self.show_payment_pane()

        tk.Button(form_frame, text="💾 पेमेंट वाउचर सेव करें", bg="#1b5e20", fg="white", command=save).grid(row=2, column=1, pady=10, padx=5)

    def show_receipt_pane(self):
        self.clear_main_content()
        form_frame = tk.LabelFrame(self.current_pane, text="🧾 RECEIPT विवरण वाउचर (राशि प्राप्ति)", bg="white", font=("Arial", 11, "bold"))
        form_frame.pack(fill="x", pady=5, ipady=10, ipadx=10)

        tk.Label(form_frame, text="पार्टी चयन करें *", bg="white").grid(row=0, column=0, padx=5, pady=5)
        parties = [k["id"] for k in self.data_store["kisan"]] + [c["id"] for c in self.data_store["company"]]
        p_party = ttk.Combobox(form_frame, values=parties)
        p_party.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="प्राप्त राशि (₹) *", bg="white").grid(row=1, column=0, padx=5, pady=5)
        r_amt = tk.Entry(form_frame, font=("Arial", 11))
        r_amt.grid(row=1, column=1, padx=5, pady=5)

        def save():
            if not p_party.get() or not r_amt.get(): return
            v_no = f"REC-{len(self.data_store['receipts']) + 2001}"
            self.data_store["receipts"].append({
                "vNo": v_no, "date": datetime.now().strftime("%Y-%m-%d"),
                "partyId": p_party.get(), "amount": float(r_amt.get())
            })
            self.save_database()
            messagebox.showinfo("सफलता", f"प्राप्ति रसीद संख्या: {v_no} सेव हुई।")
            self.show_receipt_pane()

        tk.Button(form_frame, text="💾 प्राप्ति रसीद सुरक्षित करें", bg="#1b5e20", fg="white", command=save).grid(row=2, column=1, pady=10, padx=5)

    def show_reports_pane(self):
        self.clear_main_content()
        
        ledg_bar = tk.LabelFrame(self.current_pane, text="📑 खाता लेजर विवरण (Ledger Detail)", bg="white", font=("Arial", 11, "bold"))
        ledg_bar.pack(fill="x", ipady=5, ipadx=5)

        tk.Label(ledg_bar, text="खाता चुनें:", bg="white").pack(side="left", padx=5)
        parties = [k["id"] for k in self.data_store["kisan"]] + [c["id"] for c in self.data_store["company"]]
        sel_party = ttk.Combobox(ledg_bar, values=parties)
        sel_party.pack(side="left", padx=5)

        tree = ttk.Treeview(self.current_pane, columns=("date", "type", "ref", "dr", "cr", "bal"), show="headings")
        for col, h in [("date", "तारीख"), ("type", "विवरण प्रकार"), ("ref", "रेफ सं"), ("dr", "डेबिट (+)"), ("cr", "क्रेडिट (-)"), ("bal", "दौड़ता शेष")]:
            tree.heading(col, text=h)
        tree.pack(fill="both", expand=True, pady=10)

        def generate_ledger():
            pid = sel_party.get()
            if not pid: return
            for i in tree.get_children(): tree.delete(i)
            
            master_ledger = []
            for s in self.data_store["sale"]:
                if s["partyId"] == pid: master_ledger.append((s["date"], "बिक्री बिल (Sale)", s["invNo"], float(s["grandTotal"]), 0.0))
            for pay in self.data_store["payments"]:
                if pay["partyId"] == pid: master_ledger.append((pay["date"], "भुगतान (Payment)", pay["vNo"], float(pay["amount"]), 0.0))
            for p in self.data_store["purchase"]:
                if p["partyId"] == pid: master_ledger.append((p["date"], "परचेस आवक (Pur)", p["invNo"], 0.0, float(p["grandTotal"])))
            for r in self.data_store["receipts"]:
                if r["partyId"] == pid: master_ledger.append((r["date"], "प्राप्ति (Receipt)", r["vNo"], 0.0, float(r["amount"])))

            master_ledger.sort(key=lambda x: x[0])

            running_balance = 0.0
            for dt, txt, ref, dr, cr in master_ledger:
                running_balance += (dr - cr)
                tree.insert("", "end", values=(dt, txt, ref, f"₹{dr:.2f}", f"₹{cr:.2f}", f"₹{running_balance:.2f}"))

        tk.Button(ledg_bar, text="🔍 लेजर विवरण खोजें", bg="#0288d1", fg="white", command=generate_ledger).pack(side="left", padx=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = KrishiVyaparERP(root)
    root.mainloop()