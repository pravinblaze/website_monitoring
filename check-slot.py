import requests

# URL for the API endpoint
url = "https://lift-api.vfsglobal.com/appointment/CheckIsSlotAvailable"

# Headers copied from the network inspection
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7",
    "authorize": ("EAAAAC7T5hR+QxPFIq+QqZ3mB0UrRaJVc5t5WOQIiKjEP37EDn6SsKhZU9JjleC+"
                  "yewij43W13HIBH7wRjZQ9Euq8B2Khtq+HKcNr0WCFv3KLXKNakvqjVcEQqzZhYMNbZT/"
                  "ov9Pa7rskqLMDeMlFLXFDneCh/4AKL3BhgWSCasAT5CqyH/JYGJPmS2tR9VnMBok469rODQ+"
                  "ynJYXhr/gwQbiyZY8pqHr9foU6UeYu2HgDzBOiq5gTbPVWnsUDi7EW/UJgxER9Sd6mjTj1sN1YTg+"
                  "sYAu6l3gweYRFdSNA7R9myXs1tJjP+VmovvGnaQHsa9ZKf0YHTMG5PFm+L5xnPntwfr/bC7YujJXzyUV1WyF8R091CkFkavuQfYGwMZMmVzyXMB/G887aTvTjwqYnkPgHHorhEF66mXMCAkWTAkjoXOHxaGqFFoQub6cqg3xDoSFFYGoNA7YWkjuuqnccd9bTYy0BOjEJpuQal5r24KCTudGOpvana472UvYpg77sTAor3Be8UNEXw5vWgMWEAD9kk="),
    "clientsource": ("WfTol9BjKc0KwXGDPIUZFOYioANF29anW2vPr+B6UTmf7SqxT1GjhPP3iIBso9zh9cuX5btD36CMc0O8QIAcQzord697ZzgFzHO7Kl0sBzWAOI77BcVjoPjCf8wiZ0c928DEV2WKoL/C5ikvcBlrgfkTgYMN7TWxt+sCwA5musI="),
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://visa.vfsglobal.com",
    "referer": "https://visa.vfsglobal.com/",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"),
    # The cookie header is included as a single string.
    "cookie": ("OptanonAlertBoxClosed=2025-01-06T14:28:34.444Z; _ga=GA1.1.1322204339.1736173715; "
               "rxVisitor=1736173717711J58PS5GI1113A73B0TB4LQF7M8DHFKV5; _cfuvid=wL2DgCeAOvUtSMhpGVOsoCtKJfk_XkUndR8R7YwShU4-1739473099949-0.0.1.1-604800000; "
               "_gcl_au=1.1.933353399.1739473101; dtCookie=-12$4R2270CN9VCDDU26D2HH6STRFA8LG9EA; "
               "rxvt=1739474921856|1739473121856; _fbp=fb.1.1739473172436.53841611395215900; "
               "cf_clearance=WBaXXGhXhMrSRXzw1NkoZItYDeK7yvHrUtufpLtdEXY-1739473936-1.2.1.1-aIY88aZjCv8.4_Zjtg_omH5oxsHspqY3GeGsr_.EghzpVl8Ouq6OC0DjCKB8QOaf8osht3AFIcWWaYDqnMYdwov.dChOVcj.4ey3FZ3lOnTOeurHd3zqTMf47k64JBq4rQby2m2Ox8tyL5LbHbidWD_5YVJeGfN1nJCAk6oet5iRw9MYlsVyoUA9PgBS5IsDtcURHueX76vM5EpQlmLtc75pYgA4kFIQKMkeUTD6PN1TpSmi53oyMjlvBo7qSGCVY7lpBDLhyeplaIDOacfywJJ_LvI71dLzI6N7ok7r2nA; "
               "__cf_bm=RMsK_gvRISM4jmWxB6DUXiyoRFr4CXePywPdjMk5KGo-1739474084-1.0.1.1-OGwTtf3XokA_UdAzb_MPWrNFxU4UrwJobSOd41uRyQFPx9okPg254WI2oRwuObKclzR5rwMUGFxAUHv_aI9iNw; "
               "dtPC=-12$74221850_485h1p-12$74223363_462h1p-12$74243941_565h1p-12$74313151_646h1p-12$74314445_476h1vJWFPVGBBINUPVAFBQSABIIJUMVIEVFCC-0; "
               "OptanonConsent=isGpcEnabled=0&datestamp=Thu+Feb+13+2025+20%3A18%3A34+GMT%2B0100+(Central+European+Standard+Time)&version=202411.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=DE%3BBY&AwaitingReconsent=false; "
               "lt_sn=540448d6-e50a-488f-9c45-77546d50ad0f; _ga_Z8LKRKHHG4=GS1.1.1739473102.2.1.1739474332.40.0.0"),
}

# JSON payload (this is a placeholder; update it with the actual required data)
payload = {
    "key1": "value1",
    "key2": "value2"
}

# Perform the POST request
response = requests.post(url, headers=headers, json=payload)

# Output the response details
print("Status Code:", response.status_code)
print("Response Body:", response.text)
