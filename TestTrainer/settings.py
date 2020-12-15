"""
Django settings for TestTrainer project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from corsheaders.defaults import default_headers
from datetime import timedelta
# from person.models import PersonUser

from django.utils.translation import gettext as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kf_tm4on1c1jt=ua59wu)b6n2m5ly9*&84eeh7gdr=8x4%0ke5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'testtrainer.benda.is',
    '127.0.0.1',
    '127.0.0.1:8080',
    '127.0.0.1:8000',
    'localhost',
    'localhost:8080',
    '192.168.31.139',
    '192.168.31.139:8000',
    '192.168.31.139:8080',
    'einars-macbook-pro.local',
    'einars-macbook-pro.local:8000',
    'einars-macbook-pro.local:8080',
    'test.enam.is:8000',
    'test.enam.is:8080',
    'test.enam.is',
    'api.enam.is:8000',
    'api.enam.is:8080',
    'api.enam.is',
    'https://einars-macbook-pro.local',
    'https://einars-macbook-pro.local:8000',
    'https://einars-macbook-pro.local:8080',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:8080",
    "https://localhost:8000",
    "https://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
    "https://127.0.0.1:8000",
    "https://127.0.0.1:8080",
    "http://192.168.31.139",
    "http://192.168.31.139:8000",
    "http://192.168.31.139:8080",
    'http://einars-macbook-pro.local',
    'http://einars-macbook-pro.local:8000',
    'http://einars-macbook-pro.local:8080',
    'https://einars-macbook-pro.local',
    'https://einars-macbook-pro.local:8000',
    'https://einars-macbook-pro.local:8080',
    'http://0.0.0.0',
    'http://0.0.0.0:8000',
    'http://0.0.0.0:8080',
    'http://127.0.0.1',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:8081',
    'https://127.0.0.1',
    'https://127.0.0.1:8000',
    'https://127.0.0.1:8080',
    'http://test.enam.is:8000',
    'http://test.enam.is:8080',
    'http://test.enam.is',
    'https://test.enam.is:8000',
    'https://test.enam.is:8080',
    'https://test.enam.is',
    'https://api.enam.is:8000',
    'https://api.enam.is:8080',
    'https://api.enam.is',
    'https://enam.is:8000',
    'https://enam.is:8080',
    'https://enam.is',
]

CORS_ORIGIN_WHITELIST = CORS_ALLOWED_ORIGINS

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = default_headers + (
    'contenttype',
)

# Application definition

INSTALLED_APPS = [
    'sslserver',
    'modeltranslation',
    'baton',
    # 'admin_interface',
    # 'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
#    'jet_django',
    'corsheaders',
    'base',
    'person',
    'questions',
    'baton.autodiscover',
    'rest_framework',
    'rest_framework_jwt',
    'rest_framework_simplejwt.token_blacklist',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'TestTrainer.urls'

# X_FRAME_OPTIONS='SAMEORIGIN'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'TestTrainer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testtrainerdb',
        'HOST': '127.0.0.1',
        # 'HOST': 'nature.is',
        'USER': 'vefur',
        'PASSWORD': 'planta777',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# AUTH_USER_MODEL = 'person.PersonUser'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGES = (
    ('is', 'Íslenska'),
    ('en', 'Enska'),
    ('de', 'Þýska'),
)

LANGUAGE_CODE = 'is'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'is'

# Contains the path list where Django should look into for django.po files for all supported languages
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)



REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}



SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=240),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=180),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = BASE_DIR + '/static/'
MEDIA_ROOT = BASE_DIR + '/media/'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


BATON = {
    'SITE_HEADER': 'TestTrainer',
    'SITE_TITLE': 'TestTrainer Admin',
    'INDEX_TITLE': 'TestTrainer Admin',
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
}
"""
https://manage.auth0.com/
einar@abending.is Safari password
"""


"""
AUTH0_DOMAIN = 'dev-4z-pkajz.eu.auth0.com'
API_IDENTIFIER = 'jLtBvFXWbLeJQ3m9d3iDS8EkaCUOgbra'
PUBLIC_KEY = None#{"keys":[{"alg":"RS256","kty":"RSA","use":"sig","n":"wLIq6Cb38YR2jLXtw3g0As_9Xfgy876Wd8MT53fa7eWpH376kHUWdQ-3x0bgD6ZSC3jV6wv_AyvYmkdf_Kb7ybar6oxizB5PphalZp19CpoXFCcpDzksaebA-M8GR_KlG16wvTC7-NjINpQbfsyWCdTVeCVsrwLUDs8uPnTTiAoGU5zYdSnzBeWPh4Wn6iKjrBHRSFCeMXXwNmFl4aOFwF4YOelner2T3HTkzTxbBkmBEJY-LaRXyuWY_JCRSZnwaYcMzpQ__63hVe6M_2ooJJ0xTGS4Gs27OhlzyPrKI4vaCfV8xZthLtw8PPUUDTVkd9jZnQvW1LU7HJYhvNacYw","e":"AQAB","kid":"bYX5-I4ACVE_DLFNYmqP4","x5t":"gnRFkBPzi5dmfrDVLsk-dQyLKrM","x5c":["MIIDDTCCAfWgAwIBAgIJJcHIWS1VuPNjMA0GCSqGSIb3DQEBCwUAMCQxIjAgBgNVBAMTGWRldi00ei1wa2Fqei5ldS5hdXRoMC5jb20wHhcNMjAxMTIzMDUyNTA5WhcNMzQwODAyMDUyNTA5WjAkMSIwIAYDVQQDExlkZXYtNHotcGthanouZXUuYXV0aDAuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwLIq6Cb38YR2jLXtw3g0As/9Xfgy876Wd8MT53fa7eWpH376kHUWdQ+3x0bgD6ZSC3jV6wv/AyvYmkdf/Kb7ybar6oxizB5PphalZp19CpoXFCcpDzksaebA+M8GR/KlG16wvTC7+NjINpQbfsyWCdTVeCVsrwLUDs8uPnTTiAoGU5zYdSnzBeWPh4Wn6iKjrBHRSFCeMXXwNmFl4aOFwF4YOelner2T3HTkzTxbBkmBEJY+LaRXyuWY/JCRSZnwaYcMzpQ//63hVe6M/2ooJJ0xTGS4Gs27OhlzyPrKI4vaCfV8xZthLtw8PPUUDTVkd9jZnQvW1LU7HJYhvNacYwIDAQABo0IwQDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBS2vssNv06986tmeu4H+VZKdLfm+zAOBgNVHQ8BAf8EBAMCAoQwDQYJKoZIhvcNAQELBQADggEBAKIiw+MG0+4ZR27m326wrCJkBLrTMVS8atf9wg5Pt1b5Vk8Ds+rpuEg/oUhAZiXaHdI/Wh7i4sJTLoAjjU0bLRvZrKQzBvRhou1fPLYzkNMLGOTXETiDlXBz8QJgp7g6gTCJZpxt3PT6K5459JHhmQ14y3YH6npeUR1c4FREFtKiexBJTEPiWJW4dAd+NOtXH9iRw5qTYE27q8OBi50dmtLEVraeIbjTSpDM2pMMEnHg81TXoIm6vFChBOZHLFVYQHw5oyQuusNAKcAgcsnf/YTfpG1aI6VxCk0Tqv9bzn2qFScB8XljTOI6xrMnqn0WR8QAjyjxIlkW1welmyaIetM="]},{"alg":"RS256","kty":"RSA","use":"sig","n":"v6rXNE1-QP-vvVruTu9d6us3B7zRUBfsjBwYAk-m_xrlh6W7YU8WZzXX6W_TsU19Nn87z02pRW47mnDNIF2J0XwWv4f-Css-wGRMpNHdGKm8n_0Vd9oOV2m-nn4jHVcEqgFoFFcZMoneBo_iJiLPq4x7ZvdaK6wvRS7urWXUMFEs87oghsppaTZBy8pa6Xc-B09h4KHQFP8nHjBQKYBG0k7KD1gAH5aSVa1nq_f8NnoeylnQ5lMdgu1sXZJqLlN48bL-_fLeeTiarVfRlVDd0ouxsqZhOJ0Y9FohpcirzsGVM-_1GRUoGJJaseogZDDRdr5rieR-YHifJUCV6DYcaw","e":"AQAB","kid":"X3uLwYwKGZjhV5I2yzePJ","x5t":"5LIjb9_i58_YMhW4VCMFGlMFCJI","x5c":["MIIDDTCCAfWgAwIBAgIJNzThu0wD2EdTMA0GCSqGSIb3DQEBCwUAMCQxIjAgBgNVBAMTGWRldi00ei1wa2Fqei5ldS5hdXRoMC5jb20wHhcNMjAxMTIzMDUyNTEwWhcNMzQwODAyMDUyNTEwWjAkMSIwIAYDVQQDExlkZXYtNHotcGthanouZXUuYXV0aDAuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv6rXNE1+QP+vvVruTu9d6us3B7zRUBfsjBwYAk+m/xrlh6W7YU8WZzXX6W/TsU19Nn87z02pRW47mnDNIF2J0XwWv4f+Css+wGRMpNHdGKm8n/0Vd9oOV2m+nn4jHVcEqgFoFFcZMoneBo/iJiLPq4x7ZvdaK6wvRS7urWXUMFEs87oghsppaTZBy8pa6Xc+B09h4KHQFP8nHjBQKYBG0k7KD1gAH5aSVa1nq/f8NnoeylnQ5lMdgu1sXZJqLlN48bL+/fLeeTiarVfRlVDd0ouxsqZhOJ0Y9FohpcirzsGVM+/1GRUoGJJaseogZDDRdr5rieR+YHifJUCV6DYcawIDAQABo0IwQDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBRhUEfTKvDAX/wxfo9rau7ZrNzT0TAOBgNVHQ8BAf8EBAMCAoQwDQYJKoZIhvcNAQELBQADggEBAHKuX8+iTp53LxM/4oRcCEIwJFRKNeUrAd3EfLaH0zuKzsZapL9txrbWT33AVwvC5F80cHuA7X12Gaf8j/uqlEWYtF82FBSARoBCxkd5YDm0v5zjzbWvG8FrWf+wWw95x8KaHHBq7QzMWVAsu2mzxQ5p+r6fxhXr9jsEBpG4PQ/yDwmXX3f7oFAPgdrKEX/wtDPbnzAJiSPGsXGaxAfXGxke4TX1jUkhNNoRiJeZKx/K04v1zYJUexhpl5GyacaGYzS44Hh/ERpVZ+FQb0NdpUaSPiGlxdeWrf02/toB8WSx2MU7Kmd64zPF+cFDJNwZ9XG/+M8PC2bYaF2ltdsIllk="]}]}
JWT_ISSUER = None # 'https://dev-4z-pkajz.eu.auth0.com'
#
if AUTH0_DOMAIN:
    jsonurl = request.urlopen('https://' + AUTH0_DOMAIN + '/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read().decode('utf-8'))
    cert = '-----BEGIN CERTIFICATE-----\n' + jwks['keys'][0]['x5c'][0] + '\n-----END CERTIFICATE-----'
    certificate = load_pem_x509_certificate(cert.encode('utf-8'), default_backend())
    PUBLIC_KEY = certificate.public_key()
    JWT_ISSUER = 'https://' + AUTH0_DOMAIN + '/'


def jwt_get_username_from_payload_handler(payload):
    return 'ebergmundur@gmail.com'


JWT_AUTH = {
    'JWT_PAYLOAD_GET_USERNAME_HANDLER': jwt_get_username_from_payload_handler,
    'JWT_PUBLIC_KEY': PUBLIC_KEY,
    'JWT_ALGORITHM': 'RS256',
    'JWT_AUDIENCE': API_IDENTIFIER,
    'JWT_ISSUER': JWT_ISSUER,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}
"""
