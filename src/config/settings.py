class URL:
    PLAYER: str = (
        "https://www.transfermarkt.co.uk/{name}/kader/verein/{id}/saison_id/{year}/plus/1"
    )
    TEAM: str = (
        "https://www.transfermarkt.co.uk/{league}/startseite/wettbewerb/{league_id}/plus/?saison_id={year}"
    )
