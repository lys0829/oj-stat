import requests,json

def get_stat(userid,pid):
    sess = requests.Session()
    res = sess.post("https://toj.tfcis.org/oj/be/api",data={"reqtype":"AC","acct_id":userid})
    if res.status_code != 200:
        print("[TOJ][Error] can't get user %s's data."%userid)
        return 11
    ac_pro = json.loads(res.text)["ac"]
    #print(ac_pro)
    #print(pid)
    if int(pid) in ac_pro:
        #print("AC")
        return 1
    return 10