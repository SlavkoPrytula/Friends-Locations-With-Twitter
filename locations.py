import tweepy

def get_locations(user_name):
	"""
	(str)->(dict)
	Gets all friends of a user using Twitter API keys.
	And returns dictionary with names as keys and locations as value.
	"""
    auth = tweepy.auth.OAuthHandler("473GeY7AOJEYhjb3V3bQJRVXd", "OgRJWHJjd66o6uGA65Vx7N0ebSbe4axMKNsC36j0iwg64H9vV3")
    auth.set_access_token("851332427343593472-Nql8TgigLr6LH0BSJVYW85SSTE3ATlu", "WnY2tUnh7u1HhkLhe18OATMzUlJaZtYpiLXg91ayiRORr")
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
