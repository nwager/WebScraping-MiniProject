from splinter import Browser
import sys, time
from twilio.rest import Client

account_sid = "ACf4c0b57408f916faa17aef730562cb61"
auth_token = "f323736f3adaf0a8984364ec9131eb92"

client = Client(account_sid, auth_token)

def main():

    if len(sys.argv) > 1:
        print "Welcome to bare minimum web page checking."
        url = sys.argv[1]
        if len(sys.argv) < 3:
            print "interval not stated please state now, default ten seconds."
            interval = 10
        elif len(sys.argv) == 3:
            interval = sys.argv[2]
        else:
            interval = sys.argv[2]
        check(url, interval)
    else:
        print "url and time was not given program defaulting to ten second interval, and cnn.com."
        interval = 10
        url = "http://www.cnn.com/"
        check(url, interval)
    
    
def check(url, interval):


    try:
        browser = Browser('chrome')
        browser.driver.set_window_size(1000,800)
        browser.visit(url)
        Original = len(browser.find_by_xpath('/html').text.encode('utf-8'))
        browser.quit()
        while True:
            print('To exit program ctrl+c')
            browser = Browser('chrome')
            browser.driver.set_window_size(1000,800)
            browser.visit(url)
            New = len(browser.find_by_xpath('/html').text.encode('utf-8'))
            if New != Original:
                changeMessage=("PAGE CHANGED from %d bytes to %d bytes!" % (Original, New))
                print changeMessage
                Original = New
                
                message = client.messages.create(
                    to="+15037043189",
                    from_="+19718034237",
                    body=changeMessage)
            else:
                print("No change detected")
                message = client.messages.create(
                    to="+15037043189",
                    from_="+19718034237",
                    body="No change detected")
            time.sleep(float(interval))
            browser.quit()
    except KeyboardInterrupt:
        print('Thank you for running this program exiting now.')
        sys.exit()

if __name__ == '__main__':
    main()