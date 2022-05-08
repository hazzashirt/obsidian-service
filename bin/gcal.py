from __future__ import print_function

import datetime
import os.path
from dateutil import tz
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    print(sys.path[0])
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                sys.path[0]+'/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow()  # 'Z' indicates UTC time
        # List Calendars
        calendar_list = service.calendarList().list().execute()
        calendars = []
        work_calendar=""
        # Filter for calendar
        for x in calendar_list['items']:
            # print(x['summary'],x['id'])
            calendars.append([x['id'],x['summary']])
        for x in calendars:
            if x[1] in 'Calendars':
                work_calendar = x[0]
                # print('ID: '+work_calendar)
        
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()

        # Get Calendar Events for today
        now_local = datetime.datetime.now()
        today_start = now - datetime.timedelta(hours=now_local.hour,minutes=now_local.minute,seconds=now_local.second)
        today_end = today_start + datetime.timedelta(hours=24)
        today_start_iso = today_start.isoformat()+'Z'
        today_end_iso = today_end.isoformat()+'Z'
        events_result = service.events().list(calendarId=work_calendar,timeMin=today_start_iso,
                                                timeMax=today_end_iso, singleEvents=True,
                                                orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return
        # Prints the start and name of events
        for event in events:
            start = datetime.datetime.strptime(event['start'].get('dateTime', event['start'].get('date')),"%Y-%m-%dT%H:%M:%SZ")
            start = start.replace(tzinfo=from_zone)
            end = datetime.datetime.strptime(event['end'].get('dateTime'),"%Y-%m-%dT%H:%M:%SZ")
            end = end.replace(tzinfo=from_zone)
            print("- [ ] ",start.astimezone(to_zone).strftime("%H:%M"), event['summary'])
            print("- [ ] ",end.astimezone(to_zone).strftime("%H:%M"), 'BREAK')
        # calendar = service.calendarList().get(calendar_list[0])
        # print(calendar)
        # print('Getting the upcoming 10 events')
        # events_result = service.events().list(calendarId='calendar', timeMin=now,
        #                                       maxResults=10, singleEvents=True,
        #                                       orderBy='startTime').execute()
        # events = events_result.get('items', [])

        # if not events:
        #     print('No upcoming events found.')
        #     return

        # # Prints the start and name of the next 10 events
        # for event in events:
        #     start = event['start'].get('dateTime', event['start'].get('date'))
        #     print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()