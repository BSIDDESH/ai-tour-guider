# 🗺️ AI Tour Guider — Bengaluru Edition

> A Python CLI app that acts as your personal AI travel guide for **Bengaluru**, with 25+ handpicked places, smart recommendations, itinerary planning, hidden gems, and a wishlist system.

**Author:** B. Siddesh | [github.com/BSIDDESH](https://github.com/BSIDDESH)  
**Built for:** Google — The Big Code 2026

---

## 🚀 Features

- ✅ **25+ handpicked Bengaluru places** across 8 categories
- ✅ **AI Personalised Recommendations** — based on travel style & budget
- ✅ **Smart Day-wise Itinerary Planner** — themed days (Heritage, Food, Adventure etc.)
- ✅ **Hidden Gems** section — places most tourists completely miss
- ✅ **Filter by type** — Nature, Heritage, Food, Shopping, Spiritual, Entertainment
- ✅ **Budget Guide** — Backpacker / Mid-range / Luxury breakdowns
- ✅ **Wishlist** — save favourite places with JSON persistent storage
- ✅ City overview with local tips, transport guide, emergency numbers

---

## 🧠 How the AI Works

The recommendation engine scores each place based on:

| Input | Method |
|-------|--------|
| Travel preference (Nature/Heritage/Food etc.) | Tag-based matching |
| Daily budget | Budget category mapping |
| Number of days | Smart itinerary slot allocation |

Places are ranked by **tag match score + rating** to give personalised suggestions.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Core language |
| JSON module | Wishlist persistent storage |
| OS / Datetime | Terminal + timestamps |

**No pip install needed — runs on pure Python 3!**

---

## ▶️ How to Run

```bash
git clone https://github.com/BSIDDESH/ai-tour-guider.git
cd ai-tour-guider
python main.py
```

---

## 🏙️ Places Covered

| Category | Count | Examples |
|----------|-------|---------|
| Nature | 4 | Lalbagh, Cubbon Park, Sankey Tank |
| Heritage | 4 | Bangalore Palace, Tipu Sultan's Palace |
| Spiritual | 2 | ISKCON Temple, Bull Temple |
| Food | 4 | VV Puram Food Street, MTR, Vidyarthi Bhavan |
| Shopping | 3 | Commercial Street, UB City, Chickpete |
| Entertainment | 3 | Wonderla, Indiranagar, Science Museum |
| Day Trips | 3 | Nandi Hills, Savandurga, Mysuru |
| Cultural | 2 | Janapada Loka, Bannerghatta |

---

## 📂 Project Structure

```
ai-tour-guider/
├── main.py          # Full application + Bengaluru data
├── wishlist.json    # Auto-generated wishlist
└── README.md
```

---

## 🎯 What I Learned

- Nested data modelling with Python dictionaries
- Tag-based AI recommendation system
- JSON file handling for persistent storage
- CLI UI design with ANSI colour codes
- Modular Python project structure

---

⭐ Star this repo if you found it useful!
