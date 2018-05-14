#!/usr/bin/env python
#-*-coding:utf-8-*-

import controler
import downloader
import pageparser
import time
import sqlite3
import string
import os
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')


main_url = 'http://2018.zgzcw.com/fixtures.shtml'




def main(entrance):
    start_time = time.time()
    
    print "entrance:{}".format(entrance)

    entrance_html = downloader.get_html(entrance)
    teams_url_list = pageparser.get_teams(entrance_html)
    
    for x in teams_url_list:
        print 'spider to url:{}'.format(x)
        team_id = int(x.split('/')[-1])
        
        team_html = downloader.get_html(x)
        try:
            team_name,country,create_year,league,coach,city,match_place,website,intro,img_url = pageparser.get_team_info(team_html)
            schedule,match_time,home_team,market,visit_team,score,half_score,result,market_trend,bet_type1,bet_type2,goal_number = pageparser.get_team_history_match(team_id,team_html)

            controler.write_team_data(team_id,team_name,country,create_year,league,coach,city,match_place,website,intro,img_url)
            print 'running time:{}s'.format(str(time.time()-start_time))

        except Exception as e:
            print e
            with open('fail_url.txt', 'a') as fd:
                fd.write('{}\n{}'.format(e,x))
            continue

if __name__ == '__main__':
    main('http://2018.zgzcw.com/fixtures.shtml')
