#!/usr/bin/env python
#-*-coding:utf-8-*-

import pymysql

def _decode_utf8(str):
    return str.encode('utf-8','ignore').decode('utf-8')



def write_team_data(team_id,team_name,country,create_year,league,coach,city,match_place,website,intro,img_url):

    conn = pymysql.connect(host='192.168.2.159',port=3306,user='root',passwd='root',db='worldcup',charset='utf8')
    cursor = conn.cursor()

    #插入数据
    try:
        intro =pymysql.escape_string(intro)

        cursor.execute('INSERT INTO team_data (team_id,team_name,country,create_year,league,coach,city,match_place,website,intro,img_url)VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(team_id,team_name,country,create_year,league,coach,city,match_place,website,intro,img_url))
    except Exception as e:
        print e
        pass
    cursor.close()
    conn.commit()
    conn.close()

def write_history_match(team_id,schedule,match_time,home_team,market,visit_team,score,half_score,result,market_trend,bet_type1,bet_type2,goal_number):
    
    conn = pymysql.connect(host='192.168.2.159',port=3306,user='root',passwd='root',db='worldcup',charset='utf8')
    cursor = conn.cursor()

    #插入数据
    try:

        cursor.execute('INSERT INTO history_match (team_id,schedule,match_time,home_team,market,visit_team,score,half_score,result,market_trend,bet_type1,bet_type2,goal_number)VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(team_id,schedule,match_time,home_team,market,visit_team,score,half_score,result,market_trend,bet_type1,bet_type2,goal_number))
    except Exception as e:
        print e
        pass
    cursor.close()
    conn.commit()
    conn.close()

