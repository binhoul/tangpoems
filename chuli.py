#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re
import random
import MySQLdb
import copy



def chuli(inparams):
    poemlist = []
    detail= {"id":"", "title":"", "author":"", "yearof":"", "content":""}
    detailcopy = copy.copy(detail)
    lines = open(inparams).readlines()
    findex = 0
    for findex in xrange(len(lines)):
        if lines[findex].startswith('==') and findex + 4 < len(lines) :
            detail['id'] = random.randint(99999,999999)
            detail['title'] = re.search("《(.*)》", lines[findex + 1]).group(1)
            detail['author'] = lines[findex + 2].split('：')[1]
            poemcontent = ""
            subindex = findex + 4
            while( not lines[subindex].startswith("\r\n")):
                poemcontent += lines[subindex].strip('\r\n')
                subindex += 1
            detail['content'] = poemcontent
            poemlist.append(detail)
            detail = copy.copy(detailcopy)

    return poemlist

def tosql(poemlist):
    host = "127.0.0.1"
    user = "root"
    password = "fengmao"
    conn = MySQLdb.connect(host=host,user=user,passwd=password,db='cp',charset='utf8')
    cur = conn.cursor()
    cur.execute("set names utf8")
    for xpoem in poemlist:
        sql = "insert into poems values (%s,%s,%s,'2014',%s)"
        params = (xpoem['id'],xpoem['title'],xpoem['author'],xpoem['content'])
        print params
        try:
            cur.execute(sql,params)
        except MySQLdb.Error,e:
            print "Mysql error %d: %s" %(e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    orderlist = chuli(sys.argv[1])
    tosql(orderlist)
