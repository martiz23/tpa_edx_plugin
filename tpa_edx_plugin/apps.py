"""
App configuration for tpa_edx_plugin.
"""

from __future__ import unicode_literals

from django.apps import AppConfig
from edx_django_utils.plugins import PluginSettings, PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType

class TPAEdxPluginConfig(AppConfig):
    """
    TPA edX Plugin configuration.
    """
    name = 'tpa_edx_plugin'
    verbose_name = 'TPA edX Plugin'

    plugin_app = {
      PluginURLs.CONFIG: {
           ProjectType.LMS: {
                PluginURLs.NAMESPACE: name,
                PluginURLs.REGEX: "^tpa-edx-plugin/",
                PluginURLs.RELATIVE_PATH: "urls",
            },
        },
       PluginSettings.CONFIG: {
            ProjectType.LMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: "settings.common"},
                SettingsType.PRODUCTION: {PluginSettings.RELATIVE_PATH: "settings.production"},                
            },
        }
    }

    def ready(self):
        from .signals import receivers
        print("{label} is ready.".format(label=self.label))
