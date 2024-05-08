import requests

url = "https://realtime-crypto-prices.p.rapidapi.com/get_rates"

querystring = {"symbol":"BTC"}

headers = {
	"X-RapidAPI-Key": "fa2ae83c39msh4ccfd5eeff89d1ep18ae3cjsnaed129db5729",
	"X-RapidAPI-Host": "realtime-crypto-prices.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())