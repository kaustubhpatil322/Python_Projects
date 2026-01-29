import requests
from datetime import datetime

USERNAME = "kaustubh322"
TOKEN = "jfije93uw3ntn3h3"
GRAPH_ID="graph1"
pixela_endpoint ="https://pixe.la/v1/users"

body={
    "token":"jfije93uw3ntn3h3",
    "username":"kaustubh322",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

response = (requests.post(url=pixela_endpoint , json=body))
# response.raise_for_status()
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_header ={
    "X-USER-TOKEN":TOKEN
}
graph_body={
    "id":"graph1",
    "name":"study_graph",
    "unit":"minutes",
    "type":"int",
    "color":"sora",
}

graph_response = requests.post(url=graph_endpoint , json=graph_body , headers=graph_header)
print(graph_response.text)

#------------------------------POST a PIXEL----------------------------------------

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
post_pixel_headers={
    "X-USER-TOKEN" : TOKEN,
}
post_date = datetime(2026, 1 , 28)
print(post_date.strftime("%Y%m%d"))


# date = date.today()
# month = str(date.month)
# if len(month)<2:  month = "0"+month
#
# year = str(date.year)
# day=str(date.day)
# post_date = year+month+day
post_pixel_body={
    "date":post_date.strftime("%Y%m%d"),
    "quantity":"50",
}

post_pixel_response = requests.post(url=post_pixel_endpoint , json=post_pixel_body , headers=post_pixel_headers)
print(post_pixel_response.text)

#------------------------------Update a Pixel-----------------------------------------------------------
put_date = datetime(2026 , 1 , 24)

put_endpoint = f"{post_pixel_endpoint}/{put_date.strftime('%Y%m%d')}"
put_header={
    "X-USER-TOKEN":TOKEN,
}
put_body = {
    "quantity":"150",
}
#put_response =requests.put(url=put_endpoint, json = put_body , headers=put_header)
#print(put_response.text)

#------------------------------------Delete a Pixel ------------------------------------------------------
delete_date=datetime(2026 , 1 , 27)
delete_endpoint = f"{post_pixel_endpoint}/{delete_date.strftime('%Y%m%d')}"
delete_header = {
    "X-USER-TOKEN":TOKEN,
}
delete_response = requests.delete(url=delete_endpoint , headers=delete_header)
print(delete_response.text)


