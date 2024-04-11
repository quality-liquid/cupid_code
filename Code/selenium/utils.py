def flagParse():
    chrome = False
    headless = False
    with open('options.conf', 'r') as options:
        for line in options:
            if 'headless' in line:
                headless = 'true' in line
            if 'chrome' in line:
                chrome = 'true' in line
    return chrome, headless
