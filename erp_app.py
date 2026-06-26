<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>माँ ट्रेडर्स भातमाहुल  ERP - Advanced Edition</title>
    <style>
        :root {
            --primary: #1b5e20;
            --primary-light: #e8f5e9;
            --sidebar-bg: #263238;
            --sidebar-hover: #37474f;
            --accent: #0288d1;
            --danger: #d32f2f;
            --light: #f5f7fa;
            --dark: #212121;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Arial, sans-serif; }
        
        
        /* Auth System Style */
       

        /* Left Side Menu Bar */
        
        /* Main Content Wrapper */
        
        
       
</head>
<body>

    <div id="authContainer" class="auth-container">
        <div id="box-login" class="auth-card">
            <h2>कृषि व्यापार लॉगिन</h2>
            <div class="form-group"><label>यूज़रनेम / ID</label><input type="text" id="loginUser" value="admin"></div>
            <div class="form-group"><label>पासवर्ड</label><input type="password" id="loginPass" value="1234"></div>
            <button class="btn btn-primary" style="width:100%; margin-top:10px;" onclick="handleLogin()">प्रवेश करें (Login)</button>
            <div style="margin-top:15px; display:flex; justify-content:space-between; font-size:12px;">
                <a href="#" onclick="switchAuth('forgot')" style="color:var(--accent)">पासवर्ड भूल गए?</a>
                <a href="#" onclick="switchAuth('new')" style="color:var(--primary)">नया यूज़र बनाएं</a>
            </div>
        </div>
        <div id="box-register" class="auth-card hidden">
            <h2>नया यूज़र रजिस्ट्रेशन</h2>
            <div class="form-group"><label>नया यूज़रनेम</label><input type="text" id="regUser"></div>
            <div class="form-group"><label>नया पासवर्ड</label><input type="password" id="regPass"></div>
            <button class="btn btn-primary" style="width:100%;" onclick="handleRegister()">रजिस्टर करें</button>
            <p style="text-align:center; margin-top:10px; font-size:12px;"><a href="#" onclick="switchAuth('login')">वापस लॉगिन पर जाएं</a></p>
        </div>
        <div id="box-forgot" class="auth-card hidden">
            <h2>पासवर्ड रीसेट करें</h2>
            <div class="form-group"><label>अपना यूज़रनेम दर्ज करें</label><input type="text" id="forgotUser"></div>
            <button class="btn btn-secondary" style="width:100%;" onclick="handleForgot()">पासवर्ड रिकवर करें</button>
            <p style="text-align:center; margin-top:10px; font-size:12px;"><a href="#" onclick="switchAuth('login')">लॉगिन पर आएं</a></p>
        </div>
    </div>

    <nav class="sidebar no-print">
        <div class="sidebar-brand">🚜 माँ ट्रेडर्स भातमाहुल ERP</div>
        <ul class="sidebar-menu">
            <li><a onclick="navTo('dashboard')" id="m-dashboard" class="active">📊 आकर्षक डैशबोर्ड</a></li>
            <li><a onclick="navTo('kisan')" id="m-kisan">🧑‍🌾 1. किसान विवरण</a></li>
            <li><a onclick="navTo('company')" id="m-company">🏢 2. कंपनी विवरण</a></li>
            <li><a onclick="navTo('items')" id="m-items">📦 3. ITEM का विवरण</a></li>
            <li><a onclick="navTo('purchase')" id="m-purchase">📥 4. PURCHASE विवरण</a></li>
            <li><a onclick="navTo('sale')" id="m-sale">📤 5. SALE विवरण</a></li>
            <li><a onclick="navTo('payment')" id="m-payment">💸 6. PAYMENT विवरण</a></li>
            <li><a onclick="navTo('receipt')" id="m-receipt">🧾 7. RECIEPT विवरण</a></li>
            <li><a onclick="navTo('reports')" id="m-reports">📈 8 & 9. P&L और लेजर</a></li>
        </ul>
        <div style="padding:15px; text-align:center;">
            <button class="btn btn-danger btn-sm" onclick="logout()" style="width:100%;">🔒 लॉगआउट</button>
        </div>
    </nav>

    <main class="main-content">
        <div class="top-profile-bar no-print">
            <div class="firm-info">
                <h2 id="viewFirmName">लक्ष्मी कृषि केंद्र</h2>
                <p>📍 <span id="viewAddress">मंडी प्रांगण, रायपुर</span> | राज्य: <span id="viewState">CG (22)</span> | GSTIN: <span id="viewGst">22ABCDE1234F1Z0</span> | Mob: <span id="viewMob">9827100000</span></p>
            </div>
            <div style="display:flex; gap:10px;">
                <button class="btn btn-secondary btn-sm" onclick="toggleProfileForm()">✏️ प्रोफाइल बदलें</button>
                <button class="btn btn-primary btn-sm" onclick="exportJSONData()">📥 बैकअप लें</button>
                <input type="file" id="importFile" class="hidden" onchange="importJSONData(event)">
                <button class="btn btn-sm" style="background:#607d8b; color:white;" onclick="document.getElementById('importFile').click()">📤 बैकअप रिस्टोर</button>
            </div>
        </div>

        <div id="profileEditCard" class="card hidden no-print">
            <div class="card-title">फर्म प्रोफाइल सेटिंग्स अपडेट करें</div>
            <div class="grid-4">
                <div class="form-group"><label>फर्म / प्रोपराइटर का नाम</label><input type="text" id="setFirmName"></div>
                <div class="form-group"><label>पूरा पता</label><input type="text" id="setAddress"></div>
                <div class="form-group">
                    <label>राज्य (State)</label>
                    <select id="setInitialState">
                        <option value="CG">Chhattisgarh (CG)</option>
                        <option value="MP">Madhya Pradesh (MP)</option>
                        <option value="UP">Uttar Pradesh (UP)</option>
                        <option value="MH">Maharashtra (MH)</option>
                        <option value="BR">Bihar (BR)</option>
                        <option value="RJ">Rajasthan (RJ)</option>
                    </select>
                </div>
                <div class="form-group"><label>GST No.</label><input type="text" id="setGst"></div>
                <div class="form-group"><label>मोबाइल नंबर</label><input type="text" id="setMob"></div>
            </div>
            <button class="btn btn-primary" onclick="saveFirmProfile()">💾 प्रोफाइल अपडेट करें</button>
        </div>

        <div id="v-dashboard" class="view-pane">
            <div class="card-title">व्यापार का लाइव विवरण (Dashboard Summary)</div>
            <div class="dash-row">
                <div class="metric-card" style="border-top-color:#4caf50"><h3>1. कुल पंजीकृत किसान</h3><div class="value" id="d-kisan">0</div></div>
                <div class="metric-card" style="border-top-color:#2196f3"><h3>2. संबद्ध कंपनियां</h3><div class="value" id="d-company">0</div></div>
                <div class="metric-card" style="border-top-color:#ff9800"><h3>3. कुल ITEM STOCK प्रकार</h3><div class="value" id="d-items">0</div></div>
                <div class="metric-card" style="border-top-color:#009688"><h3>4. कुल PURCHASE (आवक)</h3><div class="value" id="d-purchase">₹0</div></div>
                <div class="metric-card" style="border-top-color:#e91e63"><h3>5. कुल SALE (बिक्री)</h3><div class="value" id="d-sale">₹0</div></div>
                <div class="metric-card" style="border-top-color:#9c27b0"><h3>6. कुल PAYMENT राशि</h3><div class="value" id="d-payment">₹0</div></div>
                <div class="metric-card" style="border-top-color:#673ab7"><h3>7. कुल RECEIPT राशि</h3><div class="value" id="d-receipt">₹0</div></div>
                <div class="metric-card" style="border-top-color:#ff5722"><h3>8. व्यापार लाभ / हानि</h3><div class="value" id="d-pl">₹0</div></div>
            </div>
        </div>

        <div id="v-kisan" class="view-pane hidden">
            <div class="card">
                <div class="card-title">🧑‍🌾 किसान का नया विवरण / संपादन Form</div>
                <form id="f-kisan" onsubmit="submitKisan(event)">
                    <input type="hidden" id="kisanEditIdx">
                    <div class="grid-4">
                        <div class="form-group"><label>किसान का पूर्ण नाम *</label><input type="text" id="kName" required></div>
                        <div class="form-group"><label>पता (Address)</label><input type="text" id="kAddress"></div>
                        <div class="form-group">
                            <label>राज्य (State) *</label>
                            <select id="kState" required>
                                <option value="CG">Chhattisgarh (CG)</option>
                                <option value="MP">Madhya Pradesh (MP)</option>
                                <option value="UP">Uttar Pradesh (UP)</option>
                                <option value="MH">Maharashtra (MH)</option>
                                <option value="BR">Bihar (BR)</option>
                                <option value="RJ">Rajasthan (RJ)</option>
                            </select>
                        </div>
                        <div class="form-group"><label>मोबाइल नंबर *</label><input type="text" id="kMobile" required></div>
                        <div class="form-group"><label>सरकारी ID नंबर</label><input type="text" id="kId"></div>
                    </div>
                    <button type="submit" class="btn btn-primary">💾 किसान का डेटा सुरक्षित करें</button>
                </form>
            </div>
            <div class="card">
                <div class="card-title">दर्ज किसानों की सूची <input type="text" placeholder="🔍 खोजें..." style="width:200px; font-weight:normal;" onkeyup="filterTable('t-kisan', this.value)"></div>
                <div class="table-wrap">
                    <table id="t-kisan">
                        <thead><tr><th>ऑटो खाता संख्या</th><th>पूर्ण नाम</th><th>राज्य</th><th>पता</th><th>मोबाइल</th><th>ID नंबर</th><th>करंट बैलेंस</th><th>क्रियाएं</th></tr></thead>
                        <tbody id="b-kisan"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <div id="v-company" class="view-pane hidden">
            <div class="card">
                <div class="card-title">🏢 कंपनी का नया विवरण दर्ज करें</div>
                <form id="f-company" onsubmit="submitCompany(event)">
                    <input type="hidden" id="companyEditIdx">
                    <div class="grid-4">
                        <div class="form-group"><label>पार्टी (कंपनी) का पूर्ण नाम *</label><input type="text" id="cName" required></div>
                        <div class="form-group"><label>कंपनी पता</label><input type="text" id="cAddress"></div>
                        <div class="form-group">
                            <label>राज्य (State) *</label>
                            <select id="cState" required>
                                <option value="CG">Chhattisgarh (CG)</option>
                                <option value="MP">Madhya Pradesh (MP)</option>
                                <option value="UP">Uttar Pradesh (UP)</option>
                                <option value="MH">Maharashtra (MH)</option>
                                <option value="BR">Bihar (BR)</option>
                                <option value="RJ">Rajasthan (RJ)</option>
                            </select>
                        </div>
                        <div class="form-group"><label>मोबाइल नंबर</label><input type="text" id="cMobile"></div>
                        <div class="form-group"><label>GST नंबर</label><input type="text" id="cGst"></div>
                    </div>
                    <div class="form-group"><label>बैंक विवरण (Account Details)</label><input type="text" id="cBank"></div>
                    <button type="submit" class="btn btn-primary">💾 कंपनी डेटा सुरक्षित करें</button>
                </form>
            </div>
            <div class="card">
                <div class="card-title">दर्ज कंपनियों की सूची <input type="text" placeholder="🔍 खोजें..." style="width:200px;" onkeyup="filterTable('t-company', this.value)"></div>
                <div class="table-wrap">
                    <table id="t-company">
                        <thead><tr><th>ऑटो कंपनी ID</th><th>कंपनी नाम</th><th>राज्य</th><th>पता</th><th>GST नंबर</th><th>बैंक डिटेल्स</th><th>बैलेंस राशि</th><th>क्रियाएं</th></tr></thead>
                        <tbody id="b-company"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <div id="v-items" class="view-pane hidden">
            <div class="card">
                <div class="card-title">📦 ITEM का मास्टर विवरण बनाएं</div>
                <form id="f-item" onsubmit="submitItem(event)">
                    <input type="hidden" id="itemEditIdx">
                    <div class="grid-4">
                        <div class="form-group"><label>ITEM का नाम *</label><input type="text" id="iName" required></div>
                        <div class="form-group"><label>UNITE (यूनिट - बैग/लीटर/किग्रा)</label><input type="text" id="iUnit" value="Bag"></div>
                        <div class="form-group"><label>HSN कोड</label><input type="text" id="iHsn"></div>
                        <div class="form-group"><label>TAX RATE (%)</label><input type="number" id="iTax" value="18"></div>
                    </div>
                    <button type="submit" class="btn btn-primary">➕ आइटम सुरक्षित करें</button>
                </form>
            </div>
            <div class="card">
                <div class="card-title">मल्टीप्ले आइटम लिस्ट स्टॉक विवरण</div>
                <div class="table-wrap">
                    <table id="t-items">
                        <thead><tr><th>Item नाम</th><th>यूनिट (Unit)</th><th>HSN कोड</th><th>Tax %</th><th>क्रियाएं</th></tr></thead>
                        <tbody id="b-items"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <div id="v-purchase" class="view-pane hidden">
            <div class="card">
                <div class="card-title">📥 PURCHASE विवरण फॉर्म (आवक एंट्री)</div>
                <form id="f-purchase" onsubmit="submitPurchaseInvoice(event)">
                    <div class="grid-4">
                        <div class="form-group"><label>तारीख (Date)</label><input type="date" id="pDate" required></div>
                        <div class="form-group"><label>सप्लायर इनवॉइस नंबर (Auto)</label><input type="text" id="pInvNo" readonly></div>
                        <div class="form-group"><label>वाहन नंबर (Vehicle)</label><input type="text" id="pVehicle"></div>
                        <div class="form-group"><label>कंपनी / किसान का चयन करें *</label><select id="pParty" required></select></div>
                    </div>
                    
                    <div style="background:#f4f6f7; padding:15px; border-radius:4px; margin:10px 0;">
                        <h4 style="margin-bottom:10px; color:var(--primary);">मल्टी आइटम जोड़े (Add Items)</h4>
                        <div class="grid-4">
                            <div class="form-group"><label>Item का नाम</label><select id="pItmSelect" onchange="autoFillItemTax('pItmSelect','pItmTax')"></select></div>
                            <div class="form-group"><label>मात्रा (Quantity)</label><input type="number" id="pItmQty" value="1"></div>
                            <div class="form-group"><label>रेट (Rate)</label><input type="number" id="pItmRate" value="0"></div>
                            <div class="form-group"><label>GST Tax (%)</label><input type="number" id="pItmTax" value="18"></div>
                        </div>
                        <div class="grid-4">
                            <div class="form-group"><label>बैच नंबर (BATCH NO.) *</label><input type="text" id="pItmBatch" value="B-01"></div>
                            <div class="form-group"><label>MFG डेट</label><input type="date" id="pItmMfg"></div>
                            <div class="form-group"><label>EXP डेट</label><input type="date" id="pItmExp"></div>
                            <div class="form-group"><label>&nbsp;</label><button type="button" class="btn btn-secondary" onclick="addItemToTempBill('pur')">➕ आइटम लिस्ट में जोड़े</button></div>
                        </div>
                    </div>
                    
                    <table style="margin-top:10px;">
                        <thead><tr><th>Item नाम</th><th>Qty</th><th>Rate</th><th>Tax%</th><th>Batch</th><th>Total</th><th>हटाएं</th></tr></thead>
                        <tbody id="tempPurTableBody"></tbody>
                    </table>
                    <div style="text-align:right; font-size:16px; font-weight:bold; margin:10px 0;">कुल परचेस राशि: ₹<span id="purTotalLabel">0.00</span></div>
                    <button type="submit" class="btn btn-primary">💾 Purchase इनवॉइस सुरक्षित करें</button>
                </form>
            </div>
            <div class="card">
                <div class="card-title">सुरक्षित परचेस बिलों की सूची (Purchase List)</div>
                <div class="table-wrap">
                    <table>
                        <tbody id="b-purList"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <div id="v-sale" class="view-pane hidden">
            <div class="card">
                <div class="card-title">📤 SALE विवरण फॉर्म (बिक्री बिलिंग)</div>
                <form id="f-sale" onsubmit="submitSaleInvoice(event)">
                    <div class="grid-4">
                        <div class="form-group"><label>तारीख (Date)</label><input type="date" id="sDate" required></div>
                        <div class="sInvNo"><label>इनवॉइस नं (Auto Number)</label><input type="text" id="sInvNo" readonly></div>
                        <div class="form-group"><label>वाहन नंबर</label><input type="text" id="sVehicle"></div>
                        <div class="form-group"><label>क्रेता (किसान/कंपनी चुनें) *</label><select id="sParty" required></select></div>
                    </div>
                    <div class="grid-2">
                        <div class="form-group"><label>GST विकल्प</label>
                            <select id="sGstOption"><option value="exclude">GST अलग से जोड़ें (Exclude)</option><option value="include">GST टैक्स शामिल (Include)</option></select>
                        </div>
                    </div>

                    <div style="background:#fffde7; padding:15px; border-radius:4px; margin:10px 0; border:1px solid #fff59d;">
                        <h4 style="margin-bottom:10px; color:var(--dark);">आइटम बिक्री विवरण (Batch selection enabled)</h4>
                        <div class="grid-4">
                            <div class="form-group"><label>Item का नाम</label><select id="sItmSelect" onchange="loadAvailableBatches()"></select></div>
                            <div class="form-group"><label>उपलब्ध बैच (Batch No) *</label><select id="sBatchSelect" onchange="fillDatesFromBatch()"></select></div>
                            <div class="form-group"><label>मात्रा (Quantity)</label><input type="number" id="sItmQty" value="1"></div>
                            <div class="form-group"><label>बिक्री दर (Rate)</label><input type="number" id="sItmRate" value="0"></div>
                        </div>
                        <div class="grid-4">
                            <div class="form-group"><label>GST Tax (%)</label><input type="number" id="sItmTax" value="18" readonly></div>
                            <div class="form-group"><label>MFG डेट (Auto)</label><input type="text" id="sItmMfg" readonly style="background:#eee;"></div>
                            <div class="form-group"><label>EXP डेट (Auto)</label><input type="text" id="sItmExp" readonly style="background:#eee;"></div>
                            <div class="form-group"><label>&nbsp;</label><button type="button" class="btn btn-secondary" onclick="addItemToTempBill('sale')">➕ बिक्री लिस्ट में जोड़ें</button></div>
                        </div>
                    </div>

                    <table style="margin-top:10px;">
                        <thead><tr><th>Item नाम</th><th>Qty</th><th>Rate</th><th>Tax%</th><th>Batch</th><th>Total</th><th>हटाएं</th></tr></thead>
                        <tbody id="tempSaleTableBody"></tbody>
                    </table>
                    <div style="text-align:right; font-size:16px; font-weight:bold; margin:10px 0;">कुल net सेल राशि: ₹<span id="saleTotalLabel">0.00</span></div>
                    <button type="submit" class="btn btn-primary">💾 GST सेल बिल सुरक्षित एवं जनरेट करें</button>
                </form>
            </div>
            <div class="card">
                <div class="card-title">बिक्री बिलों की सूची (Sales Summary List)</div>
                <div class="table-wrap">
                    <table>
                       <tbody id="b-saleList"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <div id="v-payment" class="view-pane hidden">
            <div class="card">
                <div class="card-title">💸 PAYMENT विवरण वाउचर (राशि भुगतान)</div>
                <form id="f-payment" onsubmit="submitPayment(event)">
                    <div class="grid-4">
                        <div class="form-group"><label>तारीख</label><input type="date" id="payDate" required></div>
                        <div class="form-group"><label>वाउचर नंबर (Auto)</label><input type="text" id="payVno" readonly></div>
                        <div class="form-group"><label>किसान / कंपनी चयन करें *</label><select id="payParty" onchange="showCurrentBalance(this.value, 'payBalLabel')" required></select></div>
                        <div class="form-group"><label>वर्तमान देय राशि: <span id="payBalLabel" style="font-weight:bold; color:var(--danger);">₹0.00</span></label></div>
                    </div>
                    <div class="grid-2">
                        <div class="form-group"><label>भुगतान राशि (₹) *</label><input type="number" id="payAmount" required></div>
                        <div class="form-group"><label>पूर्ण भुगतान विवरण / रिमार्क</label><input type="text" id="payRemark"></div>
                    </div>
                    <button type="submit" class="btn btn-primary">💾 पेमेंट वाउचर सेव और प्रिंट करें</button>
                </form>
            </div>
            <div class="card">
                <div class="card-title">पेमेंट हिस्ट्री रिकॉर्ड</div>
                <div class="table-wrap">
                    <table>
                        <thead><tr><th>वाउचर नंबर</th><th>तारीख</th><th>पार्टी का नाम</th><th>भुगतान राशि</th><th>प्रिंट</th></tr></thead>
                        <tbody id="b-payList"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <div id="v-receipt" class="view-pane hidden">
            <div class="card">
                <div class="card-title">🧾 RECIEPT विवरण वाउचर (राशि प्राप्ति)</div>
                <form id="f-receipt" onsubmit="submitReceipt(event)">
                    <input type="hidden" id="receiptEditIdx">
                    <div class="grid-4">
                        <div class="form-group"><label>तारीख</label><input type="date" id="recDate" required></div>
                        <div class="form-group"><label>प्राप्ति रसीद नं (Auto)</label><input type="text" id="recVno" readonly></div>
                        <div class="form-group"><label>किसान / कंपनी का चयन करें *</label><select id="recParty" onchange="showCurrentBalance(this.value, 'recBalLabel')" required></select></div>
                        <div class="form-group"><label>वर्तमान बकाया राशि: <span id="recBalLabel" style="font-weight:bold; color:var(--primary);">₹0.00</span></label></div>
                    </div>
                    <div class="grid-2">
                        <div class="form-group"><label>प्राप्त राशि (₹) *</label><input type="number" id="recAmount" required></div>
                        <div class="form-group"><label>प्राप्ति विवरण (Remark)</label><input type="text" id="recRemark"></div>
                    </div>
                    <button type="submit" class="btn btn-primary">💾 प्राप्ति रसीद सुरक्षित करें</button>
                </form>
            </div>
            <div class="card">
                <div class="card-title">प्राप्ति रसीद रिकॉर्ड सूची <input type="text" id="searchReceiptInput" placeholder="🔍 रसीद / पार्टी खोजें..." style="width:220px; margin-left:10px; font-weight:normal;" onkeyup="filterTable('t-recList', this.value)"></div>
                <div class="table-wrap">
                    <table id="t-recList">
                        <thead><tr><th>रसीद संख्या</th><th>तारीख</th><th>पार्टी का नाम</th><th>प्राप्त राशि</th><th>विवरण</th><th>एक्शन</th></tr></thead>
                        <tbody id="b-recList"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <div id="v-reports" class="view-pane hidden">
            <div class="card no-print">
                <div class="card-title">📊 PROFIT & LOSS (लाभ एवं हानि खाता विवरण)</div>
                <div class="grid-2" style="background:#e8f5e9; padding:20px; text-align:center; border-radius:4px;">
                    <div><h4 style="color:#2e7d32;">कुल बिक्री व्यापार राशि (+)</h4><h2 id="plTotalSale">₹0.00</h2></div>
                    <div><h4 style="color:#c62828;">कुल खरीदी लागत राशि (-)</h4><h2 id="plTotalPur">₹0.00</h2></div>
                </div>
                <div style="text-align:center; padding:15px 0;">
                    <h3>शुद्ध व्यापार लाभ / हानि स्थिति: <span id="plNetCalculated" style="color:var(--primary)">₹0.00</span></h3>
                </div>
            </div>

            <div class="card ledger-card">
                <div class="card-title no-print">📑 किसान / कंपनी विशिष्ट खाता लेजर (Ledger Detail)</div>
                <div class="grid-4 no-print">
                    <div class="form-group"><label>पार्टी खाता चुनें</label><select id="ledgerPartySelect"></select></div>
                    <div class="form-group"><label>&nbsp;</label><button class="btn btn-secondary" onclick="generateLedgerView()">🔍 लेजर विवरण खोजें</button></div>
                    <div class="form-group"><label>&nbsp;</label><button class="btn btn-primary" onclick="window.print()">🖨️ लेजर प्रिंट पेज सेटअप</button></div>
                </div>

                <div id="ledgerPrintCanvas" style="margin-top:20px; background:#fff; padding:15px; border:1px solid #ccc;">
                    <div style="text-align:center; margin-bottom:15px;">
                        <h2 id="lpFirmName" style="color:var(--primary);">लक्ष्मी कृषि केंद्र</h2>
                        <p id="lpFirmSub">मंडी प्रांगण, रायपुर | GSTIN: 22ABCDE1234F1Z0</p>
                        <h4 style="margin-top:10px; background:#f0f2f5; padding:5px;">पार्टी ट्रांजैक्शन लेजर STATEMENT (Ledger Detail)</h4>
                    </div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:10px; font-weight:600; font-size:14px;">
                        <div>पार्टी नाम: <span id="lpPartyName">---</span></div>
                        <div>करंट क्लोजिंग बैलेंस: <span id="lpPartyClosing" style="color:var(--danger);">₹0.00</span></div>
                    </div>
                    <div class="table-wrap">
                        <table>
                            <thead><tr><th>तारीख</th><th>विवरण प्रकार</th><th>इनवॉइस/वाउचर नं</th><th>डेबिट (नाम राशि) ₹</th><th>क्रेडिट (जमा राशि) ₹</th><th>दौड़ता शेष (Balance)</th></tr></thead>
                            <tbody id="b-ledgerRows"></tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <div id="invoiceModal" class="hidden">
        <div class="invoice-box">
            <div class="no-print" style="display: flex; justify-content: flex-end; gap: 10px; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 1px solid #eee;">
                <button class="btn btn-primary" onclick="window.print()">🖨️ प्रिंट / PDF सेव करें</button>
                <button class="btn btn-danger" onclick="closeInvoiceModal()">❌ बंद करें</button>
            </div>
            
            <div id="invoicePrintArea">
                <div style="display:flex; justify-content:space-between; border-bottom:2px solid #333; padding-bottom:10px;">
                    <div>
                        <h1 id="invFirm" style="color:var(--primary); font-size:24px;">लक्ष्मी कृषि केंद्र</h1>
                        <p id="invFirmDetails">पता: मंडी प्रांगण, रायपुर<br>GSTIN: 22ABCDE1234F1Z0<br>मोबाइल: 9827100000</p>
                    </div>
                    <div style="text-align:right;">
                        <h2 style="color:#555;">TAX INVOICE</h2>
                        <p><b>इनवॉइस / वाउचर संख्या:</b> <span id="invNoText">--</span><br><b>तारीख:</b> <span id="invDateText">--</span><br><b>वाहन नं:</b> <span id="invVehicleText">--</span></p>
                    </div>
                </div>

                <div style="margin:15px 0; background:#f9f9f9; padding:10px; border:1px solid #ddd;">
                    <h4>बिल प्राप्तकर्ता (Bill To):</h4>
                    <p id="invPartyDetails">ग्राहक/पार्टी का नाम: --<br>पता: --<br>मोबाइल / ID: --</p>
                </div>

                <table style="width:100%; margin-top:15px; border-collapse:collapse;">
                    <thead>
                        <tr style="background:#f2f2f2;">
                            <th>क्र.</th><th>Item विवरण</th><th>Batch No</th><th>Qty</th><th>दर (Rate)</th><th>CGST</th><th>SGST</th><th>IGST</th><th>कुल राशि (₹)</th>
                        </tr>
                    </thead>
                    <tbody id="invItemsBody"></tbody>
                </table>

                <div style="margin-top:20px; display:flex; justify-content:space-between; align-items:flex-start;">
                    <div style="width:55%;">
                        <p id="invAmountWords" style="font-style:italic; font-weight:600; color:#555;"></p>
                    </div>
                    <div style="width:40%; text-align:right;">
                        <p>टैक्सेबल वैल्यू: ₹<span id="invTaxable">0.00</span></p>
                        <p>CGST राशि: ₹<span id="invCgst">0.00</span></p>
                        <p>SGST राशि: ₹<span id="invSgst">0.00</span></p>
                        <p>IGST राशि: ₹<span id="invIgst">0.00</span></p>
                        <hr style="margin:5px 0;">
                        <h3>कुल देय राशि (Grand Total): ₹<span id="invGrandTotal">0.00</span></h3>
                    </div>
                </div>

                <div style="margin-top:40px; display:flex; justify-content:space-between;">
                    <div>पार्टी के हस्ताक्षर</div>
                    <div style="text-align:right;">कृते, <span id="invFirmSign">फर्म का नाम</span><br><br><br><b>अधिकृत हस्ताक्षरकर्ता</b></div>
                </div>
            </div>
        </div>
    </div>

    <div id="receiptModal" class="hidden">
        <div class="invoice-box" style="max-width: 550px; border: 2px solid #1b5e20;">
            <div class="no-print" style="display: flex; justify-content: flex-end; gap: 8px; margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid #eee;">
                <button class="btn btn-primary btn-sm" onclick="window.print()">🖨️ प्रिंट करें</button>
                <button class="btn btn-whatsapp btn-sm" id="btnReceiptWhatsApp" onclick="">💬 WhatsApp</button>
                <button class="btn btn-danger btn-sm" onclick="closeReceiptModal()">❌ बंद करें</button>
            </div>
            <div id="receiptPrintArea" style="text-align:center; padding:10px;">
                <h2 id="recModalFirm" style="color:var(--primary);">लक्ष्मी कृषि सेवा केंद्र</h2>
                <p id="recModalFirmDetails">नवीन मंडी परिसर, रायपुर</p>
                <hr style="margin:10px 0; border:1px solid #1b5e20;">
                <h3 style="background:#e8f5e9; padding:5px; margin-bottom:15px;">प्राप्ति रसीद (RECEIPT VOUCHER)</h3>
                
                <table style="width:100%; font-size:14px; text-align:left; margin-bottom:15px;">
                    <tr><td style="border:none; padding:5px;"><b>रसीद संख्या:</b></td><td style="border:none; padding:5px;" id="rmVno">--</td></tr>
                    <tr><td style="border:none; padding:5px;"><b>तारीख (Date):</b></td><td style="border:none; padding:5px;" id="rmDate">--</td></tr>
                    <tr><td style="border:none; padding:5px;"><b>प्राप्तकर्ता नाम:</b></td><td style="border:none; padding:5px;" id="rmParty">--</td></tr>
                    <tr><td style="border:none; padding:5px;"><b>प्राप्त राशि:</b></td><td style="border:none; padding:5px; font-size:16px; color:var(--primary);"><b>₹<span id="rmAmt">0.00</span></b></td></tr>
                    <tr><td style="border:none; padding:5px;"><b>विवरण (Remark):</b></td><td style="border:none; padding:5px;" id="rmRemark">--</td></tr>
                    <tr><td style="border:none; padding:5px;"><b>शेष बकाया खाता बैलेंस:</b></td><td style="border:none; padding:5px; font-weight:bold;" id="rmBalance">₹0.00</td></tr>
                </table>
                <hr style="margin-top:20px; border:1px dashed #ccc;">
                <div style="margin-top:30px; display:flex; justify-content:space-between; font-size:12px;">
                    <div>हस्ताक्षरकर्ता ग्राहक</div>
                    <div>कृते, प्राधिकृत अधिकारी</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Local DB Init
        let dataStore = {
            profile: { name: "लक्ष्मी कृषि सेवा केंद्र", address: "नवीन मंडी परिसर, रायपुर (छ.ग.)", state: "CG", gst: "22ABCDE1234F1Z0", mobile: "9827112345" },
            kisan: [],
            company: [],
            items: [],
            purchase: [],
            sale: [],
            payments: [],
            receipts: []
        };

        let tempPurItems = [];
        let tempSaleItems = [];

        window.onload = function() {
            if(localStorage.getItem('krishi_vyapar_advanced_db')) {
                dataStore = JSON.parse(localStorage.getItem('krishi_vyapar_advanced_db'));
                if(!dataStore.profile.state) dataStore.profile.state = "CG"; 
            }
            refreshAllData();
        };

        function syncDB() {
            localStorage.setItem('krishi_vyapar_advanced_db', JSON.stringify(dataStore));
            calculateDashboardMetrics();
        }

        function refreshAllData() {
            document.getElementById('viewFirmName').innerText = dataStore.profile.name;
            document.getElementById('viewAddress').innerText = dataStore.profile.address;
            document.getElementById('viewState').innerText = dataStore.profile.state;
            document.getElementById('viewGst').innerText = dataStore.profile.gst;
            document.getElementById('viewMob').innerText = dataStore.profile.mobile;

            populatePartyDropdowns();
            populateItemDropdowns();

            renderKisanTable();
            renderCompanyTable();
            renderItemTable();
            renderPurchaseList();
            renderSaleList();
            renderPaymentList();
            renderReceiptList();

            setAutoControlNumbers();
            calculateDashboardMetrics();
        }

        function setAutoControlNumbers() {
            document.getElementById('pInvNo').value = "PUR-" + (dataStore.purchase.length + 5001);
            document.getElementById('sInvNo').value = "SAL-" + (dataStore.sale.length + 7001);
            document.getElementById('payVno').value = "PAY-" + (dataStore.payments.length + 1001);
            
            let idx = document.getElementById('receiptEditIdx').value;
            if(idx === "") {
                document.getElementById('recVno').value = "REC-" + (dataStore.receipts.length + 2001);
            }

            let d = new Date().toISOString().split('T')[0];
            document.getElementById('pDate').value = d;
            document.getElementById('sDate').value = d;
            document.getElementById('payDate').value = d;
            if(idx === "") document.getElementById('recDate').value = d;
        }

        // --- AUTH LOGIC ---
        function switchAuth(mode) {
            document.getElementById('box-login').classList.add('hidden');
            document.getElementById('box-register').classList.add('hidden');
            document.getElementById('box-forgot').classList.add('hidden');
            document.getElementById('box-' + mode).classList.remove('hidden');
        }
        function handleLogin() {
            let u = document.getElementById('loginUser').value;
            let p = document.getElementById('loginPass').value;
            if(u === 'admin' && p === '1234') {
                document.getElementById('authContainer').classList.add('hidden');
            } else { alert("गलत आईडी या पासवर्ड!"); }
        }
        function handleRegister() { alert("नया यूज़र रजिस्टर कर दिया गया है! अब लॉगिन करें।"); switchAuth('login'); }
        function handleForgot() { alert("आपका पासवर्ड डिफ़ॉल्ट '1234' पर्ट सेट कर दिया गया है।"); switchAuth('login'); }
        function logout() { document.getElementById('authContainer').classList.remove('hidden'); }

        // --- PROFILE LOGIC ---
        function toggleProfileForm() {
            let el = document.getElementById('profileEditCard');
            el.classList.toggle('hidden');
            if(!el.classList.contains('hidden')) {
                document.getElementById('setFirmName').value = dataStore.profile.name;
                document.getElementById('setAddress').value = dataStore.profile.address;
                document.getElementById('setInitialState').value = dataStore.profile.state || "CG";
                document.getElementById('setGst').value = dataStore.profile.gst;
                document.getElementById('setMob').value = dataStore.profile.mobile;
            }
        }
        function saveFirmProfile() {
            dataStore.profile.name = document.getElementById('setFirmName').value;
            dataStore.profile.address = document.getElementById('setAddress').value;
            dataStore.profile.state = document.getElementById('setInitialState').value;
            dataStore.profile.gst = document.getElementById('setGst').value;
            dataStore.profile.mobile = document.getElementById('setMob').value;
            syncDB();
            refreshAllData();
            document.getElementById('profileEditCard').classList.add('hidden');
        }

        // --- NAVIGATION ---
        function navTo(viewId) {
            document.querySelectorAll('.view-pane').forEach(v => v.classList.add('hidden'));
            document.querySelectorAll('.sidebar-menu a').forEach(m => m.classList.remove('active'));
            document.getElementById('v-' + viewId).classList.remove('hidden');
            document.getElementById('m-' + viewId).classList.add('active');
            
            if(viewId === 'reports') {
                document.getElementById('v-reports').classList.remove('print-invoice-mode');
                generateLedgerView();
            } else {
                document.getElementById('v-reports').classList.add('print-invoice-mode');
            }
        }

        // --- DROPDOWN POPULATION ---
        function populatePartyDropdowns() {
            let html = '<option value="">--चयन करें--</option>';
            dataStore.kisan.forEach(k => html += `<option value="${k.id}">🧑‍🌾 किसान: ${k.name} (${k.id})</option>`);
            dataStore.company.forEach(c => html += `<option value="${c.id}">🏢 कंपनी: ${c.name} (${c.id})</option>`);
            
            document.getElementById('pParty').innerHTML = html;
            document.getElementById('sParty').innerHTML = html;
            document.getElementById('payParty').innerHTML = html;
            document.getElementById('recParty').innerHTML = html;
            document.getElementById('ledgerPartySelect').innerHTML = html;
        }
        function populateItemDropdowns() {
            let html = '<option value="">--Item चुनें--</option>';
            dataStore.items.forEach(i => html += `<option value="${i.name}">${i.name}</option>`);
            document.getElementById('pItmSelect').innerHTML = html;
            document.getElementById('sItmSelect').innerHTML = html;
        }
        function autoFillItemTax(selId, taxInpId) {
            let name = document.getElementById(selId).value;
            let matched = dataStore.items.find(i => i.name === name);
            if(matched) document.getElementById(taxInpId).value = matched.tax;
        }

        // --- FINANCIAL LEDGER BALANCE RESOLVER ---
        // Sale (+ Debit), Receipt (- Credit), Purchase (- Credit), Payment (+ Debit)
        function computePartyCurrentBalance(partyId) {
            let debit = 0;
            let credit = 0;
            dataStore.sale.forEach(s => { if(s.partyId === partyId) debit += s.grandTotal; });
            dataStore.payments.forEach(pay => { if(pay.partyId === partyId) debit += pay.amount; });
            
            dataStore.purchase.forEach(p => { if(p.partyId === partyId) credit += p.grandTotal; });
            dataStore.receipts.forEach(r => { if(r.partyId === partyId) credit += r.amount; });
            
            return debit - credit;
        }

        function showCurrentBalance(partyId, labelId) {
            if(!partyId) return;
            let bal = computePartyCurrentBalance(partyId);
            document.getElementById(labelId).innerText = "₹" + bal.toFixed(2);
        }

        // --- 1. KISAN SCREEN CRUD ---
        function submitKisan(e) {
            e.preventDefault();
            let idx = document.getElementById('kisanEditIdx').value;
            let kData = {
                id: idx !== "" ? dataStore.kisan[idx].id : "KISAN-" + (dataStore.kisan.length + 1001),
                name: document.getElementById('kName').value,
                address: document.getElementById('kAddress').value,
                state: document.getElementById('kState').value,
                mobile: document.getElementById('kMobile').value,
                idCard: document.getElementById('kId').value
            };
            if(idx !== "") dataStore.kisan[idx] = kData;
            else dataStore.kisan.push(kData);
            document.getElementById('f-kisan').reset();
            document.getElementById('kisanEditIdx').value = "";
            syncDB(); refreshAllData();
        }
        function editKisan(idx) {
            let k = dataStore.kisan[idx];
            document.getElementById('kisanEditIdx').value = idx;
            document.getElementById('kName').value = k.name;
            document.getElementById('kAddress').value = k.address;
            document.getElementById('kState').value = k.state || "CG";
            document.getElementById('kMobile').value = k.mobile;
            document.getElementById('kId').value = k.idCard;
        }
        function deleteKisan(idx) { if(confirm("क्या kisan का विवरण डिलीट करना है?")) { dataStore.kisan.splice(idx,1); syncDB(); refreshAllData(); } }
        function renderKisanTable() {
            let h = '';
            dataStore.kisan.forEach((k, i) => {
                h += `<tr><td>${k.id}</td><td><b>${k.name}</b></td><td>${k.state || 'CG'}</td><td>${k.address}</td><td>${k.mobile}</td><td>${k.idCard}</td><td>₹${computePartyCurrentBalance(k.id).toFixed(2)}</td>
                <td><button class="btn btn-secondary btn-sm" onclick="editKisan(${i})">✏️</button> <button class="btn btn-danger btn-sm" onclick="deleteKisan(${i})">🗑️</button></td></tr>`;
            });
            document.getElementById('b-kisan').innerHTML = h;
        }

        // --- 2. COMPANY SCREEN CRUD ---
        function submitCompany(e) {
            e.preventDefault();
            let idx = document.getElementById('companyEditIdx').value;
            let cData = {
                id: idx !== "" ? dataStore.company[idx].id : "COMP-" + (dataStore.company.length + 2001),
                name: document.getElementById('cName').value,
                address: document.getElementById('cAddress').value,
                state: document.getElementById('cState').value,
                mobile: document.getElementById('cMobile').value,
                gst: document.getElementById('cGst').value,
                bank: document.getElementById('cBank').value
            };
            if(idx !== "") dataStore.company[idx] = cData;
            else dataStore.company.push(cData);
            document.getElementById('f-company').reset();
            document.getElementById('companyEditIdx').value = "";
            syncDB(); refreshAllData();
        }
        function editCompany(idx) {
            let c = dataStore.company[idx];
            document.getElementById('companyEditIdx').value = idx;
            document.getElementById('cName').value = c.name;
            document.getElementById('cAddress').value = c.address;
            document.getElementById('cState').value = c.state || "CG";
            document.getElementById('cMobile').value = c.mobile;
            document.getElementById('cGst').value = c.gst;
            document.getElementById('cBank').value = c.bank;
        }
        function deleteCompany(idx) { if(confirm("डिलीट करना है?")) { dataStore.company.splice(idx,1); syncDB(); refreshAllData(); } }
        function renderCompanyTable() {
            let h = '';
            dataStore.company.forEach((c, i) => {
                h += `<tr><td>${c.id}</td><td><b>${c.name}</b></td><td>${c.state || 'CG'}</td><td>${c.address}</td><td>${c.gst}</td><td>${c.bank}</td><td>₹${computePartyCurrentBalance(c.id).toFixed(2)}</td>
                <td><button class="btn btn-secondary btn-sm" onclick="editCompany(${i})">✏️</button> <button class="btn btn-danger btn-sm" onclick="deleteCompany(${i})">🗑️</button></td></tr>`;
            });
            document.getElementById('b-company').innerHTML = h;
        }

        // --- 3. ITEM SCREEN CRUD ---
        function submitItem(e) {
            e.preventDefault();
            let idx = document.getElementById('itemEditIdx').value;
            let iData = {
                name: document.getElementById('iName').value,
                unit: document.getElementById('iUnit').value,
                hsn: document.getElementById('iHsn').value,
                tax: parseFloat(document.getElementById('iTax').value) || 0
            };
            if(idx !== "") dataStore.items[idx] = iData;
            else dataStore.items.push(iData);
            document.getElementById('f-item').reset();
            document.getElementById('itemEditIdx').value = "";
            syncDB(); refreshAllData();
        }
        function editItem(idx) {
            let i = dataStore.items[idx];
            document.getElementById('itemEditIdx').value = idx;
            document.getElementById('iName').value = i.name;
            document.getElementById('iUnit').value = i.unit;
            document.getElementById('iHsn').value = i.hsn;
            document.getElementById('iTax').value = i.tax;
        }
        function deleteItem(idx) { dataStore.items.splice(idx,1); syncDB(); refreshAllData(); }
        function renderItemTable() {
            let h = '';
            dataStore.items.forEach((i, idx) => {
                h += `<tr><td><b>${i.name}</b></td><td>${i.unit}</td><td>${i.hsn}</td><td>${i.tax}%</td>
                <td><button class="btn btn-secondary btn-sm" onclick="editItem(${idx})">✏️</button> <button class="btn btn-danger btn-sm" onclick="deleteItem(${idx})">🗑️</button></td></tr>`;
            });
            document.getElementById('b-items').innerHTML = h;
        }

        // --- BATCH SYNCHRONIZATION FROM PURCHASE TO SALE ---
        function loadAvailableBatches() {
            let itmName = document.getElementById('sItmSelect').value;
            let batchSelect = document.getElementById('sBatchSelect');
            batchSelect.innerHTML = '';
            let foundBatches = [];
            dataStore.purchase.forEach(p => {
                p.items.forEach(itm => {
                    if(itm.name === itmName) { foundBatches.push(itm); }
                });
            });
            if(foundBatches.length === 0) {
                batchSelect.innerHTML = '<option value="Standard">Standard Batch</option>';
            } else {
                foundBatches.forEach(b => {
                    batchSelect.innerHTML += `<option value="${b.batch}" data-mfg="${b.mfg}" data-exp="${b.exp}" data-rate="${b.rate}" data-tax="${b.tax}">${b.batch} (Mfg: ${b.mfg})</option>`;
                });
            }
            fillDatesFromBatch();
        }

        function fillDatesFromBatch() {
            let sel = document.getElementById('sBatchSelect');
            if(sel.options.length === 0) return;
            let opt = sel.options[sel.selectedIndex];
            document.getElementById('sItmMfg').value = opt.getAttribute('data-mfg') || 'N/A';
            document.getElementById('sItmExp').value = opt.getAttribute('data-exp') || 'N/A';
            document.getElementById('sItmRate').value = opt.getAttribute('data-rate') || 0;
            document.getElementById('sItmTax').value = opt.getAttribute('data-tax') || 18;
        }

        // --- INVOICE MULTIITEM ADDING LOGIC ---
        function addItemToTempBill(type) {
            if(type === 'pur') {
                let name = document.getElementById('pItmSelect').value;
                let qty = parseFloat(document.getElementById('pItmQty').value) || 0;
                let rate = parseFloat(document.getElementById('pItmRate').value) || 0;
                let tax = parseFloat(document.getElementById('pItmTax').value) || 0;
                let batch = document.getElementById('pItmBatch').value;
                let mfg = document.getElementById('pItmMfg').value || 'N/A';
                let exp = document.getElementById('pItmExp').value || 'N/A';
                if(!name) return alert("Item select karein");
                let tot = qty * rate * (1 + tax/100);
                tempPurItems.push({ name, qty, rate, tax, batch, mfg, exp, total: tot });
                renderTempBillTable('pur');
            } else {
                let name = document.getElementById('sItmSelect').value;
                let qty = parseFloat(document.getElementById('sItmQty').value) || 0;
                let rate = parseFloat(document.getElementById('sItmRate').value) || 0;
                let tax = parseFloat(document.getElementById('sItmTax').value) || 0;
                let batch = document.getElementById('sBatchSelect').value;
                let mfg = document.getElementById('sItmMfg').value;
                let exp = document.getElementById('sItmExp').value;
                let gstOption = document.getElementById('sGstOption').value;
                if(!name) return alert("Item select karein");
                let tot = qty * rate;
                if(gstOption === 'exclude') { tot = tot * (1 + tax/100); }
                tempSaleItems.push({ name, qty, rate, tax, batch, mfg, exp, total: tot });
                renderTempBillTable('sale');
            }
        }

        function renderTempBillTable(type) {
            let html = ''; let total = 0;
            let list = type === 'pur' ? tempPurItems : tempSaleItems;
            list.forEach((item, i) => {
                total += item.total;
                html += `<tr><td>${item.name}</td><td>${item.qty}</td><td>₹${item.rate}</td><td>${item.tax}%</td><td>${item.batch}</td><td>₹${item.total.toFixed(2)}</td><td><button type="button" onclick="removeTempItem('${type}', ${i})">❌</button></td></tr>`;
            });
            document.getElementById(type === 'pur' ? 'tempPurTableBody' : 'tempSaleTableBody').innerHTML = html;
            document.getElementById(type === 'pur' ? 'purTotalLabel' : 'saleTotalLabel').innerText = total.toFixed(2);
        }

        function removeTempItem(type, i) {
            if(type === 'pur') { tempPurItems.splice(i,1); renderTempBillTable('pur'); }
            else { tempSaleItems.splice(i,1); renderTempBillTable('sale'); }
        }

        // --- SUBMIT INVOICES ---
        function submitPurchaseInvoice(e) {
            e.preventDefault();
            if(tempPurItems.length === 0) return alert("List khali hai");
            dataStore.purchase.push({
                invNo: document.getElementById('pInvNo').value,
                date: document.getElementById('pDate').value,
                vehicle: document.getElementById('pVehicle').value,
                partyId: document.getElementById('pParty').value,
                items: tempPurItems,
                grandTotal: parseFloat(document.getElementById('purTotalLabel').innerText)
            });
            tempPurItems = []; renderTempBillTable('pur');
            document.getElementById('f-purchase').reset();
            syncDB(); refreshAllData();
        }

        function submitSaleInvoice(e) {
            e.preventDefault();
            if(tempSaleItems.length === 0) return alert("List khali hai");
            let invNum = document.getElementById('sInvNo').value;
            dataStore.sale.push({
                invNo: invNum,
                date: document.getElementById('sDate').value,
                vehicle: document.getElementById('sVehicle').value,
                partyId: document.getElementById('sParty').value,
                items: tempSaleItems,
                grandTotal: parseFloat(document.getElementById('saleTotalLabel').innerText)
            });
            tempSaleItems = []; renderTempBillTable('sale');
            document.getElementById('f-sale').reset();
            syncDB(); refreshAllData();
            openInvoicePrintView('sale', invNum);
        }

        // --- PAYMENT & RECEIPTS ---
        function submitPayment(e) {
            e.preventDefault();
            let vNo = document.getElementById('payVno').value;
            dataStore.payments.push({
                vNo: vNo,
                date: document.getElementById('payDate').value,
                partyId: document.getElementById('payParty').value,
                amount: parseFloat(document.getElementById('payAmount').value),
                remark: document.getElementById('payRemark').value
            });
            document.getElementById('f-payment').reset();
            syncDB(); refreshAllData();
            alert("पेमेंट वाउचर प्रिंट के लिए तैयार है!");
        }

        function submitReceipt(e) {
            e.preventDefault();
            let idx = document.getElementById('receiptEditIdx').value;
            let vNo = document.getElementById('recVno').value;
            let pid = document.getElementById('recParty').value;
            let amt = parseFloat(document.getElementById('recAmount').value);
            let rem = document.getElementById('recRemark').value;
            let dt = document.getElementById('recDate').value;

            let rData = { vNo: vNo, date: dt, partyId: pid, amount: amt, remark: rem };

            if(idx !== "") {
                dataStore.receipts[idx] = rData;
                document.getElementById('receiptEditIdx').value = "";
            } else {
                dataStore.receipts.push(rData);
            }
            
            document.getElementById('f-receipt').reset();
            syncDB(); refreshAllData();
            openReceiptModalPopup(vNo);
        }

        // --- RECEIPT MODAL POPUP ENGINE ---
        function openReceiptModalPopup(vNo) {
            let r = dataStore.receipts.find(x => x.vNo === vNo);
            if(!r) return;

            let pName = getPartyObjectName(r.partyId);
            let bal = computePartyCurrentBalance(r.partyId);
            let partyObj = dataStore.kisan.find(x => x.id === r.partyId) || dataStore.company.find(x => x.id === r.partyId);

            document.getElementById('recModalFirm').innerText = dataStore.profile.name;
            document.getElementById('recModalFirmDetails').innerText = dataStore.profile.address;
            document.getElementById('rmVno').innerText = r.vNo;
            document.getElementById('rmDate').innerText = r.date;
            document.getElementById('rmParty').innerText = pName + " (" + r.partyId + ")";
            document.getElementById('rmAmt').innerText = r.amount.toFixed(2);
            document.getElementById('rmRemark').innerText = r.remark || 'N/A';
            document.getElementById('rmBalance').innerText = "₹" + bal.toFixed(2);

            let whatsappMsg = `नमस्ते ${pName}, आपकी राशि ₹${r.amount} रसीद नं: ${r.vNo} के तहत प्राप्त हुई। आपका कुल शेष बकाया बैलेंस ₹${bal.toFixed(2)} है। धन्यवाद - ${dataStore.profile.name}`;
            let waBtn = document.getElementById('btnReceiptWhatsApp');
            
            if(partyObj && partyObj.mobile) {
                waBtn.setAttribute('onclick', `window.open('https://api.whatsapp.com/send?phone=91${partyObj.mobile}&text=${encodeURIComponent(whatsappMsg)}', '_blank')`);
            } else {
                waBtn.setAttribute('onclick', `window.open('https://api.whatsapp.com/send?text=${encodeURIComponent(whatsappMsg)}', '_blank')`);
            }

            document.getElementById('receiptModal').classList.remove('hidden');
        }

        function closeReceiptModal() { document.getElementById('receiptModal').classList.add('hidden'); }

        function editReceipt(idx) {
            let r = dataStore.receipts[idx];
            document.getElementById('receiptEditIdx').value = idx;
            document.getElementById('recVno').value = r.vNo;
            document.getElementById('recDate').value = r.date;
            document.getElementById('recParty').value = r.partyId;
            document.getElementById('recAmount').value = r.amount;
            document.getElementById('recRemark').value = r.remark;
            showCurrentBalance(r.partyId, 'recBalLabel');
            window.scrollTo(0,0);
        }

        // --- RENDERING HISTORICAL RECORD LISTS ---
        function renderPurchaseList() {
            let h = '';
            dataStore.purchase.forEach((p, i) => {
                h += `<tr><td>${p.invNo}</td><td>${p.date}</td><td>${getPartyObjectName(p.partyId)}</td><td>₹${p.grandTotal.toFixed(2)}</td>
                <td><button class="btn btn-secondary btn-sm" onclick="openInvoicePrintView('pur','${p.invNo}')">🖨️ इनवॉइस</button> <button class="btn btn-danger btn-sm" onclick="deleteTransaction('purchase', ${i})">🗑️</button></td></tr>`;
            });
            document.getElementById('b-purList').innerHTML = h;
        }
        function renderSaleList() {
            let h = '';
            dataStore.sale.forEach((s, i) => {
                h += `<tr><td>${s.invNo}</td><td>${s.date}</td><td>${getPartyObjectName(s.partyId)}</td><td>₹${s.grandTotal.toFixed(2)}</td>
                <td><button class="btn btn-secondary btn-sm" onclick="openInvoicePrintView('sale','${s.invNo}')">🖨️ GST बिल</button> <button class="btn btn-whatsapp btn-sm" onclick="triggerInvoiceWhatsApp('${s.invNo}')">💬 WhatsApp</button> <button class="btn btn-danger btn-sm" onclick="deleteTransaction('sale', ${i})">🗑️</button></td></tr>`;
            });
            document.getElementById('b-saleList').innerHTML = h;
        }
        function renderPaymentList() {
            let h = ''; dataStore.payments.forEach(p => {
                h += `<tr><td>${p.vNo}</td><td>${p.date}</td><td>${getPartyObjectName(p.partyId)}</td><td>₹${p.amount}</td><td><button class="btn btn-sm btn-secondary" onclick="alert('Voucher Number: '+p.vNo+' Printed Successfully!')">🖨️</button></td></tr>`;
            }); document.getElementById('b-payList').innerHTML = h;
        }
        function renderReceiptList() {
            let h = ''; dataStore.receipts.forEach((r, i) => {
                h += `<tr><td>${r.vNo}</td><td>${r.date}</td><td>${getPartyObjectName(r.partyId)}</td><td>₹${r.amount}</td><td>${r.remark || ''}</td>
                <td><button class="btn btn-sm btn-secondary" onclick="openReceiptModalPopup('${r.vNo}')">👁️ रसीद</button> <button class="btn btn-sm btn-primary" onclick="editReceipt(${i})">✏️ एडिट</button> <button class="btn btn-danger btn-sm" onclick="deleteTransaction('receipts', ${i})">🗑️</button></td></tr>`;
            }); document.getElementById('b-recList').innerHTML = h;
        }

        function deleteTransaction(type, i) { if(confirm("डिलीट करें?")) { dataStore[type].splice(i,1); syncDB(); refreshAllData(); } }
        function getPartyObjectName(id) {
            let m = dataStore.kisan.find(k => k.id === id) || dataStore.company.find(c => c.id === id);
            return m ? m.name : id;
        }

        // --- WHATSAPP INVOICE ENGINE ---
        function triggerInvoiceWhatsApp(invNo) {
            let bill = dataStore.sale.find(s => s.invNo === invNo);
            if(!bill) return;
            let bal = computePartyCurrentBalance(bill.partyId);
            let partyName = getPartyObjectName(bill.partyId);
            let partyObj = dataStore.kisan.find(x => x.id === bill.partyId) || dataStore.company.find(x => x.id === bill.partyId);
            
            let itemDescText = "";
            bill.items.forEach((item, index) => {
                itemDescText += `\n${index + 1}. ${item.name} | मात्रा: ${item.qty} | दर: ₹${item.rate} | टैक्स: ${item.tax}%`;
            });

            let msg = `*बिक्री इनवॉइस (GST Bill)*\n\n*कंपनी / फर्म:* ${dataStore.profile.name}\n*क्रेता (Party):* ${partyName} (${bill.partyId})\n*इनवॉइस संख्या:* ${bill.invNo}\n*तारीख:* ${bill.date}\n\n*संबद्ध ITEM का विवरण:*${itemDescText}\n\n*कुल देय राशि:* ₹${bill.grandTotal.toFixed(2)}\n*शेष क्लोजिंग बैलेंस:* ₹${bal.toFixed(2)}\n\nव्यापार करने के लिए धन्यवाद!`;
            
            if(partyObj && partyObj.mobile) {
                window.open(`https://api.whatsapp.com/send?phone=91${partyObj.mobile}&text=${encodeURIComponent(msg)}`, '_blank');
            } else {
                window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(msg)}`, '_blank');
            }
        }

        // --- GST INVOICE RENDER VIEW & POPUP MODAL ---
        function openInvoicePrintView(type, invNo) {
            let bill = dataStore[type === 'pur' ? 'purchase' : 'sale'].find(x => x.invNo === invNo);
            if(!bill) return;

            document.getElementById('invFirm').innerText = dataStore.profile.name;
            document.getElementById('invFirmDetails').innerHTML = `पता: ${dataStore.profile.address}<br>राज्य: ${dataStore.profile.state || 'CG'}<br>GSTIN: ${dataStore.profile.gst}<br>मोबाइल: ${dataStore.profile.mobile}`;
            document.getElementById('invFirmSign').innerText = dataStore.profile.name;
            document.getElementById('invNoText').innerText = bill.invNo;
            document.getElementById('invDateText').innerText = bill.date;
            document.getElementById('invVehicleText').innerText = bill.vehicle || 'N/A';

            let party = dataStore.kisan.find(k => k.id === bill.partyId) || dataStore.company.find(c => c.id === bill.partyId);
            let isInterstate = false;
            
            if(party) {
                let pState = party.state || "CG";
                let fState = dataStore.profile.state || "CG";
                if(pState !== fState) {
                    isInterstate = true;
                }
                document.getElementById('invPartyDetails').innerHTML = `<b>नाम:</b> ${party.name}<br><b>राज्य:</b> ${pState}<br><b>पता:</b> ${party.address || 'N/A'}<br><b>मो./GST:</b> ${party.mobile} / ${party.gst || 'N/A'}`;
            } else {
                document.getElementById('invPartyDetails').innerHTML = "नाम: " + bill.partyId;
            }

            let itmHtml = ''; let taxableSum = 0; let cgstSum = 0; let sgstSum = 0; let igstSum = 0;
            bill.items.forEach((item, idx) => {
                let totalAmt = item.total;
                let calculatedTaxRate = item.tax || 0;
                
                let baseValue = item.qty * item.rate;
                let taxAmount = totalAmt - baseValue;
                if(taxAmount < 0 || Math.abs(taxAmount) < 0.01) {
                    taxAmount = baseValue * (calculatedTaxRate / 100);
                } else {
                    baseValue = totalAmt / (1 + (calculatedTaxRate / 100));
                    taxAmount = totalAmt - baseValue;
                }

                taxableSum += baseValue;

                let cgstAmt = 0, sgstAmt = 0, igstAmt = 0;
                let cgstRate = 0, sgstRate = 0, igstRate = 0;

                if(isInterstate) {
                    igstAmt = taxAmount;
                    igstRate = calculatedTaxRate;
                    igstSum += igstAmt;
                } else {
                    cgstAmt = taxAmount / 2;
                    sgstAmt = taxAmount / 2;
                    cgstRate = calculatedTaxRate / 2;
                    sgstRate = calculatedTaxRate / 2;
                    cgstSum += cgstAmt;
                    sgstSum += sgstAmt;
                }

                itmHtml += `<tr>
                    <td>${idx+1}</td>
                    <td><b>${item.name}</b><br><small>Batch: ${item.batch} (${item.mfg}/${item.exp})</small></td>
                    <td>${item.batch}</td>
                    <td>${item.qty}</td>
                    <td>₹${item.rate.toFixed(2)}</td>
                    <td>₹${cgstAmt.toFixed(2)} (${cgstRate}%)</td>
                    <td>₹${sgstAmt.toFixed(2)} (${sgstRate}%)</td>
                    <td>₹${igstAmt.toFixed(2)} (${igstRate}%)</td>
                    <td><b>₹${totalAmt.toFixed(2)}</b></td>
                </tr>`;
            });

            document.getElementById('invItemsBody').innerHTML = itmHtml;
            document.getElementById('invTaxable').innerText = taxableSum.toFixed(2);
            document.getElementById('invGrandTotal').innerText = bill.grandTotal.toFixed(2);
            
            document.getElementById('invCgst').innerText = cgstSum.toFixed(2);
            document.getElementById('invSgst').innerText = sgstSum.toFixed(2);
            document.getElementById('invIgst').innerText = igstSum.toFixed(2); 
            document.getElementById('invAmountWords').innerText = "Grand Total in Words: " + convertNumberToWords(bill.grandTotal) + " Rupees Only";
            document.getElementById('invoiceModal').classList.remove('hidden');
        }

        function closeInvoiceModal() { document.getElementById('invoiceModal').classList.add('hidden'); }

        // --- LEDGER STATEMENT GENERATION ENGINE ---
        // Payment = Debit, Receipt = Credit
        function generateLedgerView() {
            let pid = document.getElementById('ledgerPartySelect').value;
            if(!pid) return;

            document.getElementById('lpFirmName').innerText = dataStore.profile.name;
            document.getElementById('lpFirmSub').innerText = `${dataStore.profile.address} | GSTIN: ${dataStore.profile.gst}`;
            document.getElementById('lpPartyName').innerText = getPartyObjectName(pid) + " (" + pid + ")";
            
            let masterLedger = [];
            dataStore.sale.forEach(s => { if(s.partyId === pid) masterLedger.push({ date: s.date, type: "बिक्री बिल (Sale)", ref: s.invNo, dr: s.grandTotal, cr: 0 }); });
            dataStore.payments.forEach(pay => { if(pay.partyId === pid) masterLedger.push({ date: pay.date, type: "भुगतान (Payment)", ref: pay.vNo, dr: pay.amount, cr: 0 }); });
            
            dataStore.purchase.forEach(p => { if(p.partyId === pid) masterLedger.push({ date: p.date, type: "परचेस आवक (Pur)", ref: p.invNo, dr: 0, cr: p.grandTotal }); });
            dataStore.receipts.forEach(r => { if(r.partyId === pid) masterLedger.push({ date: r.date, type: "प्राप्ति (Receipt)", ref: r.vNo, dr: 0, cr: r.amount }); });

            masterLedger.sort((a,b) => new Date(a.date) - new Date(b.date));

            let html = ''; let balance = 0;
            masterLedger.forEach(row => {
                balance += (row.dr - row.cr);
                html += `<tr><td>${row.date}</td><td>${row.type}</td><td>${row.ref}</td><td>₹${row.dr.toFixed(2)}</td><td>₹${row.cr.toFixed(2)}</td><td><b>₹${balance.toFixed(2)}</b></td></tr>`;
            });
            document.getElementById('b-ledgerRows').innerHTML = html || '<tr><td colspan="6">कोई रिकॉर्ड उपलब्ध नहीं है।</td></tr>';
            document.getElementById('lpPartyClosing').innerText = "₹" + computePartyCurrentBalance(pid).toFixed(2);
        }

        // --- REALTIME ANALYTICS DASHBOARD ---
        function calculateDashboardMetrics() {
            document.getElementById('d-kisan').innerText = dataStore.kisan.length;
            document.getElementById('d-company').innerText = dataStore.company.length;
            document.getElementById('d-items').innerText = dataStore.items.length;

            let pTot = dataStore.purchase.reduce((s, x) => s + x.grandTotal, 0);
            let sTot = dataStore.sale.reduce((s, x) => s + x.grandTotal, 0);
            let payTot = dataStore.payments.reduce((s, x) => s + x.amount, 0);
            let recTot = dataStore.receipts.reduce((s, x) => s + x.amount, 0);

            document.getElementById('d-purchase').innerText = "₹" + pTot.toFixed(2);
            document.getElementById('d-sale').innerText = "₹" + sTot.toFixed(2);
            document.getElementById('d-payment').innerText = "₹" + payTot.toFixed(2);
            document.getElementById('d-receipt').innerText = "₹" + recTot.toFixed(2);

            let netProfit = sTot - pTot;
            document.getElementById('d-pl').innerText = "₹" + netProfit.toFixed(2);
            document.getElementById('d-pl').style.color = netProfit >= 0 ? "green" : "red";

            document.getElementById('plTotalSale').innerText = "₹" + sTot.toFixed(2);
            document.getElementById('plTotalPur').innerText = "₹" + pTot.toFixed(2);
            document.getElementById('plNetCalculated').innerText = "₹" + netProfit.toFixed(2);
        }

        // --- UTILITY: BACKUP IMPORT EXPORT SYSTEM ---
        function exportJSONData() {
            let dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(dataStore));
            let dlNode = document.createElement('a');
            dlNode.setAttribute("href", dataStr);
            dlNode.setAttribute("download", "KrishiVyapar_Database_Backup.json");
            dlNode.click();
        }
        function importJSONData(e) {
            let fReader = new FileReader();
            fReader.onload = function(evt) {
                try {
                    let parsed = JSON.parse(evt.target.result);
                    if(parsed.profile && parsed.kisan) {
                        dataStore = parsed; syncDB(); refreshAllData();
                        alert("डेटा सफलतापूर्वक रीस्टोर कर दिया गया है!");
                    }
                } catch(err) { alert("त्रुटि: बैकअप फ़ाइल सही नहीं है!"); }
            };
            fReader.readAsText(e.target.files[0]);
        }

        // --- UTILITY: HELPER TABLE SEARCH FILTER ---
        function filterTable(tId, val) {
            let trs = document.getElementById(tId).getElementsByTagName("tr");
            for(let i=1; i<trs.length; i++) {
                trs[i].style.display = trs[i].textContent.toLowerCase().includes(val.toLowerCase()) ? "" : "none";
            }
        }

        // --- UTILITY: AMOUNT IN WORDS ALGORITHM ---
        function convertNumberToWords(num) {
            let ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'];
            let tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'];
            num = Math.floor(num);
            if (num === 0) return 'Zero';
            function convert(n) {
                if (n < 20) return ones[n];
                if (n < 100) return tens[Math.floor(n / 10)] + (n % 10 !== 0 ? ' ' + ones[n % 10] : '');
                if (n < 1000) return ones[Math.floor(n / 100)] + ' Hundred' + (n % 100 !== 0 ? ' and ' + convert(n % 100) : '');
                if (n < 100000) return convert(Math.floor(n / 1000)) + ' Thousand' + (n % 1000 !== 0 ? ' ' + convert(n % 1000) : '');
                if (n < 10000000) return convert(Math.floor(n / 100000)) + ' Lakh' + (n % 100000 !== 0 ? ' ' + convert(n % 100000) : '');
                return '';
            }
            return convert(num);
        }
    </script>
</body>
</html>