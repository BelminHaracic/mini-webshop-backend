
# 🛒 Mini Webshop Backend API

Ovo je REST API za Mini Webshop aplikaciju. Omogućava upravljanje proizvodima, narudžbama i korisnicima. Backend je razvijen pomoću **Python FastAPI** i hostovan na **Railway platformi**.

---

## 🚀 Kako pokrenuti API lokalno

1. Kloniraj repozitorij:
   ```bash
   git clone https://github.com/BelminHaracic/mini-webshop-backend.git
   cd mini-webshop-backend
````

2. Kreiraj virtualno okruženje i aktiviraj ga:

   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   # ili
   source venv/bin/activate   # Linux/macOS
   ```

3. Instaliraj zavisnosti:

   ```bash
   pip install -r requirements.txt
   ```

4. Pokreni aplikaciju:

   ```bash
   uvicorn main:app --reload
   ```

---

## 🔗 Live API URL i dokumentacija

* **API URL:** [https://mini-webshop-backend-production.up.railway.app](https://mini-webshop-backend-production.up.railway.app)

---

## 🧪 API Endpointi

| Endpoint                   | Metoda | Opis                      |
| -------------------------- | ------ | ------------------------- |
| `/products`                | GET    | Dohvati sve proizvode     |
| `/products`                | POST   | Dodaj novi proizvod       |
| `/products/{id}`           | PUT    | Uredi proizvod            |
| `/products/{id}`           | DELETE | Obriši proizvod           |
| `/orders`                  | GET    | Dohvati sve narudžbe      |
| `/orders`                  | POST   | Kreiraj novu narudžbu     |
| `/orders/{id}`             | PUT    | Promijeni status narudžbe |
| `/auth/login` (opcionalno) | POST   | Prijava korisnika/admina  |

---

## 👤 Vrste korisnika

* **Admin**

  * Dodavanje, uređivanje i brisanje proizvoda
  * Pregled i upravljanje narudžbama

* **Gost (User)**

  * Pregled proizvoda
  * Kreiranje narudžbi

---

## 🔐 Admin kredencijali za pristup

* Username: `admin`
* Password: `admin123`

---

## 📁 Struktura projekta

```
mini-webshop-backend/
├── app/
│   ├── main.py          # Glavni fajl aplikacije
│   ├── models.py        # Definicija modela baze podataka
│   ├── routes/          # Definicija API ruta
│   └── database.py      # Povezivanje sa bazom podataka
├── requirements.txt     # Lista Python zavisnosti
└── README.md            # Ovaj fajl
```

---

## 🛠️ Tehnologije korištene

* Python 3.x
* FastAPI
* SQLite (ili druga baza)
* Uvicorn
* CORS Middleware
* Railway platforma za hosting

---

## 📎 Korisni linkovi

* Frontend web shop: [https://mini-webshop.web.app](https://mini-webshop.web.app)
* API na Railway-u: [https://mini-webshop-backend-production.up.railway.app](https://mini-webshop-backend-production.up.railway.app)

---

## 📄 Licenca

MIT © 2025 [Belmin Haračić](https://github.com/BelminHaracic)

```

Ako ti treba pomoć oko bilo čega drugog, samo reci!
```
