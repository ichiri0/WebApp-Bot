from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
WEBAPP_URL = env.str("WEBAPP_URL")
SERVER_URL = env.str("SERVER_URL")
ADMINS = env.list("ADMINS")

print(WEBAPP_URL)