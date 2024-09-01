import httpx
from loguru import logger


class WebClient:
    async def fetch(self, url: str, **values) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, **values)
                response.raise_for_status()  # Raises an exception for 4xx or 5xx responses
                return response.json()
            except httpx.HTTPStatusError as e:
                logger.error(
                    f"HTTP error occurred while sending GET request: {e}")
                error_detail = None
                try:
                    error_detail = e.response.json()["detail"]
                except ValueError:
                    # Если ответ не JSON-совместимый, отдаём текст
                    error_detail = e.response.text.strip()
                return httpx.Response(
                    e.response.status_code,
                    json={"detail": error_detail}
                )
            except httpx.RequestError as e:
                logger.error(f"Error occurred while sending GET request: {e}")
                return None

    async def post_json(self, url: str, json: dict, **values) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=json, **values)
                response.raise_for_status()  # 4xx или 5xx
                return response.json()
            except httpx.HTTPStatusError as e:
                logger.error(
                    f"HTTP error occurred while sending GET request: {e}")
                error_detail = None
                try:
                    error_detail = e.response.json()["detail"]
                except ValueError:
                    # Если ответ не JSON-совместимый, отдаём текст
                    error_detail = e.response.text.strip()
                return httpx.Response(
                    e.response.status_code,
                    detail=error_detail
                )
            except httpx.RequestError as e:
                logger.error(f"Error occurred while sending GET request: {e}")
                return None

    async def delete_json(self, url: str, json: dict, **values) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=json, **values)
                response.raise_for_status()  # 4xx или 5xx
                return response.json()
            except httpx.HTTPStatusError as e:
                logger.error(
                    f"HTTP error occurred while sending GET request: {e}")
                error_detail = None
                try:
                    error_detail = e.response.json()["detail"]
                except ValueError:
                    # Если ответ не JSON-совместимый, отдаём текст
                    error_detail = e.response.text.strip()
                return httpx.Response(
                    e.response.status_code,
                    detail=error_detail
                )
            except httpx.RequestError as e:
                logger.error(f"Error occurred while sending GET request: {e}")
                return None

    async def post_data(self, url: str, **values) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, **values)
                response.raise_for_status()  # 4xx или 5xx
                return response.json()
            except httpx.HTTPStatusError as e:
                logger.error(
                    f"HTTP error occurred while sending GET request: {e}")
                error_detail = None
                try:
                    error_detail = e.response.json()["detail"]
                except ValueError:
                    # Если ответ не JSON-совместимый, отдаём текст
                    error_detail = e.response.text.strip()
                return httpx.Response(
                    e.response.status_code,
                    detail=error_detail
                )
            except httpx.RequestError as e:
                logger.error(f"Error occurred while sending GET request: {e}")
                return None
