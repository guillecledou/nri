# -*- coding: utf-8 -*-
import scrapy


class NriSpider(scrapy.Spider):
    """A simple Scrapy spider to crawl some data from the Network Readiness Index 2019 site.
    For each country it retrieves the score of the four main pillars,
    and the score and rank of their sub pillars.
    """

    name = 'nri'
    allowed_domains = ['networkreadinessindex.org']
    start_urls = ['https://networkreadinessindex.org/nri-2019-countries/#complete-ranking']

    def parse(self, response):
        status = response.status
        url = response.css("title::text").get()
        print("HTTP STATUS: " + str(status))
        print(url)

        countries_url = response.css('.number-statistic a::attr(href)').extract()

        for country_url in countries_url:
            yield scrapy.Request(country_url, callback=self.parse_country)

    def parse_country(self, response):
        status = response.status
        country = response.css(".page-title-custom::text").get()
        print("HTTP STATUS: " + str(status))
        print(country)

        pillars_name = response.css('.title-accordion ::text').extract()
        pillars_score = response.css('.score-accordion ::text').extract()
        pillars_info = zip(pillars_name, pillars_score)

        pillars_html = response.css('.section-3-countries .panel')

        country_data = {'Country': country}

        # get information for each main pillar and its sub pillars
        for (pillar_info, sub_pillars_html) in zip(pillars_info, pillars_html):
            # sub pillars names for current pillar
            sub_pillars = sub_pillars_html.css('.accordion-intern-title::text').extract()
            # a list of scores and ranks for sub pillars [score1, rank1, score2, ...]
            numbers = sub_pillars_html.css('.column-right-numbers::text').extract()
            # transform into pairs [(score1,rank1),...,(scoreN,rankN)]
            numbers_pairs = zip(numbers[::2], numbers[1::2])

            # add current main pillar info (score)
            country_data[f'{pillar_info[0].split(":")[1].strip()} Score'] = pillar_info[1]

            # add sub pillars info
            for sub_pillar in zip(sub_pillars, numbers_pairs):
                country_data[f'{sub_pillar[0].strip()} Score'] = sub_pillar[1][0]
                country_data[f'{sub_pillar[0].strip()} Rank'] = sub_pillar[1][1]

        yield country_data
