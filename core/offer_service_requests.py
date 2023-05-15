import requests

from models.product import ProductSchema
from .config import SERVICE_URL, SERVICE_REFRESH


async def send_get_request_offers(product_id, access):
    r = requests.get(SERVICE_URL + "/products/{product_id}/offers".format(product_id=product_id),
                     headers={'Accept': 'application/json',
                              'Bearer': access})

    return r.json()#f"Status Code: {r.status_code}, Content: {r.json()}"  r.json()


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
                      json={"id": product.UUID,
                            "name": product.name,
                            "description": product.description})

    return f"Status Code: {r.status_code}, Content: {r.json()}"


