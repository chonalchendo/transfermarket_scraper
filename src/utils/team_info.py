def get_team_info(league: str, league_id: str, year: int) -> tuple:
    link = "https://www.transfermarkt.co.uk/{league}/startseite/wettbewerb/{league_id}/plus/?saison_id={year}"
    url = link.format(league=league, league_id=league_id, year=year)
    resp = httpx.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0"
        },
        timeout=20,
    )
    soup = BeautifulSoup(resp.content, "html.parser")
    team_info = soup.find_all("td", {"class": "hauptlink no-border-links"})
    team_name = [td.find('a').get('href').split('/')[1] for td in team_info]
    team_id = [td.find('a').get('href').split('/')[4] for td in team_info]
    return tuple(zip(team_name, team_id))