from aiohttp import ClientSession
from fastapi import HTTPException
from datetime import datetime



class AssetService:
    async def get_price(symbol: str) -> dict:
        async with ClientSession() as client:
            try:
                response = await client.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT")
                data = await response.json()  
                price = data.get("price")
                if not price:
                     price  = 'Invalid symbol'
                return {'symbol': symbol, 'price':price, 'date': datetime.now()}
            except Exception as error:
                raise HTTPException(400, detail=str(error))


def get_assets_service() -> AssetService :
    return AssetService