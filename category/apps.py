from django.apps import AppConfig


class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'category'

    def ready(self):
        import components.category_card.category_card