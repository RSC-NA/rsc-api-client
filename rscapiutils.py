import rscapi


def get_config(host):
	config = rscapi.Configuration(host, 
				      api_key={'api_key': 'EM59MHbM.Cpdg0DA8mwqLFly4SQ43HnbF8Z97p24F'},
				      api_key_prefix={'api_key': 'Api-Key'})

	return config

def get_api(config):
	return rscapi.ApiClient(config)


def grab_api(host):
	config = get_config(host)
	api = get_api(config)

	return api
