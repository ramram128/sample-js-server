import requests

boundary = '----boundary'

json_data = '''{
	"ipAddress":	"192.168.29.80",
	"portNo":	80,
	"protocol":	"HTTP",
	"macAddress":	"e8:a0:ed:9e:25:e2",
	"channelID":	1,
	"dateTime":	"2024-09-15T12:53:04+05:30",
	"activePostCount":	1,
	"isDataRetransmission":	false,
	"eventState":	"active",
	"channelName":	"Altra Waves 01",
	"eventType":	"alarmResult",
	"eventDescription":	"alarmResult",
	"alarmResult":	[{
			"modelData":	"UmxJMU1EQXdNRG9CQUFBQUFBQUFBQnVBOWd4UzJ1d243RGUrVW9CM3J0QkpMbVVuZ0FNSE9xY0gwaFRWRGc1TkxodUFCUzdHV1FDYS9mMzJkL0VnNzBabEJUejB1bmtQT3RBbTJYLzJEdklGZTY1MEJmSFVRVVRaZnhRbUtRQi9NWGUxK2NqTElQVEpHMFRzeE5LZDVvRHNxMDNlTjVZZDl0bnRRdjVaSjdDODQrZ0MvVzlsa1FBQ0J5bmVHcjg4RWRkYTd6QUFRazQ2aXIveUx0ZGg0T09BRko5MGhhN3Y1U1k2Qi8wYmFIOEhBRWI3ejlmZVpRekxId0JKR0tjZnorZ1l5TzhSdWlrYlRpQ3BMUFlBVG9DVkVYVGdKOE16NFFvd2dQNHdJTkFVNzBFbnVQR3NLZXJsR0lLbjZCVFZCMExYQlFEZUJZRDNTeGhjSU1UcTNnbk5GamplYTN5L0lESEUrWVhnRTJZQUFBQUFBQUFBQUFBQUFBQUFBQUFB",
			"errorCode":	1,
			"errorMsg":	"ok",
			"targetAttrs":	{
				"deviceId":	"775b8000-750b-11b2-806f-e8a0ed9e25e2",
				"deviceChannel":	1,
				"deviceName":	"Altra Waves Camera 01",
				"faceTime":	"2024-09-15T12:53:04+05:30",
				"rect":	{
					"height":	0.122,
					"width":	0.056,
					"x":	0.468,
					"y":	0.000
				}
			},
			"faces":	[{
					"faceId":	104,
					"faceRect":	{
						"height":	0.054,
						"width":	0.028,
						"x":	0.482,
						"y":	0.036
					},
					"recommendFaceRect":	{
						"height":	0.437,
						"width":	0.513,
						"x":	0.236,
						"y":	0.295
					},
					"score":	{
						"value":	43
					},
					"modeldata":	"RlI1MDAwMDoBAAAAAAAAABuA9gxS2uwn7De+UoB3rtBJLmUngAMHOqcH0hTVDg5NLhuABS7GWQCa/f32d/Eg70ZlBTz0unkPOtAm2X/2DvIFe650BfHUQUTZfxQmKQB/MXe1+cjLIPTJG0TsxNKd5oDsq03eN5Yd9tntQv5ZJ7C84+gC/W9lkQACByneGr88Edda7zAAQk46ir/yLtdh4OOAFJ90ha7v5SY6B/0baH8HAEb7z9feZQzLHwBJGKcfz+gYyO8RuikbTiCpLPYAToCVEXTgJ8Mz4QowgP4wINAU70EnuPGsKerlGIKn6BTVB0LXBQDeBYD3SxhcIMTq3gnNFjjea3y/IDHE+YXgE2YAAAAAAAAAAAAAAAAAAAAA",
					"identify":	[{
							"relationId":	"",
							"maxsimilarity":	0.900,
							"candidate":	[{
									"blacklist_id":	"1",
									"customFaceLibID":	"",
									"human_data":	[{
											"face_id":	"104",
											"contentID":	"faceLibImage",
											"pId":	"2024091512531024900T2Xn4Xb51T0cr",
											"similarity":	0.9
										}],
									"human_id":	"2",
									"reserve_field":	{
										"name":	"Saravana Sampath",
										"gender":	"male",
										"bornTime":	"1994-08-15",
										"certificateType":	"officerID",
										"certificateNumber":	"AWS001"
									},
									"similarity":	0.900,
									"listType":	"blackList",
									"extendData":	[{
											"extendID":	1,
											"enable":	false,
											"name":	"Custom Field 1",
											"value":	""
										}, {
											"extendID":	2,
											"enable":	false,
											"name":	"Custom Field 2",
											"value":	""
										}, {
											"extendID":	3,
											"enable":	false,
											"name":	"Custom Field 3",
											"value":	""
										}],
									"FDLibName":	"employee",
									"FDLibThreshold":	60
								}]
						}],
					"contentID":	"faceImage",
					"pId":	"2024091512531021900dR2RarDkkxbc5",
					"stayDuration":	8000
				}]
		}],
	"GPS":	{
		"divisionEW":	"E",
		"longitude":	0,
		"divisionNS":	"N",
		"latitude":	0
	}
}'''

# Construct the multipart form-data manually 
body = (
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"alarmResult\"; filename=""\r\n"
    "Content-Type: application/json\r\n\r\n"
).encode() + json_data.encode() + b"\r\n"  # Append JSON data

body += (
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"faceImage\"; filename=\"image.jpg\"\r\n"
    "Content-Type: image/jpeg\r\n"
    "Content-ID: 2024091512531021900dR2RarDkkxbc5\r\n\r\n"
).encode()


with open('C:/Users/Happy/Music/hunter2/images.jpeg', 'rb') as image_file:
    image_data = image_file.read()


body += image_data
body += f"\r\n--{boundary}--\r\n".encode()


headers = {
    'Content-Type': f'multipart/form-data; boundary={boundary}'
}


response = requests.post('http://localhost:8080/receive_json', data=body, headers=headers)


print(f"Server responded with status code: {response.status_code}")
print(f"Response body: {response.text}")
