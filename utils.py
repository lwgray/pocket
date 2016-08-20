# coding: utf-8
import requests
from lxml import html
import pickle


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
    data = []
    for link in links:
        try:
            request = requests.get(link)
            if request.status_code == 403 or \
               request.status_code == 404:
                continue
            # Get article root
            root = html.fromstring(request.content)
            # Extract text from p, div and span elements
            texts = root.xpath("//p/text()")\
                + root.xpath("//div/text()")\
                + root.xpath("//span/text()")\
                + root.xpath("//pre/text()")
            content = " ".join([text.strip() for text in texts])
        except:
            continue
        data.append(content)
    with open('web_data.p', 'w') as web:
        pickle.dump(data, web)
    return


def main(filename):
    ''' Extract pocket articles' content '''
    with open('training_data.p', 'r') as txt:
        txt = pickle.load(txt)
        urls = get_links(txt)
        get_content(urls)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Web Data for topic analysis')
    parser.add_argument('--filename', '-f', required=True, help='Training or Test Data')
    args = parser.parse_args()
    sys.exit(main(args.filename))
