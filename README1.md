# "Zakwieciscie" польська онлайн-крамниця квітів

## Хто підтримує проект та вносить вклад у проект

🔘 **Підтримка та вклад:**
Проект підтримується та розробляється командою ентузіастів Django.

🔘 **Перелік учасників команди:**

- Пилипко Максим/Pylypko Maksym - лідер команди, розробник (Teamlead, Full-stack Developer)
[GitHub](https://github.com/MaxPylypko) [Figma](https://www.figma.com/@7683301f_66d3_4)

- Гончаров Єгор/Honcharov Yehor - розробник (Full-Stack Developer)
[GitHub](https://github.com/YehorHoncharov) [Figma](https://www.figma.com/@d4a8c8c6_69dd_4)

- Киприч Таїсія/Kyprych Taisiia - розробник (Full-Stack Developer)
[GitHub](https://github.com/Taisiia773) [Figma](https://www.figma.com/@taisiiakiprych)

## Що робить проект

🔘 **Назва проекту та короткий опис:**
"Zakwieciscie"- Цей проект представляє собою інтернет-магазин різноманітних товарів (в основному квітів), де користувачі можуть їх переглядати, замовляти та купувати. Магазин надає зручний інтерфейс для користувачів, а також адміністративну панель для управління товарами, замовленнями та користувачами.

🔘 **Корисність проекту:**
Проект є корисним як для користувачів, так і для розробників-початківців, оскільки він надає всі необхідні інструменти для створення повноцінного вебсайту. Для початківців це чудова можливість вивчити основи роботи з Django та здобути практичні навички.

## Як приступити до роботи

🔘 **Необхідні модулі Python:**
- Django
- Pillow

Короткий опис кожного модуля:
- **Django:** основний фреймворк для розробки вебдодатків на Python.
- **Pillow** бібліотека для роботи із зображенням, використовуєтся для коректної роботи медіа-файлів

🔘 **Інструкція по запуску проекту локально:**
1. Клонуйте репозиторій: `git clone https://github.com/MaxPylypko/zakwieciscie.git`
2. Перейдіть в директорію проекту: `cd zakwieciscie-main`
3. Встановіть необхідні залежності: `pip install -r requirements.txt`
4. Зробіть міграції бази даних: `python manage.py makemigrations catalog`
5. Застосуйте міграції `python manage.py migrate`
6. Запустіть сервер: `python manage.py runserver`

## Як користувач може отримати допомогу по вашому проекту

🔘 **Структура проекту:**
- **Основні застосунки:**
  - zakwieciscie/ - головний проект Django
  - authorize/ - додаток для управління користувачами та автентифікації
  - catalog/ - додаток з товарами (каталог)
  - contacts/ - додаток з контактами володарів магазину

🔘 **Приклад створення головногої функції відображення:**

```python
# main/views.py
from django.shortcuts import render

def main(request):
    return render(request, 'main/index.html')
```

🔘 **Налаштування Blueprint у файлі urls:**
```python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import main.views
import contacts.views
import authorize.views
import catalog.views
import order.views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", main.views.main, name='main'),
    path("contacts/", contacts.views.contacts, name='contacts'),
    
    path("signup/", authorize.views.sign_up, name='signup'),
    path("login/", authorize.views.log_in, name='login'),
    
    path("flowers/", catalog.views.flowers_catalog, name='flowers_catalog'),
    path("item/<int:item_id>", catalog.views.item, name='item'),
    path("add_to_cart/<int:item_id>", catalog.views.add_to_cart, name="add_to_cart"),

    path("cart/", order.views.cart, name='cart')
    # path("favs/", order.views.favs, name='favs')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


🔘 **Опис файла settings**
```python
from pathlib import Path
import os

# Будуємо шляхи всередині проекту так: BASE_DIR / 'підкаталог'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Налаштування для швидкого старту розробки - не підходить для продуктивного використання
# Див. https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# ПОПЕРЕДЖЕННЯ З БЕЗПЕКИ: тримайте секретний ключ використовуваний в продукції в секреті!
SECRET_KEY = 'django-insecure-t8212i+#=3g0n4k^@gvphmynrx1(@=4wkoxoss0d+y!2(b-(^8'

# ПОПЕРЕДЖЕННЯ З БЕЗПЕКИ: не використовуйте DEBUG у продукції!
DEBUG = True

ALLOWED_HOSTS = []

# Визначення додатків
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'authorize',
    'contacts',
    'catalog',
    'order'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zakwieciscie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'zakwieciscie.wsgi.application'

# База даних
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валідація паролів
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Локалізація
LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Статичні файли (CSS, JavaScript, Зображення)
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

# Тип поля для первинного ключа за замовчуванням
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

🔘 **Шаблони HTML:**
```html
{% extends 'main/base.html' %}  <!-- Розширює шаблон base.html -->

{% load static %}  <!-- Підключає статичні файли -->

{% block head %}  <!-- Початок блоку head -->
  <link rel="stylesheet" href="{% static 'catalog/css/catalog.css' %}">  <!-- Підключення стилів -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>  <!-- Підключення jQuery -->
{% endblock %}  <!-- Кінець блоку head -->


{% block content %}  <!-- Початок блоку content -->
  <img class="w-100" id="flowers-catalog-banner" src="{% static 'catalog/img/banner.png' %}" alt="Flowers catalog banner">  <!-- Банер каталогу квітів -->

  <!-- Секція фільтрів -->
  <div id="filters">
    <!-- Обгортка для правильного відображення space-between -->
    <div id="filters-wrapper">
      <!-- Кольори -->
      <button class="btn btn-light dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Кольори</button>
      <div class="dropdown">
        <div class="dropdown-menu">
          <!-- Пункти випадаючого меню з кольорами -->
          <div class="dropdown-item">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label" for="flexCheckDefault">Білий</label>
            </div>
          </div>

          <div class="dropdown-item">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label" for="flexCheckDefault">Рожевий</label>
            </div>
          </div>

          <div class="dropdown-item">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label" for="flexCheckDefault">Червоний</label>
            </div>
          </div>
        </div>
        <button id="apply-filter-btn">Застосувати</button>  <!-- Кнопка застосування фільтрів -->
      </div>
    </div>
  </div>

  <!-- Відображення товарів -->
  <div id="items">
    {% for flower in flowers %}
      <div class="card">
        <div id="img-wrapper" style="background-image: url({{flower.img.url}});">
          <div id="actions-wrapper">
              <a href="{% url 'add_to_cart' item_id=flower.id %}" style="text-decoration: none;">
                <button class="action-btn">Додати до кошика<i class="bi bi-cart2"></i></button>
              </a>
            <button class="action-btn">Додати до улюблених <i class="bi bi-heart-fill"></i></button>
          </div>
        </div>

        <div class="card-body">
          <a href="{% url 'item' item_id=flower.id %}"><h5 class="card-title">{{flower.name}}</h5></a>
          <p class="card-text">{{flower.description}}</p>
          <p class="price-text">{{flower.price}} зл</p>
        </div>
      </div>
    {% endfor %}
  </div>
{% endblock %}  <!-- Кінець блоку content -->

```

🔘 **Приклад views.py з коментарями:**
```python
# main/views.py
from django.shortcuts import render

# Головна сторінка
def home(request):
    return render(request, 'main/home.html')
```

🔘 **Приклад models.py з коментарями:**
```python
from django.db import models

# Оголошуємо модель Flower, яка буде наслідуватися від базового класу models.Model
class Flower(models.Model):
    # Поле name типу CharField з максимальною довжиною 255 символів
    name = models.CharField(max_length=255)
    # Поле color типу CharField з максимальною довжиною 255 символів
    color = models.CharField(max_length=255)
    # Поле description типу TextField для зберігання довшого тексту
    description = models.TextField()
    # Поле price типу FloatField для зберігання ціни
    price = models.FloatField()
    # Поле img типу ImageField для зберігання зображення, дозволяється null і пусте значення
    img = models.ImageField(null=True, blank=True)
    
    # Метод __str__ визначає, як об'єкти цього класу представляються у текстовому вигляді
    def __str__(self):
        return f"{self.name} | {self.color} | {self.price} zl"
    
    # Вкладений клас Meta для налаштувань моделі
    class Meta:
        # Читабельна назва моделі в однині
        verbose_name = "Flower"
        # Читабельна назва моделі в множині
        verbose_name_plural = "Flowers"
```


🔘 **Опис бази даних:**
SQLite3 - легка та зручна база даних для розробки. ID виконує роль первинного ключа у таблицях бази даних, забезпечуючи унікальність кожного запису.


## Висновок по роботі над проектом
Робота над цим проектом була дуже корисною. Ми здобули безцінний досвід роботи з Django, навчилися створювати складні вебдодатки та отримали знання, які допоможуть нам у майбутніх проектах.
