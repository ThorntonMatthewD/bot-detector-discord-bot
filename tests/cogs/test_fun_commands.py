import pytest
import discord.ext.test as dpytest

from conftest import test_bot
from src.cogs.fun_commands import funCommands

@pytest.fixture(scope='module')
async def set_up_bot(test_bot):
    await test_bot.add_cog(funCommands(test_bot))
    yield test_bot

@pytest.mark.asyncio
async def test_poke(set_up_bot):
    dpytest.configure(set_up_bot)
    await dyptest.message("!poke")
    assert dpytest.verify().message().contains().content("Teehee")
