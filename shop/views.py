import time
import random
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from .models import ProductSet, BackgroundMusic  # BackgroundMusic модели кошулду
from fuzzywuzzy import fuzz


# --- 📩 TELEGRAM ЖӨНӨТҮҮ ---
def send_telegram_message(name, phone, message):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    text = (
        f"🍰 *Жаңы заказ (SSMOD)*\n\n"
        f"👤 *Аты:* {name}\n"
        f"📞 *Тел:* {phone}\n"
        f"💬 *Билдирүү:* {message if message else 'Жок'}"
    )

    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'}

    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Telegram API Error: {response.text}")
    except Exception as e:
        print(f"Telegram Connection Error: {e}")


# --- 🤖 AI ЧАТ (АКЫЛДУУ БЕКЕР БОТ) ---
def strawberry_chat_api(request):
    user_query = request.GET.get('message') or request.POST.get('message', '')
    user_query = user_query.lower().strip()

    if not user_query:
        return JsonResponse({'reply': "Салам! 🍓 Кантип жардам берейин?"})

    knowledge_base = {
        "саламдашуу": {
            "keywords": ["салам", "привет", "hello", "амансызбы", "кандай", "кеч жарык", "кутуман"],
            "reply": "Саламатсызбы! SSMOD жардамчысымын 🍓 Сизге кандай жардам бере алам?"
        },
        "ыраазычылык": {
            "keywords": ["рахмат", "спасибо", "чоң рахмат", "ыраазы", "жакшы"],
            "reply": "Сизге да чоң рахмат! 😊✨"
        },
        "клубника": {
            "keywords": ["клубника", "кулпунай", "шоколад", "белек", "набор"],
            "reply": "Биз Бельгия шоколады менен капталган эң таттуу клубникаларды сунуштайбыз! 🍫🍓"
        },
        "торттор": {
            "keywords": ["торт", "вупи пай", "красный бархат", "молочная девочка", "заказ торт"],
            "reply": "Ооба, бизде ар кандай торттор бар. Заказды 1-2 күн мурун бериңиз 🍰"
        },
        "баалар": {
            "keywords": ["баа", "канча", "сом", "цена", "прайс", "дорого", "арзан"],
            "reply": "Баалар 800 сомдон башталат. Толук прайс 'Топтомдор' бөлүмүндө 💸"
        },
        "жеткирүү": {
            "keywords": ["жеткирүү", "доставка", "курьер", "алып келүү"],
            "reply": "Ош шаары ичинде жеткирүү 100-150 сом. 🚚"
        },
        "дарек": {
            "keywords": ["кайда", "адрес", "жер", "ориентир", "локация"],
            "reply": "Биз Ош шаарындабыз, Ленин көчөсүндө жайгашканбыз 📍"
        },
        "админ": {
            "keywords": ["админ", "жетекчи", "ким", "искак", "хозяин"],
            "reply": "Мен, Искак, SSMOD негиздөөчүсүмүн. Биз 2 жылдан бери Ошто эң таттуу белектерди жасап келебиз."
        }
        # ... калган базаңыз өзгөрүүсүз калат ...
    }

    for category in knowledge_base.values():
        for keyword in category["keywords"]:
            if keyword in user_query:
                return JsonResponse({'reply': category["reply"]})

    best_match = None
    highest_score = 0
    for category in knowledge_base.values():
        for keyword in category["keywords"]:
            score = fuzz.partial_ratio(user_query, keyword)
            if score > highest_score:
                highest_score = score
                best_match = category["reply"]

    if highest_score > 65:
        reply = best_match
    else:
        reply = random.choice([
            "Түшүнбөй калдым 🤔 Башкача жазып көрүңүз.",
            "Сурооңузду өзгөртүп көрүңүз 🍓",
            "Кечириңиз, бул боюнча маалыматым жок экен 😊"
        ])

    return JsonResponse({'reply': reply})


# --- 📄 PAGES (МУЗЫКА ЛОГИКАСЫ МЕНЕН) ---

def home(request):
    # Активдүү музыканы базадан алабыз
    active_music = BackgroundMusic.objects.filter(is_active=True).first()

    if request.method == "POST":
        user_name = request.POST.get('userName')
        user_phone = request.POST.get('userPhone')
        user_msg = request.POST.get('userMsg')

        if user_name and user_phone:
            send_telegram_message(user_name, user_phone, user_msg)
            messages.success(request, "Заказыңыз ийгиликтүү кабыл алынды! 🍓")
        else:
            messages.error(request, "Сураныч, атыңызды жана номериңизди толтуруңуз.")
        return redirect('home')

    products = ProductSet.objects.all()
    return render(request, 'shop/index.html', {
        'products': products,
        'active_music': active_music  # Музыка кошулду
    })


def price(request):
    active_music = BackgroundMusic.objects.filter(is_active=True).first()
    sets = ProductSet.objects.all()
    return render(request, 'shop/price.html', {
        'sets': sets,
        'active_music': active_music  # Музыка кошулду
    })


def about(request):
    active_music = BackgroundMusic.objects.filter(is_active=True).first()
    return render(request, 'shop/about.html', {
        'active_music': active_music  # Музыка кошулду
    })


def reviews(request):
    active_music = BackgroundMusic.objects.filter(is_active=True).first()
    return render(request, 'shop/reviews.html', {
        'active_music': active_music  # Музыка кошулду
    })


def contact(request):
    active_music = BackgroundMusic.objects.filter(is_active=True).first()
    return render(request, 'shop/contact.html', {
        'active_music': active_music  # Музыка кошулду
    })