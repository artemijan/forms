class Base():
    """The base configuration."""
    DEBUG = False
    DATABASE = 'database.db'


CONFIG = {
    "dev": Base,
}
