from app.user.model.blacklist_model import BlackList


def add_token_to_blacklist(token):
    blacklist = BlackList(token)
    blacklist.add()
