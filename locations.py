import tweepy

def get_locations(user_name):
	"""
	(str)->(dict)
	Gets all friends of a user using Twitter API keys.
	And returns dictionary with names as keys and locations as value.
	"""
    auth = tweepy.auth.OAuthHandler("API key", "API secret key")
    auth.set_access_token("Access token", "Access token secret")
    api = tweepy.API(auth)
    users = tweepy.Cursor(api.friends, screen_name=user_name).items()

    users_data = {}
    try:
        for user in users:
            if user.location is not None and user.location != "":
                users_data.update({user.screen_name: user.location})
    except:
        pass

    return users_data
