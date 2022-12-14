mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\


    [theme]
    primaryColor = "#d33682"
    backgroundColor = "red"
    secondaryBackgroundColor = "#586e75"
    textColor = "#fafafa"
    font = "sans serif"

" > ~/.streamlit/config.toml
