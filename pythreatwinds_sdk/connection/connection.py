class WebClientService():
    def __init__(self):
        self.tw_endpoint = ""
        self.tw_key = ""
        self.tw_secret = ""
        self.tw_authorization = ""
        self.cursor = None

    def add_url(self, url): 
        self.tw_endpoint = url

    def add_key(self, key): 
        self.tw_key = key
    
    def add_secret(self, secret): 
        self.tw_secret = secret
    
    def add_authorization(self, authorization): 
        self.tw_authorization = authorization