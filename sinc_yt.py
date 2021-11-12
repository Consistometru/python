import requests
import json


url = ['https://youtube.com/c/Dave2D/videos',
        'https://www.youtube.com/c/LinusTechTips/videos',
        'https://www.youtube.com/c/M539Restorations/videos',
        'https://www.youtube.com/c/Hagerty/videos',
	'https://www.youtube.com/c/RichRebuilds/videos',
	'https://www.youtube.com/user/bjornnyland/videos']
cookiee = {'CONSENT': 'YES+cb.20211109-06-p0.en-GB+F+643'}



def import_video_data(URL):
    print('Fetching Video page source using URL ' + URL)
    #window["ytInitialData"] =
    page_source = requests.get(URL, cookies = cookiee)
    page_source = page_source.text
    start_index = page_source.find('ytInitialData')
    tmp = page_source[ start_index+ 15:]
    end_index = tmp.find('}};')
    tmp = tmp[:end_index] + '}}'
    return tmp

def parse_json(json_data):
    json_dict = json.loads(json_data)
    return json_dict

def main():
    print('MAIN')
    j=0
    while j<len(url):
        json_data = import_video_data(url[j])
        yt_json = parse_json(json_data)    
    #with open('yt_scrape.json', 'w', encoding='utf-8') as f:
        #json.dump(yt_json, f, ensure_ascii=False, indent=4)
        i=0
        z=5
        while i<=z :
            short_views = \
                yt_json['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer'][
                    'contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items'][i]['gridVideoRenderer']['title'][
                        'accessibility']['accessibilityData']['label']
            print(short_views)
            i=i+1
        j=j+1
        print("++++++++++++++++++++++++++")

if __name__ == '__main__':
    main()

print('done')
input()
