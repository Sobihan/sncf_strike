def get_date():
    from datetime import date
    # return the date
    date = date.today()
    month = date.strftime("%m")
    day = date.strftime("%d")

    calendar = {
        "01": "jan",
        "02": "fev",
        "03": "mar",
        "04": "apr",
        "05": "may",
        "06": "jun",
        "07": "jul",
        "08": "aug",
        "09": "sep",
        "10": "oct",
        "11": "nov",
        "12": "dec"
        }

    return ([calendar[month], day])

def notify(title, subtitle, message):
    import os
    # To Notify in macos
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

def get_url():
    date = get_date()
    url = 'http://sn.cf/cp-gni-' + date[1] + date[0]
    return(url)

def page_exist(url):
    import requests
    headers = {"User-Agent":
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    page = requests.get(url, headers=headers)
    if (page.status_code == 403 or page.status_code == 404):
        return False
    return True

def main():
    import time, webbrowser
    
    url = get_url()
    while (page_exist(url) == False):
        print("Les prévisions pour demain ne sont toujours pas disponible")
        time.sleep(30)
    notify(title    = 'Prévision pour demain', subtitle = 'With Python', message  = 'Hello, c\' est bon les prévisions sont enfin disponible...')
    webbrowser.open(url)
    
if __name__ == '__main__':
    main()
