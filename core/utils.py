async def get_access():
    with open("access.txt", "r") as access:
        token = access.read()
    return token


async def parse_uuid(uuid):
    id = str(uuid).split("(")
    id = id[2].split("'")

    return id[1]
