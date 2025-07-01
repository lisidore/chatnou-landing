import requests
import re

# Step 1 — get the current ngrok URL from local API
response = requests.get("http://127.0.0.1:4040/api/tunnels")
data = response.json()
public_url = data["tunnels"][0]["public_url"]
print(f"🌐 Current ngrok URL: {public_url}")

# ---------------------------
# Update index.html
# ---------------------------
with open("index.html", "r") as f:
    index_html = f.read()

pattern_index = r'href="http[s]?://[^/]+(/select_user\.html)"'
new_index_html = re.sub(
    pattern_index,
    f'href="{public_url}\\1"',
    index_html
)

with open("index.html", "w") as f:
    f.write(new_index_html)

print("✅ index.html updated with new ngrok URL (keeping /select_user.html)")

# ---------------------------
# Update select_user.html
# ---------------------------
with open("select_user.html", "r") as f:
    select_html = f.read()

pattern_select = r'window\.location\.href=\'http[s]?://[^/]+(/upload_[a-z]+)\''
new_select_html = re.sub(
    pattern_select,
    f"window.location.href='{public_url}\\1'",
    select_html
)

with open("select_user.html", "w") as f:
    f.write(new_select_html)

print("✅ select_user.html updated with new ngrok URL (keeping /upload_xxx)")
