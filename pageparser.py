#!/usr/bin/env python
#-*-coding:utf-8-*-

import os
from bs4 import BeautifulSoup
import requests
import sys
import json
from lxml import etree
import controler

reload(sys)
sys.setdefaultencoding('utf-8')




def get_teams(html):
    
    selector = etree.HTML(html)
    teams_xpath = "body/div[3]/div[2]/div[{}]/a[{}]"
    teams_url_list = []

    for div_num in range(1,9):
        for a_num in range(1,5):
            try:
                teams_url = selector.xpath(teams_xpath.format(str(div_num),str(a_num)))[0].get('href')
                teams_url_list.append(teams_url)                
            except IndexError,e:
                print div_num,a_num
    return teams_url_list




def get_team_info(html):

    selector = etree.HTML(html)
    soup = BeautifulSoup(html, "html.parser")
    
    team_name_xpath='body/div[5]/div[2]/div[1]/dl[1]/dt/span'
    country_xpath='body/div[5]/div[2]/div[1]/dl[1]/dd[1]/var'
    create_year_xpath='body/div[5]/div[2]/div[1]/dl[1]/dd[2]/var'
    league_xpath='body/div[5]/div[2]/div[1]/dl[1]/dd[3]/var'
    coach_xpath='body/div[5]/div[2]/div[1]/dl[1]/dd[4]/var'
    city_xpath='body/div[5]/div[2]/div[1]/dl[1]/dd[5]/var'
    match_place_xpath='body/div[5]/div[2]/div[1]/dl[1]/dd[6]/var'
    website_xpath='body/div[5]/div[2]/div[1]/dl[1]/dd[8]/var/a'
    intro_xpath='body/div[5]/div[2]/div[1]/dl[2]/dd/div/span/span/p[1]/span/span'
    img_url_xpath ='body/div[5]/div[2]/div[1]/dl[1]/dt/img'


    team_name = selector.xpath(team_name_xpath)[0].text
    country = selector.xpath(country_xpath)[0].text
    create_year = selector.xpath(create_year_xpath)[0].text
    league = selector.xpath(league_xpath)[0].text
    coach = selector.xpath(coach_xpath)[0].text
    city = selector.xpath(city_xpath)[0].text
    match_place = selector.xpath(match_place_xpath)[0].text
    website = selector.xpath(website_xpath)[0].text
    intro = soup.select('div[class="introduceDiv"]')[0].text

    img_url = selector.xpath(img_url_xpath)[0].text

    return team_name,country,create_year,league,coach,city,match_place,website,intro,img_url
    


def get_team_history_match(team_id,html):
    
    selector = etree.HTML(html)
    
    # last 30 record
    record_xpath =".//*[@id='m_{}']/td[{}]"
    
    # absolute xpath
    # record_xpath="body/div[5]/div[2]/div[3]/table/tbody[{}]/tr[{}]/td[{}]"
    # selector.xpath(record_xpath.format('1','20','3'))[0][0].text
    
    for m_num in range(0,30):#0-29
        # for td_num in range(1,12):#1-11
            try:
                schedule = selector.xpath(record_xpath.format(str(m_num),'1'))[0].text
                match_time = selector.xpath(record_xpath.format(str(m_num),'2'))[0].text
                home_team = selector.xpath(record_xpath.format(str(m_num),'3'))[0][0].text
                market = selector.xpath(record_xpath.format(str(m_num),'4'))[0][0].text
                visit_team = selector.xpath(record_xpath.format(str(m_num),'5'))[0][0].text
                score = selector.xpath(record_xpath.format(str(m_num),'6'))[0][0].text
                half_score = selector.xpath(record_xpath.format(str(m_num),'7'))[0][0].text
                result = selector.xpath(record_xpath.format(str(m_num),'8'))[0][1].text
                market_trend = selector.xpath(record_xpath.format(str(m_num),'9'))[0][0].text
                bet_type1 = selector.xpath(record_xpath.format(str(m_num),'10'))[0][0].text
                bet_type2 = selector.xpath(record_xpath.format(str(m_num),'10'))[0][1].text
                goal_number = selector.xpath(record_xpath.format(str(m_num),'11'))[0][0].text
        
                controler.write_history_match(team_id,schedule,match_time,home_team,market,visit_team,score,half_score,result,market_trend,bet_type1,bet_type2,goal_number)
                
            except IndexError,e:
                print m_num

    return schedule,match_time,home_team,market,visit_team,score,half_score,result,market_trend,bet_type1,bet_type2,goal_number

# team_url_list
#    ['http://saishi.zgzcw.com/soccer/team/767',
#  'http://saishi.zgzcw.com/soccer/team/891',
#  'http://saishi.zgzcw.com/soccer/team/746',
#  'http://saishi.zgzcw.com/soccer/team/735',
#  'http://saishi.zgzcw.com/soccer/team/772',
#  'http://saishi.zgzcw.com/soccer/team/765',
#  'http://saishi.zgzcw.com/soccer/team/783',
#  'http://saishi.zgzcw.com/soccer/team/813',
#  'http://saishi.zgzcw.com/soccer/team/638',
#  'http://saishi.zgzcw.com/soccer/team/913',
#  'http://saishi.zgzcw.com/soccer/team/649',
#  'http://saishi.zgzcw.com/soccer/team/774',
#  'http://saishi.zgzcw.com/soccer/team/766',
#  'http://saishi.zgzcw.com/soccer/team/756',
#  'http://saishi.zgzcw.com/soccer/team/768',
#  'http://saishi.zgzcw.com/soccer/team/789',
#  'http://saishi.zgzcw.com/soccer/team/648',
#  'http://saishi.zgzcw.com/soccer/team/778',
#  'http://saishi.zgzcw.com/soccer/team/642',
#  'http://saishi.zgzcw.com/soccer/team/914',
#  'http://saishi.zgzcw.com/soccer/team/644',
#  'http://saishi.zgzcw.com/soccer/team/898',
#  'http://saishi.zgzcw.com/soccer/team/650',
#  'http://saishi.zgzcw.com/soccer/team/819',
#  'http://saishi.zgzcw.com/soccer/team/798',
#  'http://saishi.zgzcw.com/soccer/team/645',
#  'http://saishi.zgzcw.com/soccer/team/744',
#  'http://saishi.zgzcw.com/soccer/team/823',
#  'http://saishi.zgzcw.com/soccer/team/815',
#  'http://saishi.zgzcw.com/soccer/team/903',
#  'http://saishi.zgzcw.com/soccer/team/775',
#  'http://saishi.zgzcw.com/soccer/team/637']