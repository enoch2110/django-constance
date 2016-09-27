from importlib import import_module

# TODO - import config so we don't need LazyConfig again?
# but this is causing tests.test_utils.UtilsTestCase to fail on py27-django-18
#from . import config, settings
from constance import LazyConfig, settings

config = LazyConfig()


def import_module_attr(path):
    package, module = path.rsplit('.', 1)
    return getattr(import_module(package), module)


def get_values():
    """
    Get dictionary of values from the backend
    :return:
    """

    # First load a mapping between config name and default value
    default_initial = ((name, options[0])
                       for name, options in settings.CONFIG.items())
    # Then update the mapping with actually values from the backend
    initial = dict(default_initial,
                   **dict(config._backend.mget(settings.CONFIG.keys())))

    return initial
