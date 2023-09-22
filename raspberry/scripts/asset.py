import os


class AssetManager:
    """
    AssetManager encapluates acessing server assets

    Why to use AssetManager when anybody can configure flask to control
    where the "templates" and "static" folders (with all web stuff) are
    located ? Flask does not take care of some other stuff, like images,
    videos and, basically everything else, so we would need AssetManager
    anyway. Since it would be used anyway, its better to use it with web
    stuff as well.
    """

    ASSETS_DIR = None

    @staticmethod
    def get_path(name: str) -> str:
        """
        Convert path to the asset.

        Parameters
        ----------
        name : str
            Path to the asset, relative to the assets folder

        Returns
        -------
        str:
            Full absolute path to the filename
        """
        return os.path.join(AssetManager.ASSETS_DIR, name)

    @staticmethod
    def get_html(name: str) -> str:
        """Alias for "get_path" function, to access html files"""
        return AssetManager.get_path(os.path.join("templates", name))

    @staticmethod
    def get_css(name: str) -> str:
        """Alias for "get_path: function, to access css files"""
        return AssetManager.get_path(os.path.join("css", name))

    @staticmethod
    def get_js(name: str) -> str:
        """Alias for "get_path: function, to access javascript files"""
        return AssetManager.get_path(os.path.join("js", name))

    @staticmethod
    def init() -> None:
        """Initialize the asset manager"""
        raspberry = os.path.dirname(os.path.dirname(__file__))
        AssetManager.ASSETS_DIR = os.path.join(raspberry, "assets")
