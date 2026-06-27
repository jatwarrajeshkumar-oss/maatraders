import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows your HTML page to talk to this backend

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br"
}

@app.route('/api/option-chain', methods=['GET'])
def get_option_chain():
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    
    session = requests.Session()
    # Hit home page first to get cookies
    session.get("https://www.nseindia.com", headers=headers)
    
    try:
        response = session.get(url, headers=headers)
        data = response.json()
        
        records = data['records']
        expiry_dates = records['expiryDates']
        current_expiry = expiry_dates[0] # Get the nearest expiry
        
        # Filter data for current expiry
        filtered_data = [x for x in records['data'] if x['expiryDate'] == current_expiry]
        underlying_value = records['underlyingValue']
        
        # Calculate Total OI for PCR
        total_ce_oi = sum(x['CE']['openInterest'] for x in filtered_data if 'CE' in x)
        total_pe_oi = sum(x['PE']['openInterest'] for x in filtered_data if 'PE' in x)
        pcr = round(total_pe_oi / total_ce_oi, 2) if total_ce_oi > 0 else 0
        
        return jsonify({
            "underlyingValue": underlying_value,
            "expiryDate": current_expiry,
            "pcr": pcr,
            "data": filtered_data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)