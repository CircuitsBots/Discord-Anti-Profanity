from discord.ext import commands

from main import Bot


class Base(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(
            f"Logged in as {self.bot.user.name} "
            f"in {len(self.bot.guilds)} guilds!"
        )


def setup(bot: Bot) -> None:
    bot.add_cog(Base(bot))
