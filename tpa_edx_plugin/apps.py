"""
App configuration for tpa_edx_plugin.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class TPAEdxPluginConfig(AppConfig):
    """
    TPA edX Plugin configuration.
    """
    name = 'tpa_edx_plugin'
    verbose_name = 'TPA edX Plugin'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'tpa_edx_plugin',
                'regex': r'^tpa_edx_plugin/',
                'relative_path': 'urls',
            },
            'cms.djangoapp': {
                'namespace': 'tpa_edx_plugin',
                'regex': r'^tpa_edx_plugin/',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
            'cms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
        }
    }

    def ready(self):
        from .signals import receivers
