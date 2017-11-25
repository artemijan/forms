class Base():
    """The base configuration."""
    DEBUG = False
    DATABASE = 'local.db'


CONFIG = {
    "dev": Base,
}
