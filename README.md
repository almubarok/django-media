# How to use

  

### Add this code to `settings.py` 
```
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```

### Add this code to `urls.py`
```
from django.conf import settings
from django.conf.urls.static import static

.
.
.


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
  
  

-  `pip3 install Pillow`  [details](https://pypi.org/project/Pillow/)

-  `python3 manage.py migrate`

-  `python3 manage.py createsuperuser`

-  `python3 manage.py runserver`
