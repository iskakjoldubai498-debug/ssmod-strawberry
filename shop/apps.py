from django.apps import AppConfig
import cloudinary

class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

    def ready(self):
        # Cloudinary конфигурациясын бул жерге мажбурлап киргизебиз
        cloudinary.config(
            cloud_name = 'dtuyalp6m',
            api_key = '636667862685854',
            api_secret = 'PgRp9Z7dBhdkoVTk0K1sa1I1390'
        )