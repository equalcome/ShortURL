# 🔗 Django 短網址服務（支援 Google / Facebook 登入）

這是一個使用 **Django + django-allauth** 開發的完整短網址系統，
支援 **Google / Facebook 登入**、短網址建立、點擊紀錄與 IP 追蹤，
並已部署於 **Render 雲端平台**。

---

## 🚀 專案特色

✅ 使用 Google / Facebook OAuth 登入  
✅ 登入後可建立自訂短網址  
✅ 點擊次數與來源 IP 自動記錄  
✅ 使用者可瀏覽自己建立的短網址清單  
✅ 部署於 Render（搭配 PostgreSQL 資料庫）  
✅ 採用 `.env` 管理敏感設定，支援雲端環境變數

---

## 🏗️ 技術架構

| 類別   | 使用技術                       |
| ------ | ------------------------------ |
| 後端   | Django 5 + django-allauth      |
| 資料庫 | PostgreSQL (Render 雲端)       |
| 驗證   | Google / Facebook OAuth 2.0    |
| 前端   | Django Template (HTML + CSS)   |
| 部署   | Render + Gunicorn + Whitenoise |

---

## ⚙️ 本地開發安裝步驟

### 1️⃣ 下載專案

```bash
git clone https://github.com/<你的帳號>/<你的repo名稱>.git
cd <你的repo名稱>
```

### 2️⃣ 建立虛擬環境

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# 或
source venv/bin/activate # macOS / Linux
```

### 3️⃣ 安裝依賴套件

```bash
pip install -r requirements.txt
```

### 4️⃣ 建立 `.env` 檔案

在專案根目錄建立 `.env` 並填入：

```
SECRET_KEY=dev-secret
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
GOOGLE_CLIENT_ID=<你的 Google Client ID>
GOOGLE_CLIENT_SECRET=<你的 Google Secret>
FB_APP_ID=<你的 Facebook App ID>
FB_APP_SECRET=<你的 Facebook Secret>
```

### 5️⃣ 建立資料表

```bash
python manage.py migrate
```

### 6️⃣ 啟動伺服器

```bash
python manage.py runserver
```

打開瀏覽器進入：  
👉 http://127.0.0.1:8000/

---

## 🌍 Render 雲端部署

### 🏗️ Build Command

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

### 🚀 Start Command

```bash
gunicorn config.wsgi
```

### 🔐 Environment Variables（環境變數）

| 變數名稱             | 範例值                          | 說明              |
| -------------------- | ------------------------------- | ----------------- |
| SECRET_KEY           | 隨機長字串                      | Django 安全金鑰   |
| DEBUG                | False                           | 關閉除錯模式      |
| ALLOWED_HOSTS        | <你的 Render 網域>.onrender.com | Render 網域       |
| DATABASE_URL         | （Render 產生的 Postgres URL）  | 資料庫連線        |
| GOOGLE_CLIENT_ID     | 你的 Google ID                  | OAuth 登入使用    |
| GOOGLE_CLIENT_SECRET | 你的 Google Secret              | OAuth 登入使用    |
| FB_APP_ID            | （可選）                        | Facebook 登入使用 |
| FB_APP_SECRET        | （可選）                        | Facebook 登入使用 |

---

## 🧪 使用流程

1️⃣ 使用者進入首頁 → 點擊「使用 Google 登入」  
2️⃣ 登入後可貼上原始網址產生短碼  
3️⃣ 系統會生成短網址（例如 `/abc123/`）  
4️⃣ 使用者點擊該短網址 → 自動導向原始網址  
5️⃣ 系統同時記錄該次點擊的時間與 IP 位址
