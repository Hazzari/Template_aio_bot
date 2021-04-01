from environs import Env

env = Env()
env.read_env()

ip = env.str('ip')
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
DATABASE = env.str("DATABASE")
PG_USER = env.str("PG_USER")
PG_PASSWORD = env.str("PG_PASSWORD")

POSTGRES_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{ip}/{DATABASE}"
