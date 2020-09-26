import requests, pprint
import pandas as pd

api_key = "240b6d037974969a3b04c691c905eeb8"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNDBiNmQwMzc5NzQ5NjlhM2IwNGM2OTFjOTA1ZWViOCIsInN1YiI6IjVmNmQ2ZDgzZTI2N2RlMDAzNDJmMmEwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5xl6Kd9pEmDpnxDAnzy5w1HhNvmNcplQi_RKdM52TYU"

#v3 get movie using movie_id
# movie_id = 500
api_version = 3
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
# endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"

#r = requests.get(endpoint)
#print(r.status_code, r.text)






#v3 search movie
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query=Endgame"

r = requests.get(endpoint)
#pprint.pprint(r.json())

if r.status_code in range(200, 299):
	data = r.json()
	results = data['results']
	if len(results) > 0:
		#print(results[0].keys())
		movie_ids = set()
		for result in results:
			_id = result['id']
			print(result['title'], _id)
			movie_ids.add(_id)
		#print(list(movie_ids))


output = 'movies.csv'
movie_data = []
for movie_id in movie_ids:
	api_base_url = f"https://api.themoviedb.org/{api_version}"
	endpoint_path = f"/movie/{movie_id}"
	endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"

	r = requests.get(endpoint)
	if r.status_code in range(200, 299):
		data = r.json()
		movie_data.append(data)
	#print(r.json())

#write to csv
df = pd.DataFrame(movie_data)
df.to_csv(output, index=False)







# v4 get movie using movie_id
# movie_id = 501
# api_version = 4
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
# endpoint = f"{api_base_url}{endpoint_path}"
# headers = {
# 	'Authorization': f'Bearer {api_key_v4}',
# 	'Content-Type': 'application/json;charset=utf-8'
# }

# r = requests.get(endpoint, headers=headers)
# print(r.status_code, r.text)