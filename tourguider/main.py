"""
╔══════════════════════════════════════════════════════╗
║   AI TOUR GUIDER — BENGALURU                         ║
║   Author : B. Siddesh | github.com/BSIDDESH          ║
║   Branch : B.E. AI & ML — East West Institute        ║
║   Built  : March 2026 | The Big Code 2026 Prep       ║
╚══════════════════════════════════════════════════════╝

Features:
  - 25+ handpicked Bengaluru places
  - AI personalised recommendations
  - Smart day-wise itinerary generator
  - Budget calculator
  - Wishlist with JSON storage
  - Nearby food suggestions for every area
  - Hidden gems section
"""

import os
import json
from datetime import datetime

# ── Colours ────────────────────────────────────────────────────────────────
BLUE   = "\033[94m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RED    = "\033[91m"
MAGENTA= "\033[95m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"

WISHLIST_FILE = "wishlist.json"

# ══════════════════════════════════════════════════════════════════════════
#  BENGALURU DATA
# ══════════════════════════════════════════════════════════════════════════
BENGALURU = {
    "name"      : "Bengaluru",
    "nickname"  : "Silicon Valley of India",
    "founded"   : "1537 (by Kempe Gowda I)",
    "population": "~13 million",
    "best_time" : "October to February (pleasant 15–28°C)",
    "avoid"     : "March–May (hot) and June–September (heavy rain)",
    "language"  : "Kannada (English & Hindi widely spoken)",
    "famous_for": "IT Industry, Gardens, Craft Beer, Dosas, Pleasant Weather",
    "fun_fact"  : "Bengaluru has more flyovers than any other Indian city!",

    "areas": {
        "Central": ["MG Road", "Brigade Road", "Cubbon Park", "Vidhana Soudha"],
        "North"  : ["Hebbal", "Yelahanka", "ISKCON Temple"],
        "South"  : ["Jayanagar", "JP Nagar", "Banashankari"],
        "East"   : ["Whitefield", "Indiranagar", "Koramangala"],
        "West"   : ["Rajajinagar", "Malleswaram", "Yeshwantpur"],
    },

    "places": [
        # ── NATURE & PARKS ──────────────────────────────────────────────
        {
            "id"      : 1,
            "name"    : "Lalbagh Botanical Garden",
            "area"    : "South Bengaluru",
            "type"    : "Nature",
            "rating"  : 4.7,
            "timings" : "6:00 AM – 7:00 PM",
            "entry"   : "Rs. 20 (Adults) | Free before 8 AM",
            "duration": "2–3 hours",
            "best_for": ["Nature lovers", "Photography", "Morning walk", "Families"],
            "tip"     : "Visit in January for the famous Republic Day Flower Show. The 200-year-old glass house is stunning!",
            "food_nearby": ["Mavalli Tiffin Room (MTR)", "Brahmin's Coffee Bar"],
            "hidden_gem" : False,
            "tags"    : ["nature", "peaceful", "photography", "history", "morning"],
        },
        {
            "id"      : 2,
            "name"    : "Cubbon Park",
            "area"    : "Central Bengaluru",
            "type"    : "Nature",
            "rating"  : 4.6,
            "timings" : "6:00 AM – 6:00 PM",
            "entry"   : "Free",
            "duration": "1–2 hours",
            "best_for": ["Jogging", "Cycling", "Picnic", "Couples"],
            "tip"     : "Rent a bicycle inside the park for just Rs. 30/hour. Avoid Sunday afternoons — very crowded.",
            "food_nearby": ["The Only Place", "Koshy's Restaurant"],
            "hidden_gem" : False,
            "tags"    : ["nature", "free", "jogging", "cycling", "morning"],
        },
        {
            "id"      : 3,
            "name"    : "Sankey Tank",
            "area"    : "Sadashivanagar",
            "type"    : "Nature",
            "rating"  : 4.4,
            "timings" : "6:00 AM – 8:00 PM",
            "entry"   : "Free",
            "duration": "1 hour",
            "best_for": ["Sunset views", "Evening walks", "Bird watching"],
            "tip"     : "Best place in Bengaluru for sunset! Bring snacks and enjoy the view from the bund.",
            "food_nearby": ["Sankey Tank snack stalls", "Hotel Pai Vista nearby"],
            "hidden_gem" : True,
            "tags"    : ["nature", "free", "sunset", "peaceful", "evening"],
        },
        {
            "id"      : 4,
            "name"    : "Ulsoor Lake",
            "area"    : "Central Bengaluru",
            "type"    : "Nature",
            "rating"  : 4.2,
            "timings" : "6:00 AM – 8:00 PM",
            "entry"   : "Free (Boating: Rs. 100)",
            "duration": "1–2 hours",
            "best_for": ["Boating", "Morning walk", "Photography"],
            "tip"     : "Try boating on weekday mornings. The lake is home to many migratory birds in winter.",
            "food_nearby": ["Shivaji Nagar restaurants", "Empire Restaurant"],
            "hidden_gem" : False,
            "tags"    : ["nature", "boating", "morning", "photography"],
        },

        # ── HERITAGE & HISTORY ──────────────────────────────────────────
        {
            "id"      : 5,
            "name"    : "Bangalore Palace",
            "area"    : "Vasanthnagar",
            "type"    : "Heritage",
            "rating"  : 4.4,
            "timings" : "10:00 AM – 5:30 PM",
            "entry"   : "Rs. 230 (Indians) | Camera: Rs. 685",
            "duration": "1.5–2 hours",
            "best_for": ["History buffs", "Architecture", "Photography"],
            "tip"     : "Tudor-style architecture inspired by England's Windsor Castle. Audio guide available. Don't miss the royal artifacts inside.",
            "food_nearby": ["UB City restaurants", "Karavalli Restaurant"],
            "hidden_gem" : False,
            "tags"    : ["heritage", "history", "architecture", "photography"],
        },
        {
            "id"      : 6,
            "name"    : "Tipu Sultan's Summer Palace",
            "area"    : "Old Bengaluru",
            "type"    : "Heritage",
            "rating"  : 4.2,
            "timings" : "8:00 AM – 5:30 PM",
            "entry"   : "Rs. 15 (Indians)",
            "duration": "1 hour",
            "best_for": ["History", "Architecture"],
            "tip"     : "Beautiful teak wood palace built in 1791. Very underrated — almost no tourists on weekdays!",
            "food_nearby": ["VV Puram Food Street (just 1 km away!)"],
            "hidden_gem" : True,
            "tags"    : ["heritage", "history", "architecture", "budget"],
        },
        {
            "id"      : 7,
            "name"    : "Vidhana Soudha",
            "area"    : "Central Bengaluru",
            "type"    : "Heritage",
            "rating"  : 4.5,
            "timings" : "Exterior — anytime",
            "entry"   : "Free (exterior viewing)",
            "duration": "30 minutes",
            "best_for": ["Photography", "Architecture"],
            "tip"     : "Visit at night when it is beautifully illuminated. Best photos from Cubbon Park side.",
            "food_nearby": ["Koshy's Bar and Restaurant"],
            "hidden_gem" : False,
            "tags"    : ["heritage", "architecture", "photography", "free", "night"],
        },
        {
            "id"      : 8,
            "name"    : "Bengaluru Fort",
            "area"    : "Krishnarajendra Market",
            "type"    : "Heritage",
            "rating"  : 4.0,
            "timings" : "8:00 AM – 5:30 PM",
            "entry"   : "Rs. 5",
            "duration": "45 minutes",
            "best_for": ["History", "Budget travel"],
            "tip"     : "One of the cheapest monuments in India at just Rs. 5! Built by Kempe Gowda in 1537.",
            "food_nearby": ["KR Market street food"],
            "hidden_gem" : True,
            "tags"    : ["heritage", "history", "budget", "hidden gem"],
        },

        # ── SPIRITUAL ───────────────────────────────────────────────────
        {
            "id"      : 9,
            "name"    : "ISKCON Temple",
            "area"    : "Rajajinagar",
            "type"    : "Spiritual",
            "rating"  : 4.8,
            "timings" : "7:15 AM – 1:00 PM | 4:15 PM – 8:30 PM",
            "entry"   : "Free",
            "duration": "1.5–2 hours",
            "best_for": ["Spiritual seekers", "Architecture", "Peaceful retreat"],
            "tip"     : "Attend the evening aarti at 6:30 PM — absolutely mesmerizing. The golden architecture is stunning at night.",
            "food_nearby": ["ISKCON prasadam (temple food — must try!)", "Rajajinagar restaurants"],
            "hidden_gem" : False,
            "tags"    : ["spiritual", "peaceful", "architecture", "free", "evening"],
        },
        {
            "id"      : 10,
            "name"    : "Dodda Ganesha Temple (Bull Temple)",
            "area"    : "Basavanagudi",
            "type"    : "Spiritual",
            "rating"  : 4.5,
            "timings" : "6:00 AM – 12:00 PM | 5:00 PM – 9:00 PM",
            "entry"   : "Free",
            "duration": "45 minutes",
            "best_for": ["Spiritual seekers", "Local culture"],
            "tip"     : "Home to the famous Nandi Bull monolith — over 4.5 metres tall! Basavanagudi is the oldest neighbourhood in Bengaluru.",
            "food_nearby": ["Vidyarthi Bhavan (legendary masala dosa nearby!)"],
            "hidden_gem" : False,
            "tags"    : ["spiritual", "culture", "free", "history"],
        },

        # ── FOOD ────────────────────────────────────────────────────────
        {
            "id"      : 11,
            "name"    : "VV Puram Food Street",
            "area"    : "Basavanagudi",
            "type"    : "Food",
            "rating"  : 4.6,
            "timings" : "5:00 PM – 11:00 PM",
            "entry"   : "Free",
            "duration": "1–2 hours",
            "best_for": ["Foodies", "Budget travel", "Local experience"],
            "tip"     : "The BEST street food in Bengaluru. Must try: Masala Puri, Dahi Puri, Gobi Manchurian, Momos and fresh fruit juices.",
            "food_nearby": ["Everything here IS food!"],
            "hidden_gem" : False,
            "tags"    : ["food", "street food", "budget", "evening", "must visit"],
        },
        {
            "id"      : 12,
            "name"    : "Mavalli Tiffin Room (MTR)",
            "area"    : "Lalbagh Road",
            "type"    : "Food",
            "rating"  : 4.7,
            "timings" : "6:30 AM – 11:00 AM | 12:30 PM – 9:00 PM",
            "entry"   : "Menu-based",
            "duration": "1 hour",
            "best_for": ["Authentic South Indian breakfast"],
            "tip"     : "100+ year old institution! Rava Idli was INVENTED here. Reach by 7 AM or expect a 30-min queue. Worth every minute.",
            "food_nearby": ["Lalbagh Botanical Garden (just 5 min walk)"],
            "hidden_gem" : False,
            "tags"    : ["food", "traditional", "breakfast", "must visit"],
        },
        {
            "id"      : 13,
            "name"    : "Vidyarthi Bhavan",
            "area"    : "Gandhi Bazaar, Basavanagudi",
            "type"    : "Food",
            "rating"  : 4.6,
            "timings" : "6:30 AM – 11:30 AM | 2:00 PM – 8:00 PM (Closed Mon)",
            "entry"   : "Menu-based",
            "duration": "45 minutes",
            "best_for": ["Masala Dosa lovers", "Authentic breakfast"],
            "tip"     : "Their crispy ghee masala dosa is legendary — people drive from across the city for it. Cash only!",
            "food_nearby": ["Gandhi Bazaar market", "Bull Temple"],
            "hidden_gem" : False,
            "tags"    : ["food", "traditional", "breakfast", "must visit"],
        },
        {
            "id"      : 14,
            "name"    : "Church Street Social",
            "area"    : "Church Street",
            "type"    : "Food",
            "rating"  : 4.4,
            "timings" : "12:00 PM – 1:00 AM",
            "entry"   : "Menu-based",
            "duration": "2 hours",
            "best_for": ["Young crowd", "Craft beer", "Fusion food"],
            "tip"     : "Iconic café-bar on the coolest street in Bengaluru. Try the pork bao buns and house-made cocktails.",
            "food_nearby": ["Entire Church Street has great cafes!"],
            "hidden_gem" : False,
            "tags"    : ["food", "nightlife", "modern", "youth"],
        },

        # ── SHOPPING ────────────────────────────────────────────────────
        {
            "id"      : 15,
            "name"    : "Commercial Street",
            "area"    : "Shivajinagar",
            "type"    : "Shopping",
            "rating"  : 4.5,
            "timings" : "10:00 AM – 9:30 PM",
            "entry"   : "Free",
            "duration": "2–3 hours",
            "best_for": ["Budget shopping", "Clothes", "Accessories", "Fabrics"],
            "tip"     : "Bargain hard — start at 50% of the quoted price. Parking is a nightmare; take Metro to Trinity station.",
            "food_nearby": ["Nagarjuna restaurant", "Street chaat stalls"],
            "hidden_gem" : False,
            "tags"    : ["shopping", "budget", "clothes", "bargain"],
        },
        {
            "id"      : 16,
            "name"    : "UB City Mall",
            "area"    : "Vittal Mallya Road",
            "type"    : "Shopping",
            "rating"  : 4.5,
            "timings" : "11:00 AM – 10:00 PM",
            "entry"   : "Free",
            "duration": "2–3 hours",
            "best_for": ["Luxury brands", "Fine dining", "Premium experience"],
            "tip"     : "Bengaluru's most premium mall. Visit the outdoor Eat Street terrace for sunset dining with city views.",
            "food_nearby": ["Restaurants inside UB City — Fatty Bao, The Black Pearl"],
            "hidden_gem" : False,
            "tags"    : ["shopping", "luxury", "food", "evening"],
        },
        {
            "id"      : 17,
            "name"    : "Chickpete Market",
            "area"    : "Old Bengaluru",
            "type"    : "Shopping",
            "rating"  : 4.3,
            "timings" : "9:00 AM – 8:00 PM",
            "entry"   : "Free",
            "duration": "1.5 hours",
            "best_for": ["Silk sarees", "Traditional jewellery", "Wholesale shopping"],
            "tip"     : "Best place for traditional Mysore silk sarees. Much cheaper than mall prices. Wholesale available too.",
            "food_nearby": ["KR Market street food", "Veena Stores filter coffee"],
            "hidden_gem" : True,
            "tags"    : ["shopping", "traditional", "budget", "silk"],
        },

        # ── ENTERTAINMENT & MODERN ───────────────────────────────────────
        {
            "id"      : 18,
            "name"    : "Wonderla Amusement Park",
            "area"    : "Mysore Road",
            "type"    : "Entertainment",
            "rating"  : 4.5,
            "timings" : "11:00 AM – 6:00 PM (Weekdays) | 10:30 AM – 7:00 PM (Weekends)",
            "entry"   : "Rs. 849 (Adults)",
            "duration": "Full day",
            "best_for": ["Families", "Friends outing", "Thrill seekers"],
            "tip"     : "Book tickets online to save Rs. 150. Visit on weekdays to avoid 2-hour ride queues. Bring a change of clothes for water rides!",
            "food_nearby": ["Food stalls inside Wonderla"],
            "hidden_gem" : False,
            "tags"    : ["entertainment", "thrill", "family", "friends"],
        },
        {
            "id"      : 19,
            "name"    : "Visvesvaraya Industrial & Technological Museum",
            "area"    : "Kasturba Road",
            "type"    : "Entertainment",
            "rating"  : 4.3,
            "timings" : "10:00 AM – 6:00 PM (Closed Mondays)",
            "entry"   : "Rs. 60 (Adults)",
            "duration": "2–3 hours",
            "best_for": ["Students", "Science enthusiasts", "Families"],
            "tip"     : "Great for engineering and science students! Interactive exhibits on space, robotics and engines. Very underrated.",
            "food_nearby": ["Koshy's nearby", "Cubbon Park snack vendors"],
            "hidden_gem" : True,
            "tags"    : ["education", "science", "students", "budget"],
        },
        {
            "id"      : 20,
            "name"    : "Indiranagar 100 Feet Road",
            "area"    : "Indiranagar",
            "type"    : "Entertainment",
            "rating"  : 4.4,
            "timings" : "12:00 PM – 2:00 AM",
            "entry"   : "Free",
            "duration": "Evening",
            "best_for": ["Nightlife", "Craft beer", "Pub hopping", "Food crawl"],
            "tip"     : "Bengaluru's most famous pub street. Try Toit Brewpub for the best craft beer. Uber surge on weekends — book in advance.",
            "food_nearby": ["Toit Brewpub", "Byg Brewski", "Burma Burma"],
            "hidden_gem" : False,
            "tags"    : ["nightlife", "food", "modern", "youth", "evening"],
        },

        # ── DAY TRIPS ───────────────────────────────────────────────────
        {
            "id"      : 21,
            "name"    : "Nandi Hills",
            "area"    : "60 km from Bengaluru",
            "type"    : "Day Trip",
            "rating"  : 4.7,
            "timings" : "6:00 AM – 10:00 PM",
            "entry"   : "Rs. 20",
            "duration": "Full day",
            "best_for": ["Sunrise", "Trekking", "Cycling", "Paragliding"],
            "tip"     : "Leave by 4:30 AM to reach before sunrise. The fog-covered valley at dawn is breathtaking. Carry a jacket — it gets cold!",
            "food_nearby": ["Hilltop restaurants", "Carry your own food for sunrise"],
            "hidden_gem" : False,
            "tags"    : ["nature", "sunrise", "trekking", "day trip", "must visit"],
        },
        {
            "id"      : 22,
            "name"    : "Savandurga Hill",
            "area"    : "60 km from Bengaluru",
            "type"    : "Day Trip",
            "rating"  : 4.5,
            "timings" : "6:00 AM – 5:00 PM",
            "entry"   : "Free",
            "duration": "Full day",
            "best_for": ["Trekking", "Rock climbing", "Adventure"],
            "tip"     : "One of Asia's largest monolithic rocks. Moderate-difficult trek. Start early — very hot by afternoon. Wear proper shoes!",
            "food_nearby": ["Local dhabas at the base"],
            "hidden_gem" : False,
            "tags"    : ["nature", "trekking", "adventure", "day trip"],
        },
        {
            "id"      : 23,
            "name"    : "Mysuru (Mysore)",
            "area"    : "145 km from Bengaluru",
            "type"    : "Day Trip",
            "rating"  : 4.8,
            "timings" : "Full day trip",
            "entry"   : "Rs. 200 (Palace entry)",
            "duration": "Full day",
            "best_for": ["Heritage", "Culture", "Royalty", "Families"],
            "tip"     : "Visit during Dasara festival (October) for a magical royal procession. Mysore Palace on Sundays and holidays is illuminated with 97,000 bulbs!",
            "food_nearby": ["Mysore Pak sweet shops", "Hotel RRR for meals"],
            "hidden_gem" : False,
            "tags"    : ["heritage", "day trip", "must visit", "history"],
        },

        # ── HIDDEN GEMS ─────────────────────────────────────────────────
        {
            "id"      : 24,
            "name"    : "Bannerghatta Biological Park",
            "area"    : "South Bengaluru (22 km)",
            "type"    : "Nature",
            "rating"  : 4.4,
            "timings" : "9:30 AM – 5:00 PM (Closed Tuesdays)",
            "entry"   : "Rs. 80 (Adults) + Safari Rs. 350",
            "duration": "3–4 hours",
            "best_for": ["Wildlife", "Families", "Nature lovers"],
            "tip"     : "Take the jungle safari to see lions and tigers up close in their habitat. Book safari tickets in advance on weekends.",
            "food_nearby": ["Canteen inside the park"],
            "hidden_gem" : True,
            "tags"    : ["nature", "wildlife", "family", "adventure"],
        },
        {
            "id"      : 25,
            "name"    : "Janapada Loka (Folk Arts Museum)",
            "area"    : "58 km from Bengaluru",
            "type"    : "Cultural",
            "rating"  : 4.3,
            "timings" : "9:00 AM – 5:30 PM (Closed Wednesdays)",
            "entry"   : "Rs. 30",
            "duration": "2 hours",
            "best_for": ["Culture lovers", "Unique experience"],
            "tip"     : "Completely unique! Over 6,000 Karnataka folk art objects. Combine with a drive along the Mysore highway.",
            "food_nearby": ["Canteen inside", "Highway dhabas"],
            "hidden_gem" : True,
            "tags"    : ["culture", "hidden gem", "unique", "art"],
        },
    ],

    "budget_guide": {
        "backpacker": {
            "label"   : "Backpacker (Rs. 500–1000/day)",
            "stay"    : "Zostel or OYO hostel (Rs. 300–500)",
            "food"    : "Darshinis and VV Puram Food Street",
            "travel"  : "BMTC bus or Metro",
            "tips"    : ["Lalbagh and Cubbon Park are free", "MTR breakfast is worth it at Rs. 100"],
        },
        "mid_range": {
            "label"   : "Mid-Range (Rs. 2000–4000/day)",
            "stay"    : "Treebo or ibis hotel",
            "food"    : "Koramangala/Indiranagar restaurants",
            "travel"  : "Metro + Ola/Uber",
            "tips"    : ["Visit Bangalore Palace", "Try craft beer at Toit"],
        },
        "luxury": {
            "label"   : "Luxury (Rs. 7000+/day)",
            "stay"    : "ITC Gardenia, Taj West End, Oberoi",
            "food"    : "Karavalli, The Only Place, Rim Naam",
            "travel"  : "Private cab",
            "tips"    : ["UB City shopping", "Sunset dinner at Skyye rooftop bar"],
        },
    },

    "transport": {
        "Metro"       : "Fastest! Namma Metro covers most tourist spots. Rs. 10–55 per trip.",
        "BMTC Bus"    : "Cheapest at Rs. 5–30. Use BMTC app for routes.",
        "Ola/Uber"    : "Most convenient. Surge pricing on weekends.",
        "Auto-rickshaw": "Negotiate fare or insist on meter. Typical trip: Rs. 50–150.",
        "Rapido Bike" : "Cheapest for solo travel. Rs. 20–80 for short distances.",
    },

    "emergency": {
        "Police"          : "100",
        "Ambulance"       : "108",
        "Fire"            : "101",
        "Tourist Helpline": "1800-425-4747",
        "Women Helpline"  : "1091",
        "BMTC Helpline"   : "080-22281100",
    },

    "local_tips": [
        "Bengaluru traffic is worst 8–10 AM and 5–8 PM. Plan sightseeing midday.",
        "The city is called 'Bengaluru' officially but locals still say 'Bangalore'.",
        "Carry a light jacket even in summer — it can get cool after evening rains.",
        "Filter coffee (kaapi) here is a religion — try it at any old-school darshini.",
        "Bengaluru has 900+ lakes but most are polluted. Sankey Tank is the cleanest.",
        "Avoid asking auto-rickshaw drivers to go to Silk Board — worst traffic junction in India!",
    ],
}

# ══════════════════════════════════════════════════════════════════════════
#  WISHLIST
# ══════════════════════════════════════════════════════════════════════════
def load_wishlist():
    if os.path.exists(WISHLIST_FILE):
        with open(WISHLIST_FILE) as f:
            return json.load(f)
    return []

def save_wishlist(wl):
    with open(WISHLIST_FILE, "w") as f:
        json.dump(wl, f, indent=2)

# ══════════════════════════════════════════════════════════════════════════
#  DISPLAY HELPERS
# ══════════════════════════════════════════════════════════════════════════
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_header():
    clear()
    print(f"\n{CYAN}{BOLD}╔══════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}{BOLD}║   AI TOUR GUIDER — BENGALURU EDITION                ║{RESET}")
    print(f"{CYAN}║   Author: B. Siddesh | github.com/BSIDDESH          ║{RESET}")
    print(f"{CYAN}{BOLD}╚══════════════════════════════════════════════════════╝{RESET}\n")

def stars(rating):
    full  = int(rating)
    empty = 5 - full
    return f"{YELLOW}{'★' * full}{'☆' * empty}{RESET} {rating}"

def show_place_card(p, idx=None):
    prefix = f"[{idx}] " if idx else ""
    gem    = f" {MAGENTA}[HIDDEN GEM]{RESET}" if p.get("hidden_gem") else ""
    print(f"\n  {BLUE}{BOLD}{prefix}{p['name']}{RESET}{gem}")
    print(f"  {'─'*50}")
    print(f"  Area      : {p['area']}")
    print(f"  Type      : {p['type']}")
    print(f"  Rating    : {stars(p['rating'])}")
    print(f"  Timings   : {p['timings']}")
    print(f"  Entry     : {GREEN}{p['entry']}{RESET}")
    print(f"  Duration  : {p['duration']}")
    print(f"  Best For  : {', '.join(p['best_for'])}")
    print(f"  {CYAN}AI Tip: {p['tip']}{RESET}")
    print(f"  Food Near : {', '.join(p['food_nearby'])}")

# ══════════════════════════════════════════════════════════════════════════
#  MENU FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════
def city_overview():
    B = BENGALURU
    print(f"\n{CYAN}{BOLD}  BENGALURU — {B['nickname']}{RESET}")
    print(f"  {'═'*55}")
    print(f"  Founded    : {B['founded']}")
    print(f"  Population : {B['population']}")
    print(f"  Famous For : {B['famous_for']}")
    print(f"  Best Time  : {GREEN}{B['best_time']}{RESET}")
    print(f"  Avoid      : {RED}{B['avoid']}{RESET}")
    print(f"  Language   : {B['language']}")
    print(f"  Fun Fact   : {YELLOW}{B['fun_fact']}{RESET}")

    print(f"\n  {BOLD}AREAS OF BENGALURU:{RESET}")
    for area, spots in B["areas"].items():
        print(f"  {BLUE}{area:<10}{RESET} : {', '.join(spots)}")

    print(f"\n  {BOLD}TRANSPORT OPTIONS:{RESET}")
    for mode, desc in B["transport"].items():
        print(f"  {CYAN}{mode:<20}{RESET} : {desc}")

    print(f"\n  {BOLD}LOCAL TIPS:{RESET}")
    for i, tip in enumerate(B["local_tips"], 1):
        print(f"  {i}. {tip}")

    print(f"\n  {BOLD}EMERGENCY NUMBERS:{RESET}")
    for service, num in B["emergency"].items():
        print(f"  {service:<22} : {RED}{BOLD}{num}{RESET}")

def browse_all_places():
    places = BENGALURU["places"]
    print(f"\n  {BOLD}ALL PLACES IN BENGALURU ({len(places)} total){RESET}")
    type_order = ["Nature","Heritage","Spiritual","Food","Shopping","Entertainment","Day Trip","Cultural"]
    for ptype in type_order:
        group = [p for p in places if p["type"] == ptype]
        if not group: continue
        print(f"\n  {YELLOW}{BOLD}── {ptype.upper()} ──────────────────{RESET}")
        for p in group:
            gem = f" {MAGENTA}★{RESET}" if p.get("hidden_gem") else ""
            print(f"  [{p['id']:>2}] {BLUE}{p['name']}{RESET}{gem}  {stars(p['rating'])}  |  {DIM}{p['area']}{RESET}")

def ai_recommend(wishlist):
    print(f"\n  {BOLD}AI PERSONALISED RECOMMENDATION ENGINE{RESET}")
    print(f"  {'─'*42}")
    print(f"\n  What type of traveller are you?")
    print(f"  1. Nature & Outdoors Lover")
    print(f"  2. History & Heritage Fan")
    print(f"  3. Foodie (Street Food & Restaurants)")
    print(f"  4. Shopaholic")
    print(f"  5. Spiritual Seeker")
    print(f"  6. Adventure & Thrill Seeker")
    print(f"  7. Nightlife & Modern Scene")
    print(f"  8. Student / Budget Traveller")

    try:
        pref = int(input("\n  Your type (1-8): "))
    except ValueError:
        print(f"  {RED}Invalid!{RESET}"); return

    try:
        budget = int(input("  Daily budget (Rs): "))
    except ValueError:
        budget = 1500

    try:
        days = int(input("  How many days in Bengaluru? "))
    except ValueError:
        days = 2

    tag_map = {
        1: ["nature", "peaceful", "morning"],
        2: ["heritage", "history", "architecture"],
        3: ["food", "street food", "must visit", "traditional"],
        4: ["shopping", "bargain", "budget"],
        5: ["spiritual", "peaceful", "free"],
        6: ["adventure", "trekking", "day trip"],
        7: ["nightlife", "modern", "youth", "evening"],
        8: ["free", "budget", "students", "hidden gem"],
    }

    pref_tags = tag_map.get(pref, [])
    all_places = BENGALURU["places"]

    # Score each place
    scored = []
    for p in all_places:
        score = sum(1 for t in pref_tags if t in p["tags"])
        if score > 0:
            scored.append((score, p["rating"], p))

    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    top = [item[2] for item in scored[:min(6, len(scored))]]

    if not top:
        top = sorted(all_places, key=lambda x: x["rating"], reverse=True)[:5]

    # Budget category
    if budget < 1000:
        bcat = "backpacker"
    elif budget < 5000:
        bcat = "mid_range"
    else:
        bcat = "luxury"

    bguide = BENGALURU["budget_guide"][bcat]

    print(f"\n  {GREEN}{BOLD}AI RECOMMENDATIONS FOR YOU{RESET}")
    print(f"  {'═'*50}")
    print(f"  Budget Plan : {YELLOW}{bguide['label']}{RESET}")
    print(f"  Stay At     : {bguide['stay']}")
    print(f"  Eat At      : {bguide['food']}")
    print(f"  Travel By   : {bguide['travel']}")
    print(f"  {'─'*50}")

    print(f"\n  {BOLD}Top {len(top)} Places For You:{RESET}")
    for i, p in enumerate(top, 1):
        gem = f" {MAGENTA}[HIDDEN GEM!]{RESET}" if p.get("hidden_gem") else ""
        print(f"\n  {i}. {BLUE}{BOLD}{p['name']}{RESET}{gem}")
        print(f"     {stars(p['rating'])}  |  {p['type']}  |  Entry: {GREEN}{p['entry']}{RESET}")
        print(f"     {CYAN}Tip: {p['tip']}{RESET}")

    # Add to wishlist prompt
    ans = input(f"\n  Save these to wishlist? (y/n): ").strip().lower()
    if ans == "y":
        for p in top:
            wishlist.append({"place": p["name"], "area": p["area"],
                             "date": datetime.now().strftime("%Y-%m-%d")})
        save_wishlist(wishlist)
        print(f"  {GREEN}✓ {len(top)} places saved to wishlist!{RESET}")

def plan_itinerary():
    print(f"\n  {BOLD}SMART ITINERARY PLANNER{RESET}")
    print(f"  {'─'*40}")
    try:
        days = int(input("  How many days in Bengaluru? "))
    except ValueError:
        print(f"  {RED}Invalid!{RESET}"); return

    all_places = BENGALURU["places"]
    rated = sorted(all_places, key=lambda x: x["rating"], reverse=True)

    time_slots = [
        ("🌅 Early Morning (6–8 AM) ", "morning"),
        ("☕ Morning     (9–12 PM)  ", ""),
        ("🌞 Afternoon   (12–4 PM)  ", ""),
        ("🌆 Evening     (4–8 PM)   ", "evening"),
        ("🌙 Night       (8 PM+)    ", "night"),
    ]

    day_themes = {
        1: ("Central Bengaluru — Heritage & Nature",  ["nature","heritage","free"]),
        2: ("Food, Culture & Shopping",               ["food","shopping","culture"]),
        3: ("Spiritual & Hidden Gems",                ["spiritual","hidden gem","unique"]),
        4: ("Day Trip & Adventure",                   ["day trip","adventure","trekking"]),
        5: ("Entertainment & Nightlife",              ["entertainment","nightlife","modern"]),
    }

    print(f"\n  {CYAN}{BOLD}YOUR {days}-DAY BENGALURU ITINERARY{RESET}")
    print(f"  {'═'*52}")

    used_ids = set()
    for day in range(1, days + 1):
        theme, tags = day_themes.get(day, (f"Day {day} Exploration", []))
        print(f"\n  {YELLOW}{BOLD}DAY {day} — {theme}{RESET}")
        print(f"  {'─'*48}")

        # Pick best places for the day's theme
        day_places = []
        for p in rated:
            if p["id"] not in used_ids:
                tag_match = any(t in p["tags"] for t in tags) if tags else True
                if tag_match:
                    day_places.append(p)
                    used_ids.add(p["id"])
                if len(day_places) >= 3:
                    break

        # Fallback: just pick highest rated unused
        if not day_places:
            for p in rated:
                if p["id"] not in used_ids:
                    day_places.append(p)
                    used_ids.add(p["id"])
                    if len(day_places) >= 3: break

        for i, (slot_label, slot_tag) in enumerate(time_slots[:3]):
            if i < len(day_places):
                p = day_places[i]
                gem = f" {MAGENTA}[Hidden Gem!]{RESET}" if p.get("hidden_gem") else ""
                print(f"\n  {slot_label}")
                print(f"    {BLUE}{BOLD}{p['name']}{RESET}{gem}")
                print(f"    Entry: {GREEN}{p['entry']}{RESET}  |  Duration: {p['duration']}")
                print(f"    {CYAN}Tip: {p['tip']}{RESET}")
                if p["food_nearby"]:
                    print(f"    Food: {p['food_nearby'][0]}")

    print(f"\n  {BOLD}TRANSPORT TIP FOR YOUR TRIP:{RESET}")
    for mode, desc in BENGALURU["transport"].items():
        print(f"  • {CYAN}{mode}{RESET}: {desc}")

def view_by_type():
    types = sorted(set(p["type"] for p in BENGALURU["places"]))
    print(f"\n  {BOLD}FILTER BY TYPE:{RESET}")
    for i, t in enumerate(types, 1):
        count = sum(1 for p in BENGALURU["places"] if p["type"] == t)
        print(f"  {i}. {t} ({count} places)")
    try:
        choice = int(input("\n  Enter number: "))
        selected_type = types[choice - 1]
    except (ValueError, IndexError):
        print(f"  {RED}Invalid!{RESET}"); return

    filtered = [p for p in BENGALURU["places"] if p["type"] == selected_type]
    print(f"\n  {YELLOW}{BOLD}{selected_type.upper()} PLACES IN BENGALURU{RESET}")
    for p in sorted(filtered, key=lambda x: x["rating"], reverse=True):
        show_place_card(p, p["id"])

def hidden_gems():
    gems = [p for p in BENGALURU["places"] if p.get("hidden_gem")]
    print(f"\n  {MAGENTA}{BOLD}BENGALURU HIDDEN GEMS — Places Most Tourists Miss!{RESET}")
    print(f"  {'═'*52}")
    for p in gems:
        show_place_card(p)

def budget_guide():
    print(f"\n  {BOLD}BENGALURU BUDGET GUIDE{RESET}")
    print(f"  {'═'*50}")
    for key, data in BENGALURU["budget_guide"].items():
        col = GREEN if key == "backpacker" else YELLOW if key == "mid_range" else RED
        print(f"\n  {col}{BOLD}{data['label']}{RESET}")
        print(f"  Stay   : {data['stay']}")
        print(f"  Food   : {data['food']}")
        print(f"  Travel : {data['travel']}")
        for tip in data["tips"]:
            print(f"  • {tip}")

def view_wishlist(wishlist):
    print(f"\n  {BOLD}YOUR WISHLIST ({len(wishlist)} places){RESET}")
    if not wishlist:
        print(f"  {YELLOW}Empty! Use AI Recommendations to add places.{RESET}")
        return
    for i, item in enumerate(wishlist, 1):
        print(f"  {i}. {BLUE}{item['place']}{RESET}  —  {item['area']}  (Saved: {item['date']})")

    ans = input("\n  Clear wishlist? (y/n): ").strip().lower()
    if ans == "y":
        wishlist.clear()
        save_wishlist(wishlist)
        print(f"  {GREEN}Wishlist cleared!{RESET}")

# ══════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════
def main():
    wishlist = load_wishlist()

    while True:
        print_header()
        print(f"  {BOLD}MAIN MENU — Bengaluru has {len(BENGALURU['places'])} handpicked places for you!{RESET}")
        print(f"  {'─'*50}")
        print(f"  1.  City Overview & Local Tips")
        print(f"  2.  Browse All Places")
        print(f"  3.  AI Personalised Recommendations")
        print(f"  4.  Plan My Itinerary (Day-wise)")
        print(f"  5.  Filter Places by Type")
        print(f"  6.  {MAGENTA}Hidden Gems (Places Tourists Miss!){RESET}")
        print(f"  7.  Budget Guide")
        print(f"  8.  My Wishlist")
        print(f"  9.  Exit")
        print(f"  {'─'*50}")

        choice = input(f"\n  Enter choice (1-9): ").strip()

        if   choice == "1": city_overview()
        elif choice == "2": browse_all_places()
        elif choice == "3": ai_recommend(wishlist)
        elif choice == "4": plan_itinerary()
        elif choice == "5": view_by_type()
        elif choice == "6": hidden_gems()
        elif choice == "7": budget_guide()
        elif choice == "8": view_wishlist(wishlist)
        elif choice == "9":
            print(f"\n  {GREEN}Enjoy Bengaluru! — B. Siddesh | github.com/BSIDDESH{RESET}\n")
            break
        else:
            print(f"  {RED}Invalid! Enter 1-9.{RESET}")

        input(f"\n  {BLUE}Press Enter to continue...{RESET}")

if __name__ == "__main__":
    main()
