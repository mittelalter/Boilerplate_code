import pandas as pd
import requests
from bs4 import BeautifulSoup

data_list = []

for year in range(2010, 2013):
    for month in range(1, 13):
        for week in range(0, 5):
            url = requests.get(
                f"https://workey.codeit.kr/ratings/index?year={year}&month={month}&weekIndex={week}"
            )
            soup = BeautifulSoup(url.text, "html.parser")

            if len(soup.select(".row")) > 1:
                for tr_tags in soup.select("tr.row")[1:]:
                    td_tags = tr_tags.select("td")

                    period = soup.select_one(
                        "#weekSelectBox > option[selected:selected]"
                    ).get_text()
                    # td_ta
                    rank = td_tags[0].get_text()
                    channel = td_tags[1].get_text()
                    program = td_tags[2].get_text()
                    rating = td_tags[3].get_text()

                    data_list.append([period, rank, channel, program, rating])


df = pd.DataFrame(
    data=data_list, columns=["period", "rank", "channel", "program", "rating"]
)
df.head()
