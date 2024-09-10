our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_routes = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", same_routes)

unique_routes = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_routes)

if same_routes:
    print("Both airlines share some destinations.")
else:
    print("There are no shared destinations between the two airlines.")