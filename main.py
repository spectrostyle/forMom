import checkEvents

# could change this to read a csv with the websites you want, updatable
url_list = ["https://tavaresfl.portal.civicclerk.com", 
            "https://clermontfl.portal.civicclerk.com",
            ]

def main():
    all_events = []

    for url in url_list:
        event_links = checkEvents.page_check(url)
        for event in event_links:
            all_events.append(event)

    links_with_minutes = []

    for link in all_events:
        minutes = checkEvents.get_minutes(link)
        if minutes != None:
            links_with_minutes.append(minutes)

    print(links_with_minutes)


if __name__ == "__main__":
    main()
