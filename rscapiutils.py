import rscapi


def get_config(host):
	config = rscapi.Configuration(host, 
				      api_key={'Api-Key': 'a2ooxauj.B8gVfrllKA1POuZaUZmOSHSUhrGeLyp5'},
				      api_key_prefix={'Api-Key': 'Api-Key'})

	return config

def get_api(config):
	return rscapi.ApiClient(config)


def grab_api(host):
	config = get_config(host)
	api = get_api(config)

	return api
