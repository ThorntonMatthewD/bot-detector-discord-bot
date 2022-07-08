import aiohttp
import discord
import pytest

from discord.ext.commands import Bot


@pytest.fixture
async def test_bot(event_loop):
    bot: discord.Client = Bot(
        command_prefix="!",
        loop=event_loop,
        intents=discord.Intents(
            messages=True,
            guilds=True,
            members=True,
            reactions=True,
            message_content=True,
        ),
    )
    async with aiohttp.ClientSession() as session:
        bot.Session = session

        yield bot
