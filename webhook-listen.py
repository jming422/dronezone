import push
from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/github', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        my_info = request.json
        action = my_info['action']
        merged = my_info['pull_request']['merged']
        commits = my_info['pull_request']['commits']

        if action == 'closed' and merged:
            push.celebrate(magnitude=commits)

        print('action:', action)
        print('merged property?:', merged)
        print('commits:', commits)
        return 'Ok'
    else:
        print('Didn\'t get Content-Type json.')
        print(request.headers['Content-Type'])
        print(request.get_data())
        return 'Eat some pi'

if __name__ == '__main__':
    app.run(debug=True)
