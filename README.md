
# ⚙️ Mini Webshop – Backend

Ovo je backend API za **Mini Webshop** aplikaciju, razvijen korištenjem FastAPI frameworka. Backend omogućava upravljanje proizvodima, narudžbama i korisnicima, te komunikaciju sa frontend aplikacijom.

---

## 🚀 Pokretanje aplikacije lokalno

Prati ove korake da pokreneš backend lokalno:

```bash
# 1. Idi u direktorij backend
cd mini-webshop-backend

# 2. Kreiraj virtualno okruženje i aktiviraj ga
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# 3. Instaliraj potrebne pakete
pip install -r requirements.txt

# 4. Pokreni FastAPI server
uvicorn main:app --reload
````

Backend će biti dostupan na `http://localhost:5000`.

---

## 🌐 Deploy verzija (Railway)

Backend API je deployan na Railway i dostupan je na sljedećem URL-u:

🔗 [https://mini-webshop-backend-production.up.railway.app](https://mini-webshop-backend-production.up.railway.app)

---

## ⚙️ Funkcionalnosti

API pruža sljedeće funkcionalnosti:

* 📦 **Upravljanje proizvodima** – CRUD operacije (kreiranje, čitanje, ažuriranje, brisanje)
* 🛒 **Upravljanje narudžbama** – kreiranje, pregled i ažuriranje statusa narudžbi
* 🔐 **Autentikacija admin korisnika** – provjera pristupa admin funkcijama
* 🧩 **Validacija podataka i greške** – odgovarajuće poruke i statusi API poziva

---

## 🔗 API Endpointi

### Proizvodi (`/products`)

* `GET /products` – Dohvati listu proizvoda
* `GET /products/{id}` – Dohvati detalje proizvoda
* `POST /products` – Kreiraj novi proizvod (admin)
* `PUT /products/{id}` – Ažuriraj proizvod (admin)
* `DELETE /products/{id}` – Obriši proizvod (admin)

### Narudžbe (`/orders`)

* `GET /orders` – Dohvati listu narudžbi (admin)
* `GET /orders/{id}` – Dohvati detalje narudžbe (admin)
* `POST /orders` – Kreiraj novu narudžbu
* `PUT /orders/{id}` – Ažuriraj status narudžbe (admin)

---

## 👤 Admin kredencijali (primjer)

| Korisničko ime | Lozinka  |
| -------------- | -------- |
| admin          | admin123 |

---

## 📁 Povezani repozitoriji

📁 **Backend source code:**
🔗 [https://github.com/BelminHaracic/mini-webshop-backend](https://github.com/BelminHaracic/mini-webshop-backend)

📁 **Frontend source code:**
🔗 [https://github.com/BelminHaracic/mini-webshop-frontend](https://github.com/BelminHaracic/mini-webshop-frontend)

---

## 🧪 Testiranje API-ja

API se može testirati putem alata kao što su [Postman](https://www.postman.com/) ili [Insomnia](https://insomnia.rest/).

**Base URL:**
`https://mini-webshop-backend-production.up.railway.app` (produkcija)
ili
`http://localhost:5000` (lokalno)

---

## 📝 Napomene

* Backend je razvijen u FastAPI frameworku s automatski generisanom Swagger dokumentacijom na `/docs`.
* Deployment je urađen na Railway platformu.
* Baza podataka može biti lokalna SQLite ili produkcijski DB povezan s Railway.

---

✅ Za pokretanje kompletne aplikacije, ne zaboravi pokrenuti i frontend!

---

Hvala na korištenju Mini Webshop backenda! 🚀

```

Sad je sve u istom formatu kao tvoj frontend README, uredno, pregledno i spremno za copy-paste direktno u `README.md` backend repozitorija.  
Javi ako trebaš još nešto!
```
