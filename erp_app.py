import streamlit as st
import json
import os
from datetime import datetime

# डेटाबेस फ़ाइल पाथ
DB_FILE = "krishi_vyapar_db.json"

# पेज कॉन्फ़िगरेशन (यह हमेशा सबसे ऊपर होना चाहिए)
st.set_page_config(page_title="माँ ट्रेडर्स भातमाहुल ERP", layout="wide")

# --- डेटाबेस प्रबंधन ---
def load_database():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {
        "profile": {"name": "माँ ट्रेडर्स भातमाहुल", "address": "ग्राम भातमाहुल, तहसील हसौद, जिला सक्ती (छत्तीसगढ़)", "state": "CG", "gst": "22ASXPJ1176B1ZU", "mobile": "9827112345"},
        "kisan": [], "company": [], "items": [], "purchase": [], "sale": [], "payments": [], "receipts": []
    }

def save_database(data):
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        st.error(f"डेटा सुरक्षित करने में त्रुटि: {e}")

# सेसन स्टेट में डेटा लोड करना
if "data" not in st.session_state:
    st.session_state.data = load_database()
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "temp_pur_items" not in st.session_state:
    st.session_state.temp_pur_items = []
if "temp_sale_items" not in st.session_state:
    st.session_state.temp_sale_items = []

# --- हेल्पर फ़ंक्शंस ---
def compute_party_balance(data, party_id):
    debit = 0.0
    credit = 0.0
    for s in data["sale"]:
        if s["partyId"] == party_id: debit += float(s["grandTotal"])
    for pay in data["payments"]:
        if pay["partyId"] == party_id: debit += float(pay["amount"])
    for p in data["purchase"]:
        if p["partyId"] == party_id: credit += float(p["grandTotal"])
    for r in data["receipts"]:
        if r["partyId"] == party_id: credit += float(r["amount"])
    return debit - credit

def get_party_name(data, pid):
    for k in data["kisan"]:
        if k["id"] == pid: return f"🧑‍🌾 {k['name']}"
    for c in data["company"]:
        if c["id"] == pid: return f"🏢 {c['name']}"
    return pid

# --- लॉगिन स्क्रीन ---
if not st.session_state.logged_in:
    st.markdown("<h2 style='text-align: center; color: #1b5e20;'>🚜 माँ ट्रेडर्स भातमाहुल ERP</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        with st.get_container() if hasattr(st, 'get_container') else st.container(border=True):
            st.subheader("सुरक्षित लॉगिन विवरण")
            user = st.text_input("यूज़रनेम / ID", value="admin")
            password = st.text_input("पासवर्ड", type="password", value="1234")
            if st.button("प्रवेश करें (Login)", use_container_width=True):
                if user == "admin" and password == "1234":
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("गलत यूज़रनेम या पासवर्ड!")
else:
    # --- मुख्य डैशबोर्ड लेआउट ---
    data = st.session_state.data
    prof = data["profile"]
    
    # हेडर
    st.markdown(f"<div style='background-color:#1b5e20; padding:15px; border-radius:5px; margin-bottom:20px;'>"
                f"<h1 style='color:white; margin:0;'>🏢 {prof['name']}</h1>"
                f"<p style='color:#e8f5e9; margin:0;'>📍 {prof['address']} | GST: {prof['gst']} | Mob: {prof['mobile']}</p>"
                f"</div>", unsafe_allow_html=True)
    
    # साइडबार मेनू
    st.sidebar.title("Navigation Menu")
    menu = st.sidebar.radio("मॉड्यूल चुनें", [
        "📊 आकर्षक डैशबोर्ड (Summary)", 
        "🧑‍🌾 1. किसान विवरण (Kisan Master)", 
        "🏢 2. कंपनी विवरण (Company)", 
        "📦 3. ITEM का विवरण (Item Master)",
        "📥 4. PURCHASE आवक",
        "📤 5. SALE बिक्री बिल",
        "💸 6. PAYMENT वाउचर",
        "🧾 7. RECEIPT वाउचर",
        "📈 8 & 9. लेजर स्टेटमेंट (Ledger)"
    ])
    
    if st.sidebar.button("🔒 लॉग आउट (Logout)", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

    # --- 1. डैशबोर्ड ---
    if menu == "📊 आकर्षक डैशबोर्ड (Summary)":
        st.header("व्यापार का लाइव विवरण")
        p_tot = sum(float(x["grandTotal"]) for x in data["purchase"])
        s_tot = sum(float(x["grandTotal"]) for x in data["sale"])
        pay_tot = sum(float(x["amount"]) for x in data["payments"])
        rec_tot = sum(float(x["amount"]) for x in data["receipts"])
        net_pl = s_tot - p_tot

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("कुल पंजीकृत किसान", len(data["kisan"]))
        c2.metric("संबद्ध कंपनियां", len(data["company"]))
        c3.metric("कुल PURCHASE (आवक)", f"₹{p_tot:.2f}")
        c4.metric("कुल SALE (बिक्री)", f"₹{s_tot:.2f}")

        c5, c6, c7 = st.columns(3)
        c5.metric("कुल भुगतान (Payment)", f"₹{pay_tot:.2f}")
        c6.metric("कुल रसीद (Receipt)", f"₹{rec_tot:.2f}")
        c7.metric("व्यापार अनुमानित लाभ/हानि", f"₹{net_pl:.2f}", delta=f"{net_pl:.2f}")

    # --- 2. किसान मॉड्यूल ---
    elif menu == "🧑‍🌾 1. किसान विवरण (Kisan Master)":
        st.header("🧑‍🌾 किसान मास्टर प्रबंधन")
        with st.form("kisan_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            name = col1.text_input("पूर्ण नाम *")
            mob = col2.text_input("मोबाइल नंबर *")
            addr = col1.text_input("पता (Address)")
            state = col2.selectbox("राज्य", ["CG", "MP", "UP", "MH"])
            submitted = st.form_submit_button("💾 किसान विवरण सुरक्षित करें")
            if submitted and name and mob:
                pid = f"KISAN-{len(data['kisan']) + 1001}"
                data["kisan"].append({"id": pid, "name": name, "mobile": mob, "address": addr, "state": state})
                save_database(data)
                st.success(f"किसान {name} (ID: {pid}) का खाता पंजीकृत हुआ!")
                st.rerun()

        if data["kisan"]:
            st.subheader("किसान सूची एवं बैलेंस")
            kisan_list = []
            for k in data["kisan"]:
                bal = compute_party_balance(data, k["id"])
                kisan_list.append({**k, "Current Balance": f"₹{bal:.2f}"})
            st.dataframe(kisan_list, use_container_width=True)

    # --- 3. कंपनी विवरण ---
    elif menu == "🏢 2. कंपनी विवरण (Company)":
        st.header("🏢 कंपनी / सप्लायर मास्टर")
        with st.form("company_form", clear_on_submit=True):
            c_name = st.text_input("कंपनी/फर्म का नाम *")
            c_gst = st.text_input("GSTIN नंबर")
            submitted = st.form_submit_button("💾 कंपनी सुरक्षित करें")
            if submitted and c_name:
                pid = f"COMP-{len(data['company']) + 2001}"
                data["company"].append({"id": pid, "name": c_name, "gst": c_gst})
                save_database(data)
                st.success("कंपनी पंजीकृत की गई!")
                st.rerun()
        if data["company"]:
            st.dataframe(data["company"], use_container_width=True)

    # --- 4. ITEM मास्टर ---
    elif menu == "📦 3. ITEM का विवरण (Item Master)":
        st.header("📦 स्टॉक आइटम मास्टर")
        with st.form("item_form", clear_on_submit=True):
            i_name = st.text_input("Item का नाम *")
            i_unit = st.selectbox("यूनिट", ["Bag", "Litre", "Kg", "Pcs"])
            i_tax = st.number_input("GST %", min_value=0, max_value=28, value=18)
            submitted = st.form_submit_button("➕ आइटम स्टॉक में जोड़ें")
            if submitted and i_name:
                data["items"].append({"name": i_name, "unit": i_unit, "tax": i_tax})
                save_database(data)
                st.success(f"{i_name} मास्टर लिस्ट में जोड़ा गया!")
                st.rerun()
        if data["items"]:
            st.dataframe(data["items"], use_container_width=True)

    # --- 5. PURCHASE आवक ---
    elif menu == "📥 4. PURCHASE आवक":
        st.header("📥 परचेस स्टॉक आवक बिल प्रविष्टि")
        parties = [k["id"] for k in data["kisan"]] + [c["id"] for c in data["company"]]
        p_party = st.selectbox("सप्लायर/कंपनी खाता चुनें *", parties if parties else ["कोई खाता उपलब्ध नहीं"])
        
        inv_no = f"PUR-{len(data['purchase']) + 5001}"
        st.info(f"ऑटो इनवॉइस सं: {inv_no}")

        with st.container(border=True):
            st.write("आइटम जोड़ें")
            items_list = [i["name"] for i in data["items"]]
            i_select = st.selectbox("Item चुनें", items_list if items_list else ["पहले आइटम बनाएं"])
            c1, c2, c3 = st.columns(3)
            i_qty = c1.number_input("मात्रा (Qty)", min_value=1, value=1)
            i_rate = c2.number_input("लागत दर (Purchase Rate)", min_value=0.0, value=0.0)
            i_batch = c3.text_input("बैच नंबर", value="B-01")
            
            if st.button("➕ लिस्ट में आइटम जोड़ें"):
                tot = i_qty * i_rate
                st.session_state.temp_pur_items.append({"name": i_select, "qty": i_qty, "rate": i_rate, "batch": i_batch, "total": tot})
        
        if st.session_state.temp_pur_items:
            st.subheader("वर्तमान जोड़े गए आइटम्स")
            st.table(st.session_state.temp_pur_items)
            grand = sum(x["total"] for x in st.session_state.temp_pur_items)
            st.write(f"### कुल देय राशि: ₹{grand:.2f}")
            
            if st.button("💾 परचेस बिल फाइनल लॉक करें"):
                data["purchase"].append({
                    "invNo": inv_no, "date": datetime.now().strftime("%Y-%m-%d"),
                    "partyId": p_party, "items": st.session_state.temp_pur_items, "grandTotal": grand
                })
                save_database(data)
                st.session_state.temp_pur_items = []
                st.success("परचेस इनवॉइस सफलतापूर्वक सेव हुआ!")
                st.rerun()

    # --- 6. SALE बिक्री ---
    elif menu == "📤 5. SALE बिक्री बिल":
        st.header("📤 नया डिजिटल जीएसटी सेल बिल")
        parties = [k["id"] for k in data["kisan"]] + [c["id"] for c in data["company"]]
        s_party = st.selectbox("क्रेता / ग्राहक खाता चुनें *", parties if parties else ["कोई खाता उपलब्ध नहीं"])
        
        inv_no = f"SAL-{len(data['sale']) + 7001}"
        st.error(f"सेल बिल संख्या: {inv_no}")

        with st.container(border=True):
            items_list = [i["name"] for i in data["items"]]
            i_select = st.selectbox("बिक्री Item चुनें", items_list if items_list else ["पहले आइटम बनाएं"])
            c1, c2 = st.columns(2)
            i_qty = c1.number_input("बिक्री मात्रा", min_value=1, value=1)
            i_rate = c2.number_input("बिक्री दर (Sale Rate)", min_value=0.0, value=0.0)
            
            if st.button("➕ बिक्री सूची में डालें"):
                tot = i_qty * i_rate
                st.session_state.temp_sale_items.append({"name": i_select, "qty": i_qty, "rate": i_rate, "total": tot})

        if st.session_state.temp_sale_items:
            st.subheader("बिल आइटम लिस्ट")
            st.table(st.session_state.temp_sale_items)
            grand = sum(x["total"] for x in st.session_state.temp_sale_items)
            st.write(f"### कुल ग्रांड टोटल: ₹{grand:.2f}")
            
            if st.button("💾 सेल बिल प्रिंट/सुरक्षित करें"):
                data["sale"].append({
                    "invNo": inv_no, "date": datetime.now().strftime("%Y-%m-%d"),
                    "partyId": s_party, "items": st.session_state.temp_sale_items, "grandTotal": grand
                })
                save_database(data)
                
                # डिजिटल रसीद टेक्स्ट
                p_name = get_party_name(data, s_party)
                msg = f"फर्म: {prof['name']}\nग्राहक: {p_name}\nबिल सं: {inv_no}\nकुल: ₹{grand:.2f}"
                st.text_area("WhatsApp के लिए रेडी टेक्स्ट:", value=msg)
                
                st.session_state.temp_sale_items = []
                st.success("बिक्री बिल सेव कर दिया गया है।")

    # --- 7. PAYMENT ---
    elif menu == "💸 6. PAYMENT वाउचर":
        st.header("💸 भुगतान प्रविष्टि (Payment Voucher)")
        parties = [k["id"] for k in data["kisan"]] + [c["id"] for c in data["company"]]
        with st.form("pay_form", clear_on_submit=True):
            p_party = st.selectbox("पार्टी चुनें", parties)
            amt = st.number_input("भुगतान की गई राशि (₹)", min_value=0.0)
            if st.form_submit_button("💾 पेमेंट वाउचर लॉक करें") and amt > 0:
                v_no = f"PAY-{len(data['payments']) + 1001}"
                data["payments"].append({"vNo": v_no, "date": datetime.now().strftime("%Y-%m-%d"), "partyId": p_party, "amount": amt})
                save_database(data)
                st.success("भुगतान वाउचर सफलतापूर्वक सहेजा गया!")
                st.rerun()

    # --- 8. RECEIPT ---
    elif menu == "🧾 7. RECEIPT वाउचर":
        st.header("🧾 रसीद प्राप्ति प्रविष्टि (Receipt Voucher)")
        parties = [k["id"] for k in data["kisan"]] + [c["id"] for c in data["company"]]
        with st.form("rec_form", clear_on_submit=True):
            r_party = st.selectbox("पार्टी चुनें", parties)
            amt = st.number_input("प्राप्त हुई राशि (₹)", min_value=0.0)
            if st.form_submit_button("💾 रसीद वाउचर लॉक करें") and amt > 0:
                v_no = f"REC-{len(data['receipts']) + 2001}"
                data["receipts"].append({"vNo": v_no, "date": datetime.now().strftime("%Y-%m-%d"), "partyId": r_party, "amount": amt})
                save_database(data)
                st.success("प्राप्ति वाउचर सफलतापूर्वक सहेजा गया!")
                st.rerun()

    # --- 9. लेजर ---
    elif menu == "📈 8 & 9. लेजर स्टेटमेंट (Ledger)":
        st.header("📈 खाता लेजर और पासबुक")
        parties = [k["id"] for k in data["kisan"]] + [c["id"] for c in data["company"]]
        sel_party = st.selectbox("लेजर देखने के लिए खाता संख्या चुनें", parties)
        
        if sel_party:
            master_ledger = []
            for s in data["sale"]:
                if s["partyId"] == sel_party: master_ledger.append({"तारीख": s["date"], "विवरण": "बिक्री बिल (Sale)", "रेफरेंस": s["invNo"], "डेबिट (+)": float(s["grandTotal"]), "क्रेडिट (-)": 0.0})
            for pay in data["payments"]:
                if pay["partyId"] == sel_party: master_ledger.append({"तारीख": pay["date"], "विवरण": "भुगतान (Payment)", "रेफरेंस": pay["vNo"], "डेबिट (+)": float(pay["amount"]), "क्रेडिट (-)": 0.0})
            for p in data["purchase"]:
                if p["partyId"] == sel_party: master_ledger.append({"तारीख": p["date"], "विवरण": "परचेस आवक (Pur)", "रेफरेंस": p["invNo"], "डेबिट (+)": 0.0, "क्रेडिट (-)": float(p["grandTotal"])})
            for r in data["receipts"]:
                if r["partyId"] == sel_party: master_ledger.append({"तारीख": r["date"], "विवरण": "प्राप्ति (Receipt)", "रेफरेंस": r["vNo"], "डेबिट (+)": 0.0, "क्रेडिट (-)": float(r["amount"])})
            
            master_ledger.sort(key=lambda x: x["तारीख"])
            
            # दौड़ता शेष (Running Balance) गणना
            running_balance = 0.0
            final_ledger = []
            for row in master_ledger:
                running_balance += (row["डेबिट (+)"] - row["क्रेडिट (-)"])
                final_ledger.append({**row, "दौड़ता शेष (Balance)": f"₹{running_balance:.2f}"})
            
            st.subheader(f"{get_party_name(data, sel_party)} का स्टेटमेंट")
            if final_ledger:
                st.dataframe(final_ledger, use_container_width=True)
            else:
                st.warning("इस खाते में अभी कोई लेन-देन दर्ज नहीं है।")