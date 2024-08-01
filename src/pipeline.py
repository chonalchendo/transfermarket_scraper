from pathlib import Path

import pandas as pd

from .savers import ParquetSaver
from .schemas import Team
from .scraper import PlayerScraper, TeamScraper, MultiScraper


def team_scraper() -> None:
    output = Path().cwd() / "src" / "data" / "team_info.parquet"

    scraper = TeamScraper(
        league="premier-league",
        league_id="GB1",
        year=2023,
        saver=ParquetSaver(output_path=output),
    )

    scraper.scrape()


def player_scraper() -> None:
    input_path = Path().cwd() / "src" / "data" / "team_info.parquet"
    output_path = Path().cwd() / "src" / "data" / "player_info.parquet"

    team_info = pd.read_parquet(input_path)

    teams = [
        Team(id=team.team_id, name=team.team_name)
        for team in team_info.itertuples(
            index=False
        )
    ]

    scrapers = [PlayerScraper(team=team, year=2023) for team in teams]

    multi_scraper = MultiScraper(
        scrapers=scrapers, saver=ParquetSaver(output_path=output_path)
    )

    multi_scraper.scrape()


def main() -> None:
    player_scraper()


if __name__ == "__main__":
    main()
