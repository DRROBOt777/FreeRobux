# main.py
import sys
import os

# Current directory ကို path ထဲထည့်ပါ
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Rb.so ကို import လုပ်ပါ
import Rb

# Flask app object ကို ရယူပါ
app = Rb.app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
