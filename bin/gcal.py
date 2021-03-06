from __future__ import print_function

import datetime
import os.path
from pickle import UNICODE
from dateutil import tz
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# If modifying these scopes, delete the file token_cal.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token_cal.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token_cal.json'):
        creds = Credentials.from_authorized_user_file('token_cal.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                sys.path[0]+'/credentials_cal.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token_cal.json', 'w') as token:
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
            if x[1] in 'Work - Reclaimed':
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
            start = datetime.datetime.strptime(event['start'].get('dateTime', event['start'].get('date')),"%Y-%m-%dT%H:%M:%S%z")
            # start = start.replace(tzinfo=from_zone) # not needed when calendar is already in local time
            end = datetime.datetime.strptime(event['end'].get('dateTime'),"%Y-%m-%dT%H:%M:%S%z")
            # end = end.replace(tzinfo=from_zone)
            eventString=event['summary']
            # remove task completion emojis from reclaim
            emoji_pattern = re.compile("["
                                        u"\u2705"
                                        u"\U0001F6E1"
                                        "]+",flags=re.UNICODE)
            eventString = emoji_pattern.sub(r'', eventString).strip()
            meeting = "- [ ] "+start.astimezone(to_zone).strftime("%H:%M")+" [["+eventString+"]]"
            print((meeting))
            print("- [ ] "+end.astimezone(to_zone).strftime("%H:%M")+ ' Break')
    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()