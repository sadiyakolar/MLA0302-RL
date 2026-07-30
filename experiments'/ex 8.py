road = ["Start","Signal","Turn","Goal"]

for place in road:

    if place=="Signal":
        print(place,"-> Stop and Wait")

    elif place=="Turn":
        print(place,"-> Turn Left")

    elif place=="Goal":
        print(place,"-> Destination Reached")

    else:
        print(place,"-> Move Forward")
