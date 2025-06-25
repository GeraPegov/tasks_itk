import asyncio
import json

import aiohttp


def get_urls(file_out: str):
    try:
        with open(file_out) as info:
            return json.load(info)
    except FileNotFoundError:
        print(f"Файл {file_out} не найден")
        return None
    except json.JSONDecodeError:
        print(f"Файл {file_out} содержит невалидный JSON")
        return None
    except Exception as e:
        print(f"Низвестная ошибка: {e}")
        return None


async def get_data(url: str, semaphore: asyncio.Semaphore):
    async with semaphore:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        if "application/json" not in response.headers["content-type"]:
                            return None
                        return {url: await response.text()}
                    return None
        except asyncio.TimeoutError:
            print(f"Таймаут при запросе к {url}")
        except aiohttp.ClientError as e:
            print(f"Ошибка соединения с {url}: {str(e)}")
        except Exception as e:
            print(f"Неизвестная ошибка {e}")


def record(data: dict):
    try:
        with open("response.jsonl", "w") as file:
            file.write(json.dumps(data) + "\n")
    except OSError as e:
        print(f"Ошибка записи в файл: {str(e)}")
    except Exception as e:
        print(f"Неизвестная ошибка : {str(e)}")


async def fetch_all(file: str, max_concurrent: int = 5):
    try:
        semaphore = asyncio.Semaphore(max_concurrent)
        urls = get_urls(file)
        if urls:
            get_data_url = [get_data(url, semaphore) for url in urls]
            data_for_record = await asyncio.gather(*get_data_url)
            for data in data_for_record:
                if data:
                    record(data)
        return None
    except Exception as e:
        print(f"Неизвестная ошибка в {str(e)}")


if __name__ == "__main__":
    file = "url.json"
    asyncio.run(fetch_all(file))
