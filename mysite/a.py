import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'blog/static/blog/')
print(STATIC_ROOT)

MEDIA_URL = '/blog/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'blog/static/blog/media/img/')

print(MEDIA_ROOT)
