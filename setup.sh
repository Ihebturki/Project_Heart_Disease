mkdir -p ~/.streamlit/

echo "[theme]
primaryColor='#2214c7'
backgroundColor='#ffffff'
secondaryBackgroundColor='#e8eef9'
textColor='#000000'
font='sans serif'
[general]
email = \"ihebturki77.com\"
[server]
headless = true
enableCORS=false
port = $PORT


" > ~/.streamlit/config.toml
