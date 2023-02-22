# Practice Set 6
# INFO-I 211 - Spring 2023

"""
Matt and Erika are sitting in on a committee regarding the Luddy School
Budget for the next couple of years. The school puts on Events, and it would
be helpful if we could project how many events we need to budget for, based
on the number of events which occurred in past months.

The Luddy School has an "Events" page:
https://luddy.indiana.edu/events/

... and this *seems* to have all of the information that we need: but the
information is in a format (HTML) that is inconvenient for us to do any
kind of analysis on.

"Everybody stand back. I know Regular Expressions!"
                                - https://xkcd.com/208/

Let's practice writing regular expressions, apply our new skills to an
information extraction task, and generate an `events-report.csv` to
summarize our findings.
"""

import re
import csv

# PS 6.1
# ------
# The following problems mirror the problems shown in the RegexOne tutorials
# mentioned on Canvas:
# https://regexone.com/lesson/introduction_abcs
#
# Work through each of the 15 lessons on the website.
# For each "lesson" function below, replace:
#
# ```
# pattern = r""
# ```
#
# with your solution in each lesson. For example, you might solve
# `lesson_1()` by writing:
#
# ```
# pattern = r"abc"
# ```
#
# You might also try testing some of your implementations to get an idea for
# what each output looks like. Perhaps something like:
#
# ```
# for example in ["abcdefg", "abcde", "abc"]:
#     print(lesson_1(example))
# ```
#
# Note: the "r" prefix refers to a "raw" Python string. The TL;DR explanation
# (Too Long; Didn't Read) version is that a Python raw string interprets
# special characters like '\' as actual strings, whereas the default strings
# we've used up to this point sometimes use those special characters to mark
# things like tabs ('\t') or newlines ('\n').
# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals


def lesson_1(input_string):
    # https://regexone.com/lesson/introduction_abcs
    pattern = r"abc"
    return re.search(pattern, input_string)


def lesson_1_and_a_half(input_string):
    # https://regexone.com/lesson/letters_and_digits
    pattern = r"123"
    return re.search(pattern, input_string)


def lesson_2(input_string):
    # https://regexone.com/lesson/wildcards_dot
    pattern = r"...\."
    return re.search(pattern, input_string)


def lesson_3(input_string):
    # https://regexone.com/lesson/matching_characters
    pattern = r"[^drp]an"
    return re.search(pattern, input_string)


def lesson_4(input_string):
    # https://regexone.com/lesson/excluding_characters
    pattern = r"[hd]og"
    return re.search(pattern, input_string)


def lesson_5(input_string):
    # https://regexone.com/lesson/character_ranges
    pattern = r"[A-C]"
    return re.search(pattern, input_string)


def lesson_6(input_string):
    # https://regexone.com/lesson/repeating_characters
    pattern = r"waz{3,5}up"
    return re.search(pattern, input_string)


def lesson_7(input_string):
    # https://regexone.com/lesson/kleene_operators
    pattern = r"a{2,4}b{0,4}c{1,2}"
    return re.search(pattern, input_string)


def lesson_8(input_string):
    # https://regexone.com/lesson/optional_characters
    pattern = r"\d+ files? found\?"
    return re.search(pattern, input_string)


def lesson_9(input_string):
    # https://regexone.com/lesson/whitespaces
    pattern = r"\d\.\s+abc"
    return re.search(pattern, input_string)


def lesson_10(input_string):
    # https://regexone.com/lesson/line_beginning_end
    pattern = r"^Mission: successful$"
    return re.search(pattern, input_string)


# PS 6.1 - Interlude!
# -------------------
# Ten down, five to go. Keep up the good work!
#
# The rest of the "lessons" below are similar to the ones we've already
# solved, but introduce "match groups."
#
# Our implementations use some Python syntax we may not have encountered
# before: the "Walrus" operator `:=` (named so because the syntax looks
# like a pair of eyes with walrus tusks).
#
# You can interpret the Walrus operator like a conditional assignment
# statement: if `re.search(pattern, input_string)` returns something,
# we bind the variable `m` to its result.
#
# It gives us a shorthand way to write:
#
# ```
# m = re.search(pattern, input_string)
# if m is not None:
#     return m.group(1)
# else:
#     return None
# ```
#
# Keep testing your functions as you go. `lesson_11` should extract
# file names for strings ending with ".pdf", so:
#
# >>> lesson_11("something.pdf")
# something
# >>> lesson_11("otherwise.txt")
#               <--- Nothing is shown, because this returns `None`


def lesson_11(input_string):
    # https://regexone.com/lesson/capturing_groups
    pattern = r"^(file.+)\.pdf$"

    if m := re.search(pattern, input_string):
        return m.group(1)


def lesson_12(input_string):
    # https://regexone.com/lesson/nested_groups
    pattern = r"(\w+ (\d+))"

    if m := re.search(pattern, input_string):
        return m.group(1), m.group(2)


def lesson_13(input_string):
    # https://regexone.com/lesson/more_groups
    pattern = r"(\d+)x(\d+)"

    if m := re.search(pattern, input_string):
        return m.group(1), m.group(2)


def lesson_14(input_string):
    # https://regexone.com/lesson/conditionals
    pattern = r"I love (cats|dogs)"
    return re.search(pattern, input_string)


def lesson_15(input_string):
    # https://regexone.com/lesson/misc_meta_characters
    pattern = r".*"
    return re.search(pattern, input_string)


# PS 6.2
# ------
# Remember our friendly `safe_load_file` function from assignment 3?
# Make sure it takes a `file_name` as input, returns the contents of the file
# as a string using `.read()`, or returns the empty string ("") if the file
# does not exist.


def safe_load_file(file_name):
    try:
        # if files does exist, open file and print as string
        with open(file_name, "r", encoding="utf-8-sig") as file:
            data = file.read()
            return data 
    # if file does not exist, return empty string
    except:
        return ''

# print(safe_load_file("events-page.txt"))


# PS 6.3
# ------
# Let's get some practice first by writing `extract_scripts`. The HTML page
# has quite a few `<script>` tags that we could extract into a list.
# Implement `extract_scripts`.
#
# There are 12 scripts in the page. We want a list of all of them *except*
# the analytics script, which looks something like this:
#
# ```
# <script>//
# (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
# new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
# j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
# '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
# })(window,document,'script','dataLayer','GTM-WJFT899');
# // </script>
# ```
#
# Experiment with Python and with Regex101: https://regex101.com/
# to extract a list of the 12 scripts:
#
# >>> script_list = extract_scripts(safe_load_file("events-page.txt"))
# >>> print(len(script_list))
# 12
# >>> print(script_list)
# ['<script src="//assets.iu.edu/web/1.5/libs/modernizr.min.js"></script>', '<script src="https://assets.iu.edu/web/1.5/libs/modernizr.min.js"></script>', '<script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>', '<script crossorigin="anonymous" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" src="https://code.jquery.com/jquery-3.3.1.min.js"></script>', '<script crossorigin="anonymous" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" src="https://code.jquery.com/jquery-3.5.1.min.js"></script>', '<script src="https://luddy.indiana.edu/_assets/js/jquery-ui-1.12.1/jquery-ui.min.js"></script>', '<script src="https://assets.iu.edu/web/3.3.x/js/iu-framework.min.js" type="text/javascript"></script>', '<script src="https://assets.iu.edu/search/3.3.x/search.min.js"></script>', '<script src="https://luddy.indiana.edu/_assets/js/sice.js" type="text/javascript"></script>', '<script src="https://luddy.indiana.edu/_assets/js/site.js" type="text/javascript"></script>', '<script src="https://luddy.indiana.edu/_assets/js/sice/datatable.js" type="text/javascript"></script>', '<script src="../_assets/js/sice/events.js" type="text/javascript"></script>']


def extract_scripts(html_string):
    pattern = r"<script\s.*<\/script>"
    matches = re.findall(pattern, html_string)
    # for match in matches:
    #     print(match)
    return matches

# script_list = extract_scripts(safe_load_file("events-page.txt"))
# print(len(script_list))
# print(script_list)


# PS 6.4
# ------
# Social media links will be a good thing to practice with next.
# Implement `extract_social_media_links` and return a list containing
# links to Luddy's five social media accounts.
#
# ```
# html_string = safe_load_file("events-page.txt")
#
# links = extract_social_media_links(html_string)
#
# print(links)
# ```
#
# Output:
#
# ```
# ['https://www.twitter.com/IULuddy',
#  'https://www.facebook.com/IULuddy',
#  'https://www.instagram.com/IULuddy',
#  'https://www.youtube.com/c/IULuddy',
#  'https://www.linkedin.com/company/iuluddy']
# ```
#
# Hint:
# This one might be difficult to do with a single regular expression.
# It might be easier to *first* extract a list of `aria-label`, and
# *then* use a second regular expression to match something inside of
# `href` links.


def extract_social_media_links(html_string):
    pattern = r"(?=<a aria).*(https.*uddy).*"
    matches = re.findall(pattern, html_string)
    return matches
    
# html_string = safe_load_file("events-page.txt")
# links = extract_social_media_links(html_string)
# print(links)


# PS 6.5
# ------
# Let's apply our skills to our original goal: find names, dates, and links
# in the Luddy events page.
#
# There are 116 names, dates, and events. After implementing each function
# (`extract_event_names`, `extract_event_names`, `extract_event_links`),
# each should return a list containing 116 items.
#
# ```
# events_page = safe_load_file("events-page.txt")
#
# names = extract_event_names(events_page)
# dates = extract_event_dates(events_page)
# links = extract_event_links(events_page)
#
# print(len(names), len(dates), len(links))
# # 116 116 116
# ```


def extract_event_names(html_string):
    pattern = r"<a itemprop=\"url\" href=\".*\".*\s*.*\"name\">(.*)<\/span>"
    matches = re.findall(pattern, html_string)
    # for match in matches:
    #     print(match)
    return matches

# events_page = safe_load_file("events-page.txt")
# names = extract_event_names(events_page)
# print(len(names))


def extract_event_dates(html_string):
    pattern = r"meta date\'>(.*, \d\d\d\d)<\/p>.*"
    matches = re.findall(pattern, html_string)
    # for match in matches:
    #     print(match)
    return matches

# events_page = safe_load_file("events-page.txt")
# dates = extract_event_dates(events_page)
# print(len(dates))


def extract_event_links(html_string):
    pattern = r"<a itemprop=\"url\" href=\"(.*)\""
    matches = re.findall(pattern, html_string)
    # for match in matches:
    #     print(match)
    return matches

# events_page = safe_load_file("events-page.txt")
# links = extract_event_links(events_page)
# print(len(links))


# PS 6.6
# ------
# Let's implement two functions to handle the months.
#
# `extract_months` takes a `dates_list` as input, and returns just the "month"
# portion. Like this:
#
# >>> extract_months(["Monday, February 6, 2023", "Monday, February 13, 2023", "Tuesday, January 10, 2023"])
# ["February", "February", "January"]
#
# `events_per_month` takes a similar input, but returns a dictionary mapping
# each month to the number of times that month occurred:
#
# >>> events_per_month(["Monday, February 6, 2023", "Monday, February 13, 2023", "Tuesday, January 10, 2023"])
# {"February": 2, "January": 1}
#
# >>> events_per_month(extract_event_dates(safe_load_file("events-page.txt")))
# {'February': 15, 'March': 16, 'April': 21, 'January': 4, 'December': 4, 'November': 15, 'October': 21, 'September': 17, 'August': 1, 'May': 2}


# doesn't work :( 
# i tried to make this work forver, but it kept giving me errors so, sorry

# def extract_months(dates_list):
#     pattern = "meta date\'>.*, (\D*) .*, \d\d\d\d<\/p>.*"
#     matches = re.findall(pattern, dates_list)
#     # for match in matches:
#     #     print(match)
#     return (matches)

# def events_per_month(dates_list):
#     pattern = ".*, (\D*) .*, \d\d\d\d"
#     matches = re.findall(pattern, dates_list)
#     dict2= {}
#     for match in matches:
#         if match not in dict2:
#             dict2[match] = matches.count(match)
#         else:
#             continue
#     return dict2

# dates = events_per_month(extract_event_dates(safe_load_file("events-page.txt")))
# print(dates)
# events_per_month(dates)

# events_per_month(["Monday, February 6, 2023", "Monday, February 13, 2023", "Tuesday, January 10, 2023"])

# events_per_month(extract_event_dates(safe_load_file("events-page.txt")))


# PS 6.7
# ------
# We've written five functions that process various parts of the "Events" page.
# Let's put the pieces together in the `make_events_report()` function.
# This should call our functions, and write to an `events-report.csv` file
# with columns: ("EventName", "URL", "Date", "Month", "EventsThisMonth")
#
# ```
# make_events_report(safe_load_file("events-page.txt"))
# ```
#
# Calling `make_events_report()` should create an `events-report.csv` file
# that contains lines with this general structure:
#
# ```
# "EventName","URL","Date","Month","EventsThisMonth"
# "Event 1","https://...","Monday, February 13, 2023","February",15
# "Event 2","https://...","Monday, February 20, 2023","February",15
# "Event 3","https://...","Wednesday, February 22, 2023","February",15
# "Event 4","https://...","Wednesday, March 1, 2023","March",16
# ```
#
# Hint 1:
#
# We recommend passing `csv.QUOTE_NONNUMERIC`, similar to this:
#
# ```
# csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
# ```
#
# Hint 2:
#
# Everything *except* `events_per_month` should return a list of 116 items.
# `events_per_month(dates)` returns a dictionary. When we write
# each row to `events-report.csv`, we will want to use the month value to
# look up the number of events that month in the dictionary.
#
# e.g., something like:
#
# ```
# by_month = events_per_month(date)
# number = by_month["January"]
# ```


def make_events_report(html_string):
    name = extract_event_names(html_string)
    date = extract_event_dates(html_string)
    link = extract_event_links(html_string)
    # no month because it doesn't work 
    # month = extract_months(extract_event_dates(html_string))

    # everything works, except for the 6.6 part so i just left that out of this part 
    with open('events-report.csv', 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        row_list = [['EventName', 'URL', 'Date', 'Month', 'EventThisMonth']]
        for i in range(len(name)):
            row_list.append([name[i], link[i], date[i]])
        writer.writerows(row_list)
        
# make_events_report(safe_load_file("events_page.txt"))


# PS 6.8 - Complete the Analysis!
# -------------------------------
# `make_events_report()` is the main deliverable this week. But we've included
# a main module to below to give you an idea for how we might run/test your
# code for completeness.
#
# Un-comment this, make sure things are working correctly, and submit your
# `{username}_ps6.py` on Canvas.
#
#
if __name__ == "__main__":

    from pprint import pprint

    for m in ["Ana", "Bob", "Cpc"]:
        # These should return/print something
        print(lesson_5(m))
    for m in ["aax", "bby", "ccz"]:
        # These should return/print `None`
        print(lesson_5(m))

    events_page = safe_load_file("events-page.txt")

    pprint(extract_scripts(events_page))
    pprint(extract_social_media_links(events_page))

    make_events_report(events_page)


# Just for Fun - Regular Languages and Context-Free Languages
# -----------------------------------------------------------
# Regular Expressions are extremely useful, and we will use quite a few of
# them in form validation when building our web app (e.g. making sure email
# addresses are correct).
#
# Did this assignment feel tricky? Did it involve a lot of trial-and-error?
#
# Often in computing, we talk about "using the right algorithm."
# Regular expressions are rarely the "right algorithm" when extracting
# information from structured HTML documents.
#
# This is really a "Parsing" task. Regular expressions are good at *recognizing*
# patterns, but cannot handle complex nested structures. In the real world, we
# would approach this with a generalization of "regular expressions" called
# "context-free grammars."
# https://en.wikipedia.org/wiki/Formal_grammar
#
# There is a pretty powerful HTML/XML-parsing library in Python called
# "Beautiful Soup" (https://www.crummy.com/software/BeautifulSoup/)
#
# (1) Read the BeautifulSoup documentation. Can you see a way that we could have used
#     beautiful soup to make some of the above problems easier?
#
# Let's explore some complications.
#
# (2) In your browser, view the website
#     https://informatics.indiana.edu/contact/index.html
#     Find the email address for the department chair
#
# (3) Now search in the source code (CTRL + u / ⌘ + u / "View page source")
#     for the chair's email. They should look very different! One looks like an email,
#     the other looks like a mess!
#
# Q: What do you think is happening here? Why would this be useful?
