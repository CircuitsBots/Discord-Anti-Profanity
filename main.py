from typing import Dict

from discord.ext import commands

import config


EXTENSIONS = [
    "cogs.base",
    "cogs.filter_lang"
]


class Bot(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.offenses: Dict[int, int] = {}

    def run(self, *args, **kwargs) -> None:
        for ext in EXTENSIONS:
            self.load_extension(ext)

        super().run(*args, **kwargs)


if __name__ == '__main__':
    bot = Bot(
        command_prefix=config.PREFIX
    )
    bot.run(config.TOKEN)
