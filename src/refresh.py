# CEO-bot daily job: refresh stars/last commit from public GitHub API (set GITHUB_TOKEN env for higher limits), then rerun gen.py
import json,os,urllib.request
p=os.path.join(os.path.dirname(__file__),"data/tools.json");d=json.load(open(p))
for t in d:
    r=urllib.request.Request(f"https://api.github.com/repos/{t['repo']}",headers={"User-Agent":"selfhostai"}|({"Authorization":"Bearer "+os.environ["GITHUB_TOKEN"]} if os.environ.get("GITHUB_TOKEN") else {}))
    try:j=json.load(urllib.request.urlopen(r,timeout=15));t["stars"]=j["stargazers_count"];t["last_commit"]=j["pushed_at"];t["archived"]=j["archived"]
    except Exception as e:print(t["repo"],e)
json.dump(d,open(p,"w"),indent=1);print("ok")
