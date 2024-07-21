from .scraper import TeamScraper, PlayerScraper
from .savers import ParquetSaver
from .schemas import Team
from pathlib import Path
from rich import print
import pandas as pd
import time


def team_scraper() -> None:
    output = Path().cwd() / "src" / "data" / "team_info.parquet"

    scraper = TeamScraper(
        league="premier-league",
        league_id="GB1",
        year=2023,
        saver=ParquetSaver(output_path=output),
    )

    scraper.run()


def player_scraper() -> None:
    path = Path().cwd() / "src" / "data" / "team_info.parquet"
    team_info = pd.read_parquet(path)

    teams = [
        Team(id=id, name=name)
        for id, name in zip(team_info["team_id"], team_info["team_name"])
    ]

    for team in teams:
        scraper = PlayerScraper(
            year=2023,
            team=team,
        )

        data = scraper.run()
        print(data)
        time.sleep(5)


def main() -> None:
    player_scraper()


if __name__ == "__main__":
    main()
