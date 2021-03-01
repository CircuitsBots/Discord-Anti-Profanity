import discord
from discord.ext import commands
from profanity_check import predict_prob

import config
from main import Bot


def predict(text: str) -> float:
    return predict_prob([text])[0]


class FilterLang(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        value = predict(message.content)
        if value > config.TOLERANCE:
            await message.delete()
            await message.channel.send(
                f"{message.author.mention}'s message was deleted.",
                delete_after=5
            )
            self.bot.offenses.setdefault(message.author.id, 0)
            self.bot.offenses[message.author.id] += 1


def setup(bot: Bot) -> None:
    bot.add_cog(FilterLang(bot))
