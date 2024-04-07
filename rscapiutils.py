import rscapi
import asyncio

def get_config(host, api_key):
	config = rscapi.Configuration(host, 
				      api_key={'Api-Key': api_key},
				      api_key_prefix={'Api-Key': 'Api-Key'})

	return config

def get_api(config):
	return rscapi.ApiClient(config)


def grab_api(host, api_key):
	config = get_config(host, api_key)
	api = get_api(config)

	return api


async def do_things():
	api = grab_api('http://localhost:3000/api/v1', api_key='XEb03FNA.Sqff9r4Ktg809gQ0WsJK3aeekZOwV5BG')
	transapi = rscapi.TransactionsApi(api)
	res = await transapi.transactions_history_list(player=181204305993400321, league=1, season_number=None)
	print(res)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

loop.run_until_complete(do_things())

