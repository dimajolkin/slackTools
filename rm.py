import requests
import json
import calendar
from datetime import datetime, timedelta

_token = "xoxp-***"
_domain = "***-team"
def getTokken:
   url = "https://slack.com/oauth/authorize"
   
   pass
if __name__ == '__main__':
    while 1:
        try:
           files_list_url = 'https://slack.com/api/files.list'
           date = str(calendar.timegm((datetime.now() + timedelta(-15))
               .utctimetuple()))
           data = {"token": _token, "ts_to": date}
           response = requests.post(files_list_url, data = data)
           if len(response.json()["files"]) == 0:
               break
           count_delete = 0
           print "Load new files:"
           for f in response.json()["files"]:
               count_delete+=1
               print count_delete.__str__() + ") Deleting file " + f["name"] + "..."
               timestamp = str(calendar.timegm(datetime.now().utctimetuple()))
               delete_url = "https://" + _domain + ".slack.com/api/files.delete?t=" + timestamp
               answer = requests.post(delete_url, data = {
                   "token": _token, 
                   "file": f["id"], 
                   "set_active": "true", 
                   "_attempts": "1"})
               print answer.json() 
        except Exception:
           if (count_delete == 0):
                exit()
           print "Reconnect"   
    print "DONE!"
