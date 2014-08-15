import requests
import json
import time
import random

TOKEN = 'CAACEdEose0cBAAYXkSTIjfut4jxi7YdWtiiQb6wN1POifDvgBpYB8GYMZA750yH2caN3E26h0lXRrVxdCwr5aBFGylnqJ6M0l0uSnH9ISXxZCmtVGUVyCd6aoldwG8PjkjhyFXv22P6EweRMKQ2c2IdZBfnqZBtXhmFsxCDB92B3m7vZCJQvvEUMANnxAEdKq7f2u6uPSY3GmhWnt129ZC'

def get_posts():
    query = ("SELECT post_id, actor_id, message FROM stream WHERE "
            "filter_key = 'others' AND source_id = me() AND "
            "created_time>" + str(int(AFTER)) + " AND created_time<"
             + str(int(BEFORE)) + " LIMIT 400");
    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

def commentall(wallposts):
    
        a= rawInput();

if __name__ == '__main__':
    AFTER = time.mktime(time.strptime('05/08/2014',"%d/%m/%Y"))
    BEFORE = time.mktime(time.strptime('06/08/2014',"%d/%m/%Y"))
    all_posts = get_posts();

    list = ["Thank you %s",
            "Thanks a lot %s",
            "Thanks %s"
            ];
    for wallpost in all_posts:
        r = requests.get('https://graph.facebook.com/%s' % wallpost['actor_id']);
        url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id'];
        user = json.loads(r.text);
        message = random.choice(LIMITst) %user['first_name'];
        payload = {'access_token': TOKEN, 'message': message};
        print message
        #s = requests.post(url, data=payload);
        print "Wall post %s done" % user['first_name'];
        raw_input()
