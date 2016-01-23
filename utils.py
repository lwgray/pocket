# coding: utf-8
import requests
from lxml import html
import pickle
from progress.bar import Bar


def get_links(data):
    """
    Extract resolved urls from saved pocket articles
    """
    print "Getting Links"
    links = [value['resolved_url'] for item in data for key, value in item.iteritems()]
    print "Got Links"
    print links[0]
    return links


def get_content(links):
    """ 
    Extract relevant content related to article
    """
    print "requesting content"
    bar = Bar('Progress --> ', max=len(links))
    data = []
    for link in links:
        bar.next()
        try:
            print "Request Sent"
            request = requests.get(link)
            print "status received {0}".format(request.status_code)
            if request.status_code == 403 or \
               request.status_code == 404:
                continue 
            # Get article root
            print "Accessing Article root"
            root = html.fromstring(request.content)
            # Extract text from p, div and span elements
            print "Extracting text"
            texts = root.xpath("//p/text()")\
                + root.xpath("//div/text()")\
                + root.xpath("//span/text()")\
                + root.xpath("//pre/text()")
            content = " ".join([text.strip() for text in texts])
        except:
            continue
        data.append(content)
    bar.finish()
    print "Returning Content"
    return data
