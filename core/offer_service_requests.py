import requests

from models.product import ProductSchema
from .config import SERVICE_URL, SERVICE_REFRESH


async def send_get_request_offers(product_id, access):
    r = requests.get(SERVICE_URL + "/products/{}/offers".format(product_id),
                     headers={'Accept': 'application/json',
                              'Bearer': access})

    return f"Status Code: {r.status_code}, Content: {r.json()}"


async def send_post_request_access():
    r = requests.post(SERVICE_URL + "/auth",
                      headers={'Accept': 'application/json',
                               'Bearer': SERVICE_REFRESH}
                      )

    return f"Status Code: {r.status_code}, Content: {r.json()}"


async def send_post_request_register_product(product: ProductSchema, access):
    r = requests.post(SERVICE_URL + "/products/register",
                      headers={'Accept': 'application/json',
                               'Bearer': access},
                      json={**product.dict()})

    return f"Status Code: {r.status_code}, Content: {r.json()}"
