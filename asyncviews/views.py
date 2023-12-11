import asyncio
import httpx
from django.http import HttpResponse

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        response = await client.get('https://httpbin.org/')
        print(response)

async def async_view(request):
    await http_call_async()
    return HttpResponse('Non-blocking response')