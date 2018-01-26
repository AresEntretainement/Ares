import asyncio
from datetime import datetime
SODA_LOCK = asyncio.Lock()
BURGER_SEM = asyncio.Semaphore(3)
FRITES_COUNTER = 0
FRITES_LOCK = asyncio.Lock()
async def get_soda(client):
	async with SODA_LOCK:
		print("    > Remplissage du soda pour {}".format(client))
		await asyncio.sleep(1)
		print("    < Le soda de {} est pret".format(client))

async def get_frites(client):
	global FRITES_COUNTER
	async with FRITES_LOCK:
		print("     > Recuperation des frites pour {}".format(client))
		if FRITES_COUNTER == 0:
			print("    > Demarrage de la cuisson des frites pour {}".format(client))
			await asyncio.sleep(4)
			FRITES_COUNTER = 5
			print("  ** Les frites sont cuites **  ")
		FRITES_COUNTER -= 1
		print("    < Les Frites de {} sont pretes".format(client))
async def get_burger(client):
	print("    > Commange du burger en cuisine pour {}".format(client))
	async with BURGER_SEM:
		await asyncio.sleep(3)
		print("    < Le burger de {} est pret".format(client))
async def serve(client):
	print("=> Commande passe par {}".format(client))
	start_time = datetime.now()
	await asyncio.wait(
		[
			get_soda(client),
			get_frites(client),
			get_burger(client)
		]
	)
	total = datetime.now() - start_time
	print("<= {} servi en {}".format(client, datetime.now() - start_time))
	return total
async def perf_test(nb_requests, period, timeout):
	tasks = []
	for idx in range(1, nb_requests + 1):
		client_name = 'client_{}'.format(idx)
		tsk = asyncio.ensure_future(serve(client_name))
		tasks.append(tsk)
		await asyncio.sleep(period)
	finished, _ = await asyncio.wait(tasks)
	success = set()
	for tsk in finished:
		if tsk.result().seconds < timeout:
			success.add(tsk)

	print("{}/{} clients satisfaits".format(len(success),len(finished)))
