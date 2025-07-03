import requests
import re

# get current ngrok public URL
response = requests.get("http://127.0.0.1:4040/api/tunnels")
data = response.json()
public_url = data["tunnels"][0]["public_url"]
print(f"🌐 Current ngrok URL: {public_url}")

# use the public_url as-is
multiuser_url = public_url

# update select_user.html
with open("select_user.html", "r") as f:
    select_html = f.read()

pattern_select = r"window\.location\.href='http[s]?://[^/]+(/upload_[a-z]+)'"
new_select_html = re.sub(
    pattern_select,
    f"window.location.href='{multiuser_url}\\1'",
    select_html
)

with open("select_user.html", "w") as f:
    f.write(new_select_html)

print("✅ select_user.html updated with new ngrok URL (keeping /upload_xxx')")
