import requests
from bs4 import BeautifulSoup

def get_stat(userid,pid):
    sess = requests.Session()
    
    res = sess.get("https://tioj.ck.tp.edu.tw/users/"+userid, allow_redirects=False)
    
    if res.status_code != 200:
        print("[TOJ][Error] can't get user %s's data."%userid)
        return 11
    
    user_profile = res.text
    bs = BeautifulSoup(user_profile, 'html.parser')
    
    ac_pro = bs.find_all("a",{"class":"text-success"})
    #print(ac_pro)
    ac_pro = [int(pro.text) for pro in ac_pro]
    
    if int(pid) in ac_pro:
        return 1
    return 10
    