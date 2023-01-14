europe = {'spain': {'capital':'madrid'},
           'france': {'capital':'paris'},
           'germany': {'capital':'berlin'},
           'norway': {'capital':'oslo'}}
for country, info in europe.items():
    print(f'The capital of {country.title()} is {info["capital"].title()}')