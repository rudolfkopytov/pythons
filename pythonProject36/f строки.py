europe = {'spain': {'capital':'madrid'},
           'france': {'capital':'paris'},
           'germany': {'capital':'berlin'},
           'norway': {'capital':'oslo'}}
for country, info in europe.items():
    print(info)
    print(f'The capital of {country.title()} is {list(info.values())[0].title()}')