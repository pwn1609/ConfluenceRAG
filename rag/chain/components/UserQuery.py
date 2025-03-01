class UserQuery:
    def __init__(self, query):
        self.query = query
        self.is_search_query = self.determine_query_type()

    def get_query(self):
        return self.query

    def set_query(self, query):
        self.query = query

    def determine_query_type(self):
        # Simple heuristic to determine query type
        search_terms = ["find", "search", "lookup", "locate"]
        for term in search_terms:
            if term in self.query.lower():
                return True  # Search query
        return False  # Question and answer query