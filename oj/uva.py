import requests
import json
import time

def get_stat(userid,pid):
    sess = requests.Session()
    res = sess.get("https://uhunt.onlinejudge.org/api/p/num/"+str(pid))
    if res.status_code != 200:
        print("[Uva][Error] can't change pnum to pid.")
        return 11
    pid = json.loads(res.text)["pid"]
    
    res = sess.get("https://uhunt.onlinejudge.org/api/uname2uid/"+userid)
    if res.status_code != 200:
        print("[Uva][Error] can't change username to uid.")
        return 11
    userid = int(res.text)
    
    res = sess.get("https://uhunt.onlinejudge.org/api/subs-pids/%d/%d/0"%(userid,pid))
    if res.status_code != 200:
        print("[Uva][Error] can't get user %s on problem uva%d's submission list"%(userid,pid))
        return 11
    
    sublist = json.loads(res.text)[str(userid)]["subs"]
    verdict = 0
    for sub in sublist:
        if sub[1] != pid:
            continue
        verdict = max(verdict,sub[2])
    '''
    20 : In queue
30 : Compile error
35 : Restricted function
40 : Runtime error
45 : Output limit
50 : Time limit
60 : Memory limit
70 : Wrong answer
80 : PresentationE
90 : Accepted
    '''
    verdictmap = {90:1,80:2,70:3,60:6,50:5,45:4,40:7,35:12,30:8,20:12}
    if verdict == 0:
        return 10
    if verdict<20:
        return 9
    return verdictmap[verdict]