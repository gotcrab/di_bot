from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    pass

@dataclass
class TgBot:
    token: str
    # adm_ids: list[int]

@dataclass
class Config:
    tg_bot: TgBot
    # db: DatabaseConfig

def load_config(path: str | None='/home/gotcrab/PycharmProjects/di_bot/.env') -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot = TgBot(token=env('BOT_TOKEN')))

if __name__ == '__main__':
    print(load_config())
