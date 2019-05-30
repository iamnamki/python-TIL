import sys, os
import datetime



def gitcmd(cmd):
    print("gitcmd : ", cmd)
    os.system(cmd)

sa = sys.argv # 0 실행파일, 1: commit 메시지

now = datetime.datetime.now()
default_msg = "{} Today I learned".format(now.strftime('%Y-%m-%d'))
commit_msg = default_msg
has_msg = len(sa) >= 2


if has_msg :
    commit_msg = sa[1]

else :
    input_msg = input("Default Message?? (Yes : Enter or input message) > ")
    if input_msg != "":
        commit_msg = input_msg

print("commit ... ", commit_msg)

gitcmd("git add --all")
gitcmd('git commit -am "{}"'.format(commit_msg))
gitcmd("git push")