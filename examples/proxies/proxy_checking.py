import asyncio

from OmeglePyRewrite.ProxyChecking import ProxyChecking

checker = ProxyChecking('proxies.txt', 'working.txt')
loop = asyncio.get_event_loop()

checker.check_proxies()

loop.run_forever()
