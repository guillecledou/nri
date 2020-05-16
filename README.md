# NRI Spider

A simple [Scrapy](https://scrapy.org/) spider to get data from the
[Network Readiness Index 2019](https://networkreadinessindex.org/) site.
For each country it retrieves the score of the four main pillars,
and the score and rank of their sub pillars.

In particular, it retrieves the following information for each surveyed country.

- Country
- Technology Score
- Access Score
- Access Rank
- Content Score
- Content Rank
- Future technology Score
- Future technology Rank
- Impact Score
- Economy Score
- Economy Rank
- Quality of life Score
- Quality of life Rank
- SDG Contribution Score
- SDG Contribution Rank
- People Score
- Individuals Score
- Individuals Rank
- Businesses Score
- Businesses Rank
- Governments Score
- Governments Rank
- Governance Score
- Trust Score
- Trust Rank
- Regulation Score
- Regulation Rank
- Inclusion Score
- Inclusion Rank

# Requirements

You need Scrapy, which you can install with the following command.

```bash
pip install scrapy
```

# Usage

After cloning the repository, move into the project folder and run the following command.

```bash
scrapy crawl nri
```

If everything goes well, this will create a ``nri_data.csv`` file with the requested data.

Currently, the website has some issue with all the information from Kyrgyzstan and some information from Hungary.
However, this information can be manually retrieved from the report.
