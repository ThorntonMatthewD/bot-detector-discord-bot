import asyncio
import pytest
import discord.ext.test as dpytest

from conftest import test_bot
from src.cogs.fun_commands import funCommands


@pytest.fixture(autouse=True)
async def set_up_bot(test_bot):
    await test_bot.add_cog(funCommands(test_bot))
    dpytest.configure(set_up_bot)
    return test_bot


@pytest.mark.asyncio
async def test_poke():
    await dpytest.message("!poke")
    assert dpytest.verify().message().contains().content("Teehee")