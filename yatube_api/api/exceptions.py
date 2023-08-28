class SelfFollowingError(Exception):
    """You can't follow yourself."""
    pass


class UndefinedUsernameToFollowError(Exception):
    """No user with that username."""
    pass
