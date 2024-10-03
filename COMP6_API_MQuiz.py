import os
from webexteamssdk import WebexTeamsAPI
import requests
import json

#API Token
access_token = "NGExYjM5OTktMWM5Ny00YjFiLThkMDYtZDIxMjY1ZjE2ODA5YzVkNTQ2NjItM2Jl_P0A1_60c4241b-f916-4111-96c4-b4c6eecaa22e"
api = WebexTeamsAPI(access_token = "NGExYjM5OTktMWM5Ny00YjFiLThkMDYtZDIxMjY1ZjE2ODA5YzVkNTQ2NjItM2Jl_P0A1_60c4241b-f916-4111-96c4-b4c6eecaa22e")

#Create a Room and Add People
#room = api.rooms.create(title='Quiz Room Wagan')
#participant_email = 'allandavemarcoso@baliuagu.edu.ph'
#api.memberships.create(roomId=room.id, personEmail=participant_email)

#print(f'Room created: {room.title}')
#print(f'Participant added: {participant_email}')

#Create a Meeting
#url = "https://webexapis.com/v1/meetings"

#headers = {
#"Authorization": f"Bearer {access_token}",
#"Content-Type": "application/json"
#}

#meeting_data = {
#"title": "Quiz Meeting Wagan",
#start": "2024-10-03T15:00:00+00:00",
#"end": "2024-10-03T16:30:00+00:00"
#}

#response = requests.post(url, headers=headers, json=meeting_data)
#if response.status_code == 200:
#    print("Meeting created successfully!")
#    meeting_id = response.json()["id"]
#    print(f"Meeting ID: {meeting_id}")
#else:
#    print("Failed to create meeting.")

#Send a message to a room
#message = api.messages.create(roomId="Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZWFjZDU2NjAtODE1YS0xMWVmLTkyYzctN2Q1ZmI0NzE1NWEy", text='Como esta?')
#print(f'Message sent: {message.text}')

#List Messages
#messages = api.messages.list(roomId="Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZWFjZDU2NjAtODE1YS0xMWVmLTkyYzctN2Q1ZmI0NzE1NWEy")

#for message in messages:
#   print(f'Message: {message.text}')

#Delete a message
#api.messages.delete(messageId="Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL01FU1NBR0UvYzNlNGJmMTAtODE1Yi0xMWVmLTljODctYWI3ZDMyNDgwOGVh")
#print(f'Message deleted: {message.text}')