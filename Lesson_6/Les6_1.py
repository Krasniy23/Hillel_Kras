coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
print((i, l for i, l in dict(zip(coin, code))))