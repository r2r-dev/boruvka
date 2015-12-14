from src.applications.base.query.BoruvkaBaseQuery import BoruvkaBaseQuery
from src.applications.auth.storage.BoruvkaTokenStorage import BoruvkaTokenStorage


class BoruvkaAuthQuery(BoruvkaBaseQuery):
    def create_token(self, value, date):
        token = BoruvkaTokenStorage()
        token.value = value
        token.expirationDate = date
        self._dao.save(token)
        return token

    def get_token(self, **kwargs):
        conditions = []
        values = []
        for key, value in kwargs.items():
            condition = "{0:s} = %s".format(key)
            conditions.append(condition)
            values.append(value)
        where_clause = " AND ".join(conditions)
        tokens = self._dao.list_where(
            where_clause=where_clause,
            clazz=BoruvkaTokenStorage,
            arg_list=values
        )
        
        # TODO check if unique results
        if len(tokens) > 0:
            return tokens[0]
        return None
