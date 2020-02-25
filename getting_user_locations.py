import folium
from geopy.geocoders import Nominatim
import locations

geolocator = Nominatim(user_agent='myapplication')


def find_locations(user_input):

    """
    (int)(int, int) -> (f_map.html)

    This function returns generated map that reassembles
    all users-friens of an account.

    Also puts markers in those positions.

    """

    latitude_start = 49.8326046
    longatude_start = 23.8721529
    start_point = (latitude_start, longatude_start)
    m = folium.Map(location=[latitude_start, longatude_start], zoom_start=4.2, tiles='OpenStreetMap')

    marker = folium.Marker([latitude_start, longatude_start],
                           popup="<b><strong>{}</strong></b>".format("My_location"),
                           icon=folium.Icon(color="red")).add_to(m)

    # Create layer:
    friends_group = folium.FeatureGroup(name="Friends").add_to(m)

    friends_locations = locations.get_locations(user_input)

    for friend in friends_locations:
        print("Getting location for: {}".format(friend))
        try:
            location = geolocator.geocode(friends_locations[friend])
            latitude = location.latitude
            longatude = location.longitude

            user_name = friend

            marker = folium.Marker([latitude, longatude],
                                   popup="<b><strong>{}</strong></b>".format("Name: \n" + user_name),
                                   icon=folium.Icon(color="orange", icon="film outline")).add_to(m)
            friends_group.add_child(marker)
            # m.save('friends_location_files/templates/f_map.html')
            h_m = m.get_root().render()
        except:
            pass


    folium.LayerControl().add_to(m)
    # m.save('friends_location_files/templates/f_map.html')
    return h_m
