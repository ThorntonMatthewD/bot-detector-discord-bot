import aiohttp
import discord
import pytest

from discord.ext.commands import Bot

@pytest.fixture
async def test_bot():
    bot: discord.Client = Bot(command_prefix='!')
    bot.Session = aiohttp.ClientSession()

    yield bot