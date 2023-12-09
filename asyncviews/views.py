import asyncio
from django.http import HttpResponse
import httpx
from time import sleep

async def http_call_async():
    for num in range(1, 5):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        response = await client.get('https://httpbin.org/')
        print(response)

def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    response = httpx.get('https://httpbin.org/')
    print(response)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-blocking HTTP request')

def sync_view(request):
    http_call_sync()
    return HttpResponse('Blocking HTTP request')