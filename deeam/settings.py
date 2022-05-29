DEEAM_PROJECT_SETTINGS = {
    'NAME': 'DEEAM',
    'VERSION': '0.0.1a',
}


DATABASES = {
    'default': {
        'ENGINE': 'sqlite',
        'NAME': DEEAM_PROJECT_SETTINGS.get('NAME'),
    },
}


DEBUG = True
