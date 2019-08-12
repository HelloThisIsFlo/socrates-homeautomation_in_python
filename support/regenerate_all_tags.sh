#!/usr/bin/env python3

import os 
import subprocess
current_dir = os.path.dirname(os.path.realpath(__file__))

# subprocess.call(['git', 'log', '--graph', "--pretty='%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'", '--all'])
# subprocess.call(['git', 'log', '--graph', "--pretty='%s'", '--all'])
# subprocess.run(['git', 'tag', '-l'], capture_output=True)
# subprocess.run('git', 'tag', '-l', capture_output=False)
# subprocess.run('git', 'tag', '-l')

def all_tags():
    res = subprocess.run(["git", "tag", "-l"], capture_output=True, text=True)
    stdout_lines = [l for l in res.stdout.split('\n') if l != '']
    return stdout_lines

def remove_tag(tag):
    subprocess.run(['git', 'tag', '-d', tag], capture_output=False)

def all_step_commits():
    def build_tag(msg):
        step = msg.split(' -')[0]
        tag = step.lower().replace(' ', '-')
        return tag

    res = subprocess.run(['git', 'log', "--pretty=%h|%s"], capture_output=True, text=True)
    commit_lines = [l for l in res.stdout.split('\n') if l != '']
    commits = []
    for commit_line in commit_lines:
        print(commit_line)
        splitted_commit_line = commit_line.split('|')

        msg = splitted_commit_line[1]
        tag = build_tag(msg)
        hashstr = splitted_commit_line[0]
        if msg.startswith('Step'):
            commits.append({'msg': msg, 'hashstr': hashstr, 'tag': tag})

    # commits = [{'msg': line[1], 'hashstr': line[0]} for line =  in commit_lines]

    return commits
    # return stdout_lines
    # return [{'msg': '', 'hashstr': ''}]

def checkout(commit_hashstr):
    subprocess.run(['git', 'checkout', commit_hashstr])

def do_tag(tag_name):
    subprocess.run(['git', 'tag', tag_name])




# print(all_tags())
for tag in all_tags():
    remove_tag(tag)

for commit in all_step_commits():
    print(commit['hashstr'])
    checkout(commit['hashstr'])
    do_tag(commit['tag'])

#     print(commit)

# process = subprocess.run(['ls','-lha'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
# output = process.stdout

# print(output.split('\n'))