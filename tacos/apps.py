"""Taco app"""

from django.apps import AppConfig


class TacosConfig(AppConfig):
    """Taco app config"""
    name = 'tacos'
    verbose_name = 'Tacos'

    def ready(self):
        import tacos.signals
