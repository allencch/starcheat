"""
Qt techs management dialog
"""

from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PIL.ImageQt import ImageQt

import assets, qt_techs
from config import Config

class Techs():
    def __init__(self, main_window):
        self.dialog = QDialog(main_window.window)
        self.ui = qt_techs.Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.main_window = main_window

        assets_db_file = Config().read("assets_db")
        starbound_folder = Config().read("starbound_folder")
        self.assets = assets.Assets(assets_db_file, starbound_folder)
        self.player = main_window.player
