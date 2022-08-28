#! usr/bin/python python3

from resquest import *



print("Fazendo a busca dos ep")

async def call_and_send_email():
    result = await  how_many_ep()
    return print(result)