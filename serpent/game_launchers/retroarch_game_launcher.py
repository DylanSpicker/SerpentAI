from serpent.game_launcher import GameLauncher, GameLauncherException
from serpent.utilities import is_linux, is_macos, is_windows

import shlex
import subprocess


class RetroarchGameLauncher(GameLauncher):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def launch(self, **kwargs):
        core_path = kwargs.get("core_path")
        rom_path = kwargs.get("rom_path")

        if core_path is None:
            raise GameLauncherException("A 'core_path' kwarg is required...")

        if rom_path is None:
            raise GameLauncherException("A 'rom_path' kwarg is required...")

        launch_list = ["retroarch", "-L", core_path, rom_path]

        if is_linux():
            subprocess.Popen(launch_list)
        elif is_macos():
            subprocess.Popen(launch_list)
        elif is_windows():
            subprocess.Popen(launch_list)