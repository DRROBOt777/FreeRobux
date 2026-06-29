import os
import sys
from cryptography.fernet import Fernet

# Render ရဲ့ Environment ကနေ လျှို့ဝှက်သော့ကို လှမ်းယူခြင်း
SECRET_KEY = os.environ.get("MY_SECRET_KEY")

if not SECRET_KEY:
    print("[-] Error: MY_SECRET_KEY ရှာမတွေ့ပါ။ Render Settings မှာ ထည့်ပေးပါ။")
    sys.exit(1)

try:
    # ၁။ ကုဒ်ဝှက်ထားတဲ့ rb_enc.py ဖိုင်ကို ဖတ်ခြင်း
    with open("rb_enc.py", "rb") as f:
        encrypted_data = f.read()

    # ၂။ သော့ချက်နဲ့ ကုဒ်ပြန်ဖြည်ခြင်း
    fernet = Fernet(SECRET_KEY.encode())
    decrypted_data = fernet.decrypt(encrypted_data)

    # ၃။ ဖြည်လို့ရလာတဲ့ ကုဒ်တွေကို မန်မိုရီထဲမှာတင် တိုက်ရိုက် Run ခြင်း (ဖိုင်အဖြစ် မသိမ်းပါ)
    compiled_code = compile(decrypted_data, "rb", "exec")
    rb_module = {}
    exec(compiled_code, rb_module)

    # Flask app object ကို ဆွဲထုတ်ခြင်း
    app = rb_module.get("app")
    print("[+] rb_enc.py decrypted and loaded successfully in memory!")

except Exception as e:
    print(f"[-] Failed to decrypt or run the code: {e}")
    sys.exit(1)

if __name__ == "__main__":
    if app:
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
