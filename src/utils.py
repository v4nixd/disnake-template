from disnake.ext import commands


class Utils:
    @staticmethod
    def load_cogs(bot: commands.InteractionBot) -> None:
        print("Loading cogs")
        bot.load_extensions("src/cogs/events")
        print("Cogs loaded")
