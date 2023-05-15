import asyncio

from core.offer_service_requests import send_post_request_access, send_get_request_offers
from core.utils import get_access, parse_uuid
from models.product import OfferSchema
from repository.offer import create_all, delete_all


async def access_service():
    while True:
        res = await send_post_request_access()
        print(res)
        content = res.split(' {')
        content1 = content[1].split(': ')
        content_formatted = content1[1].replace("'", "").replace('}', '')
        if content_formatted != 'Cannot generate access token because another is valid':
            with open("access.txt", "w") as access:
                access.write(content_formatted)
        print(content_formatted)
        await asyncio.sleep(300)


async def offers_service(product_ids, db):
    token = await get_access()
    while True:
        offers = []
        for product_id in product_ids:
            p_id = await parse_uuid(product_id)
            res = await send_get_request_offers(access=token, product_id=p_id)
            for offer in res:
                offer['product_id'] = p_id
                offers.append(OfferSchema.parse_obj(offer))
                await delete_all(db=db, product_id=p_id)
                await create_all(db=db, product_id=p_id, offer_list=offers)

        await asyncio.sleep(60)
