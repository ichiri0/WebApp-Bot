from .abstracts import WebClient
from bot.config.data_config import SERVER_URL


class WebAppsService(WebClient):

    async def get_all(self):
        url = SERVER_URL + "/web-apps/get-all"
        print(SERVER_URL)
        print(url)
        r = await self.fetch(url)
        return r
