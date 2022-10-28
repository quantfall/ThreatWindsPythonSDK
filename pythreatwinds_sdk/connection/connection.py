class Connection:
    """
    Template for make a connection object
    """
    def __init__(self):
        self.endpoint = None

    def add_connection(self,url):
        self.endpoint = url