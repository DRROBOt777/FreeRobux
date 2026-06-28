import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import Rb
    print("[+] Rb.so loaded successfully")
except ImportError as e:
    print(f"[-] Failed to load Rb.so: {e}")
    sys.exit(1)

# Flask app object ကို ရယူပါ
if hasattr(Rb, 'app'):
    app = Rb.app
    print("[+] Flask app object found")
else:
    print("[-] No 'app' object found in Rb.so")
    sys.exit(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
