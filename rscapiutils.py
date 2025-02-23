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
	api = grab_api('http://localhost/api/v1', api_key='aHNlro89.LcAkQRsRRtVg2Zsj2o02nB59xfHY4ige')
	lapi = rscapi.TrackerLinksApi(api)
	
	res = await lapi.tracker_links_list(discord_id=int('352600418062303244'))
	mapi = rscapi.MembersApi(api)
	update = rscapi.models.update_member_rsc_name.UpdateMemberRSCName(name="ha ha boo.", admin_override=True)
	res = await mapi.members_name_change(id=int('352600418062303244'), data=update)
	print(res)	


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

loop.run_until_complete(do_things())
