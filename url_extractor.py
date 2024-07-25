
base_url = "https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-{}-episode-of-mann-ki-baat/"

# get ordinal suffix
def ordinal(n):
    if 10 <= (n % 100) <= 20:
        suffix = 'th'
    else:
        temp = n % 10
        if temp == 1:
            suffix = 'st'
        elif temp == 2:
            suffix = 'nd'
        elif temp == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    return str(n) + suffix

# list of all episode urls
episode_urls = []

# currently 111 episodes of mann ki baat are there
for num in range(1, 112):
    url = base_url.format(ordinal(num))
    episode_urls.append(url)

with open("mann_ki_baat_urls.txt", "w") as file:
    for url in episode_urls:
        file.write(url + "\n")