from src.applications.base.query.BoruvkaBaseQuery import BoruvkaBaseQuery
from src.applications.user.storage.BoruvkaUserStorage import BoruvkaUserStorage


class BoruvkaUserQuery(BoruvkaBaseQuery):
    def create_user(self, username, password):
        user = BoruvkaUserStorage()
        user.username = username
        user.password = password
        self._dao.save(user)
        return user

    def get_user(self, **kwargs):
        conditions = []
        values = []
        for key, value in kwargs.items():
            condition = "{0:s} = %s".format(key)
            conditions.append(condition)
            values.append(value)
        where_clause = " AND ".join(conditions)
        users = self._dao.list_where(
            where_clause=where_clause,
            clazz=BoruvkaUserStorage,
            arg_list=values
        )

        # TODO check if unique results
        if len(users) > 0:
            return users[0]
        return None
