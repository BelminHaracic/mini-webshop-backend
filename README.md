Naravno! Evo kompletnog `README.md` fajla za tvoj **backend API** – spremno za **copy-paste**:

---

````markdown
# 🛒 Mini Webshop API

Ovo je REST API za Mini Webshop aplikaciju. Omogućava upravljanje proizvodima, narudžbama i korisnicima. Backend je razvijen pomoću **Python FastAPI** i povezan sa frontend aplikacijom hostovanom na Firebaseu.

---

## 🚀 Kako pokrenuti API lokalno

1. **Kloniraj repozitorij:**
   ```bash
   git clone https://github.com/BelminHaracic/mini-webshop-backend.git
   cd mini-webshop-backend
````

2. **Kreiraj virtualno okruženje:**

   ```bash
   python -m venv venv
   venv\Scripts\activate      # na Windows
   # ili
   source venv/bin/activate   # na Linux/macOS
   ```

3. **Instaliraj zavisnosti:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Pokreni aplikaciju:**

   ```bash
   uvicorn main:app --reload
   ```

---

## 🔗 API dokumentacija

Možeš testirati API putem **Postmana** ili pregledati automatski generisanu dokumentaciju:

* 📘 Swagger UI: [`http://localhost:5000/docs`](http://localhost:5000/docs)
* 🔬 Redoc: [`http://localhost:5000/redoc`](http://localhost:5000/redoc)

---

## 🧪 API funkcionalnosti

| Endpoint                     | Metoda | Opis                      |
| ---------------------------- | ------ | ------------------------- |
| `/products`                  | GET    | Dohvati sve proizvode     |
| `/products`                  | POST   | Dodaj novi proizvod       |
| `/products/{id}`             | PUT    | Uredi proizvod            |
| `/products/{id}`             | DELETE | Obriši proizvod           |
| `/orders`                    | GET    | Pregled narudžbi          |
| `/orders`                    | POST   | Kreiraj narudžbu          |
| `/orders/{id}`               | PUT    | Promijeni status narudžbe |
| `/auth/login` *(opcionalno)* | POST   | Login korisnika/admina    |

---

## 👤 Vrste korisnika

* 👨‍💼 **Admin**

  * Može dodavati, uređivati i brisati proizvode
  * Ima uvid u sve narudžbe i može mijenjati njihov status

* 🛍️ **Korisnik (Guest)**

  * Može pregledavati proizvode i praviti narudžbe

---

## 🔐 Admin pristup

Koristi sljedeće kredencijale za testiranje putem Postmana:

* **Username:** `admin`
* **Password:** `admin123`

---

## 🌐 Deployment

API se može deployati na:

* 🐍 **Render**, **Railway**, **PythonAnywhere**
* Ili lokalno putem `ngrok` ako se želi testirati s frontendom

---

## 📁 Struktura projekta

```
mini-webshop-backend/
├── app/                # API moduli i rute
│   ├── main.py         # Glavna aplikacija
│   ├── models.py       # Modeli baze podataka
│   ├── routes/         # Endpoint rute
│   └── database.py     # Konekcija s bazom
├── requirements.txt    # Zavistnosti
└── README.md           # Ovaj dokument
```

---

## 📎 Linkovi

* 🔗 Frontend aplikacija: [Webshop na Firebase](https://<TVOJ-LINK>.web.app)
* 🔗 API na Postman: [Postman kolekcija](https://www.postman.com/...)

---

## 🛠️ Tehnologije

* Python 3.x
* FastAPI
* SQLite (ili druga baza)
* Uvicorn
* CORS, Axios

---

## 📄 Licenca

MIT © 2025 [Belmin Haračić](https://github.com/BelminHaracic)

```

---

Ako koristiš **Flask** umjesto FastAPI, mogu ti odmah prilagoditi i Flask verziju. Samo reci.
```
