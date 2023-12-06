import rscapi


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
