#!/usr/bin/python
# Based on concurrent_download.py by Denis Bilenko
# https://github.com/surfly/gevent/blob/master/examples/concurrent_download.py

"""Spawn multiple workers and wait for them to complete"""
from __future__ import print_function

import json
from urllib2 import urlopen

#from gevent import monkey
import gevent
from gevent.queue import Queue


# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
#monkey.patch_all()
def query_url(url, result_queue):
    data = urlopen(url)
    json_data = json.loads(data.read())
    result_queue.put(json_data)

def batch_query(requests):
    result_queue = Queue()
    jobs = [gevent.spawn(query_url, request, result_queue) for request in requests]
    gevent.joinall(jobs)
    result_queue.put(StopIteration)
    
    results = []
    for data in result_queue :
        results.append(data)
    return results
