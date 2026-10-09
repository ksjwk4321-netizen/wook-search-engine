
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Wook 검색엔진")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Wook 검색엔진</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 80px 20px;
                background: #f5f7fb;
            }
            h1 {
                font-size: 48px;
                color: #4285f4;
            }
            input {
                width: 70%;
                max-width: 450px;
                padding: 14px;
                border: 1px solid #ddd;
                border-radius: 25px;
                font-size: 16px;
            }
            button {
                padding: 14px 22px;
                border: none;
                border-radius: 25px;
                background: #4285f4;
                color: white;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Wook</h1>
        <p>무엇이든 검색해 보세요.</p>
        <form action="https://www.google.com/search" method="get">
            <input type="text" name="q" placeholder="검색어를 입력하세요">
            <button type="submit">검색</button>
        </form>
    </body>
    </html>
    """


@app.get("/health")
def health():
    return {"status": "ok", "service": "Wook"}
