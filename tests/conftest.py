import aiohttp
import discord
import pytest

from discord.ext.commands import Bot

@pytest.fixture
async def test_bot():
    bot: discord.Client = Bot(command_prefix='!')
    async with aiohttp.ClientSession() as session:
        bot.Session = session

        yield bot