from typing import Dict
from dotenv import dotenv_values

from ck_bot.utils.types import EnvDict


def parse_env_file() -> EnvDict:
    env_vars: Dict[str, str] = dotenv_values(".env")  # type: ignore
    config: EnvDict = EnvDict(
        DISCORD_CLIENT_TOKEN=env_vars["DISCORD_CLIENT_TOKEN"],
        SHOULD_SYNC_COMMANDS=env_vars["SHOULD_SYNC_COMMANDS"],
        SPOTIPY_CLIENT_ID=env_vars["SPOTIPY_CLIENT_ID"],
        SPOTIPY_CLIENT_SECRET=env_vars["SPOTIPY_CLIENT_SECRET"],
        SPOTIPY_REDIRECT_URI=env_vars["SPOTIPY_REDIRECT_URI"],
        SPOTIPY_SCOPE=env_vars["SPOTIPY_SCOPE"],
        SPOTIFY_USERNAME=env_vars["SPOTIFY_USERNAME"],
    )
    return config
