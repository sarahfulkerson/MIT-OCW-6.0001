# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
from abc import ABC, abstractmethod


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    """
    Used to represent a news story obtained from an RSS feed.
    """
    def __init__(self, guid: str, title: str, description: str, link: str, pubdate: datetime):
        """
        Creates a NewsStory object with the following attributes:

        self.guid (string): the globally unique identifier for a news story\n
        self.title (string): the title of a news story\n
        self.description (string): the description of a news story\n
        self.link (string): a link which takes you to additional content about a news story\n
        self.pubdate (datetime): the publication date of a news story\n
        """
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        """Returns: self.guid"""
        return self.guid
    
    def get_title(self):
        """Returns: self.title"""
        return self.title

    def get_description(self):
        """Returns: self.description"""
        return self.description
    
    def get_link(self):
        """Returns: self.link"""
        return self.link
    
    def get_pubdate(self):
        """Returns: self.pubdate"""
        return self.pubdate
    
#======================
# Triggers
#======================

class Trigger(ABC):
    """
    Modified from original problem set:\n
    -- Abstract class Trigger now inherits from 'abc'\n
    -- Method 'evaluate' is now an abstract method
    """
    @abstractmethod
    def evaluate(self, newsStory: NewsStory):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        ## I changed it - sorry MIT!

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    """
    Abstract class which takes one string parameter (phrase) to use as a trigger. Inherits from Trigger.
    
    phrase: string
    """
    def __init__(self, phrase: str):
        """
        Calls __init__ method of superclass Trigger.
        
        Sets self.phrase = phrase.lower()
        """
        super().__init__()

        self.phrase = phrase.lower()
    
    def is_phrase_in(self, text: str):
        """
        text: string

        Returns 'True' if self.phrase is present in 'text', otherwise returns 'False'.
        """
        # convert 'text' to lowercase and replace all punctuation with ' '
        stripped_text = ''

        for char in text.lower().strip():
            if char in string.ascii_lowercase or char in string.whitespace:
                stripped_text += char
            elif char in string.punctuation:
                stripped_text += ' '

        # split phrase and stripped_text on any whitespace character
        split_phrase = self.phrase.strip().split()
        split_text = stripped_text.split()

        # if split_text is shorter than split_phrase, then split_phrase cannot be present
        if len(split_phrase) > len(split_text):
            return False
        
        # Search every item of split_text for the first item of split_phrase
        ## If the first item of split_phrase is present and split_phrase has only 1 item, return True
        ## Else if the first item of split_phrase is present, check if the rest of the phrase is present
        for index in range(len(split_text) - len(split_phrase) + 1):    # prevent over indexing on split_text by stopping iteration when the last index in split_phrase lines up with the last index in split_text
            found_first_item = split_text[index] == split_phrase[0]
            
            if found_first_item and len(split_phrase) == 1:
                return True
            elif found_first_item:
                position = index
                found_phrase = True

                # Check if every word in split_phrase is present IN ORDER inside split_text
                ## Break out of the loop early and set found_phrase to False if the split_phrase word does not match the split_text word at the appropriate position
                ## Otherwise, increment our position in split_text and keep checking the words in split_phrase
                for word in split_phrase:
                    if word != split_text[position]:
                        found_phrase = False
                        break
                    position += 1
                
                # If found_phrase is still True, return True
                if found_phrase == True:
                    return True
        
        # The first item of split_phrase was not found in split_text, so return False
        return False

# Problem 3
class TitleTrigger(PhraseTrigger):
    """
    Trigger class which fires when parameter 'phrase' is found in the title of a NewsStory object.
    
    Takes one string parameter (phrase) to use as a trigger. Inherits from PhraseTrigger.
    
    phrase: string
    """
    def __init__(self, phrase: str):
        """
        Calls __init__ method of superclass PhraseTrigger.
        
        Superclass method sets self.phrase = phrase.lower()
        """
        super().__init__(phrase)
    
    def evaluate(self, newsStory: NewsStory):
        """
        newsStory: instance of class NewsStory

        Returns 'True' if self.phrase is present in the title of 'newsStory', otherwise returns 'False'.
        """
        return self.is_phrase_in(newsStory.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase: str):
        """
        Calls __init__ method of superclass PhraseTrigger.
        
        Superclass method sets self.phrase = phrase.lower()
        """
        super().__init__(phrase)
    
    def evaluate(self, newsStory: NewsStory):
        """
        newsStory: instance of class NewsStory

        Returns 'True' if self.phrase is present in the description of 'newsStory', otherwise returns 'False'.
        """
        return super().is_phrase_in(newsStory.get_description())

# TIME TRIGGERS

# Problem 5
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    """
    Abstract class which takes one string parameter (time) to use as a trigger. Inherits from Trigger.
    
    time: string, required format "3 Oct 2016 17:00:10"
    """
    def __init__(self, time: str):
        """
        Calls __init__ method of superclass Trigger.
        
        Converts 'time' to datetime object and assigns to self.time
        """
        super().__init__()

        self.time = datetime.strptime(time, "%d %b %Y %H:%M:%S")
    
    def match_newsstory_timezone(self, newsStory: NewsStory):
        """
        Returns a new datetime object 'matched_time' which takes the value of self.time (datetime) and matches the tzinfo attribute to the tzinfo attribute of parameter 'newsStory'.

        newsStory: instance of class NewsStory

        Returns: datetime object 
        """
        matched_time = self.time
        matched_time = matched_time.replace(tzinfo=newsStory.get_pubdate().tzinfo)
        return matched_time

# Problem 6
class BeforeTrigger(TimeTrigger):
    """
    Trigger class which fires when a NewsStory object is published strictly before the value of the class' self.time attribute.
    
    Takes one string parameter (time) to use as a trigger. Inherits from TimeTrigger.
    
    time: string, required format "3 Oct 2016 17:00:10" in EST
    """
    def __init__(self, time: str):
        """
        Calls __init__ method of superclass TimeTrigger.
        
        Superclass method converts 'time' to datetime object and assigns to self.time
        """
        super().__init__(time)
    def evaluate(self, newsStory: NewsStory):
        """
        newsStory: instance of class NewsStory

        Returns 'True' if NewsStory object is published strictly before the value of the class' self.time attribute, otherwise returns 'False'.
        """
        matched_time = self.match_newsstory_timezone(newsStory)

        return newsStory.get_pubdate() < matched_time

class AfterTrigger(TimeTrigger):
    """
    Trigger class which fires when a NewsStory object is published strictly after the value of the class' self.time attribute.
    
    Takes one string parameter (time) to use as a trigger. Inherits from TimeTrigger.
    
    time: string, required format "3 Oct 2016 17:00:10" in EST
    """
    def __init__(self, time: str):
        """
        Calls __init__ method of superclass TimeTrigger.
        
        Superclass method converts 'time' to datetime object and assigns to self.time
        """
        super().__init__(time)
    def evaluate(self, newsStory: NewsStory):
        """
        newsStory: instance of class NewsStory

        Returns 'True' if NewsStory object is published strictly after the value of the class' self.time attribute, otherwise returns 'False'.
        """
        matched_time = self.match_newsstory_timezone(newsStory)

        return matched_time < newsStory.get_pubdate()

# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    """
    Trigger class which inverts the output of another Trigger object's 'evaluate' method call.
    
    Takes one Trigger parameter (trigger). Inherits from Trigger.
    
    trigger: Trigger
    """
    def __init__(self, trigger: Trigger):
        """
        Calls __init__ method of superclass Trigger.
        
        Method assigns parameter 'trigger' to 'self.trigger'.
        """
        super().__init__()

        self.trigger = trigger
    
    def evaluate(self, newsStory: NewsStory):
        return not self.trigger.evaluate(newsStory)

# Problem 8
# TODO: AndTrigger

# Problem 9
# TODO: OrTrigger


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

