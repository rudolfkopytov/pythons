d={
  "20": [
    {
      "name": "RUB",
      "cost": 0.1354,
      "amount": 1000
    },
    {
      "name": "BTC",
      "cost": 36008,
      "amount": 0.003
    }
  ],
  "21": [
    {
      "name": "RUB",
      "cost": 0.1354,
      "amount": 2000
    },
    {
      "name": "BTC",
      "cost": 36008,
      "amount": 0.006
    }
  ]
}


import json #- работает только со строками


print(json.dumps(d, indent=2))