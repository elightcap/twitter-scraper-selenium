#!/usr/bin/env python3
try:
    from selenium.common.exceptions import NoSuchElementException
    from .scraping_utils import Scraping_utilities
    from .driver_utils import Utilities
    import sys
    import urllib.request
    import re
    from inspect import currentframe
    from .scraping_utilities import Scraping_utlities
    from dateutil.parser import parse
except Exception as ex:
    frameinfo = currentframe()
    print("Error on line no. {} : {}".format(frameinfo.f_lineno,ex))

frameinfo = currentframe()

class Finder:
  """
  this class should contain all  the static method to find that accept
  webdriver instance and perform operation to find elements and return the
  found element.
  method should follow convention like so:

  @staticmethod
  def __method_name(parameters):
  """

  @staticmethod
  def __find_name(driver) -> str:
    try:
      name = name = driver.title
      name = Scraping_utlities._Scraping_utlities__parse_name(name)
      return name
    except Exception as ex:
      print("Error at method find_name on line no. {} : {}".format(frameinfo.f_lineno, ex))

  @staticmethod
  def __fetch_all_tweets(driver):
    try:
      return driver.find_elements_by_css_selector('div[data-testid="tweet"]')
    except:
      print("Error at method find_all_tweets on line no. {} : {}".format(frameinfo.f_lineno, ex))

  @staticmethod
  def __find_replies(tweet):
    try:
      replies = tweet.find_element_by_css_selector('div[data-testid="reply"]')
      if replies.text == "":
        return 0
      else:
        return int(Scraping_utlities._Scraping_utlities__value_to_float(replies.text))
    except Exception as ex:
      print("Error at method find_replies on line no. {} : {}".format(frameinfo.f_lineno, ex))
      return ""

  @staticmethod
  def __find_shares(tweet):
    try:
      shares = tweet.find_element_by_css_selector('div[data-testid="retweet"]')
      if shares.text == "":
        return 0
      else:
        return int(Scraping_utlities._Scraping_utlities__value_to_float(shares.text))
    except Exception as ex:
      print("Error at method find_shares on line no. {} : {}".format(frameinfo.f_lineno, ex))
      return ""

  @staticmethod
  def __find_status(tweet):
    try:
      anchors = Finder.__find_all_anchor_tags(tweet)
      status = "NA"
      if len(anchors) > 2:
        status = anchors[2].get_attribute("href").split("/")
      return status
    except Exception as ex:
      print("Error at method find_status on line no. {} : {}".format(frameinfo.f_lineno, ex))
      return []

  @staticmethod
  def __find_all_anchor_tags(tweet):
    try:
      return tweet.find_elements_by_tag_name('a')
    except Exception as ex:
      print("Error at method find_all_anchor_tags on line no. {} : {}".format(
          frameinfo.f_lineno, ex))

  @staticmethod
  def __find_timestamp(tweet):
    try:
      timestamp = tweet.find_element_by_tag_name(
          "time").get_attribute("datetime")
      posted_time = parse(timestamp).isoformat()
      return posted_time
    except Exception as ex:
      print("Error at method find_all_anchor_tags on line no. {} : {}".format(
          frameinfo.f_lineno, ex))


  @staticmethod
  def __find_content(tweet):
    try:
      content_element = tweet.find_elements_by_xpath('.//*[@dir="auto"]')[4]
      return content_element.text
    except Exception as ex:
      print("Error at method find_all_anchor_tags on line no. {} : {}".format(
          frameinfo.f_lineno, ex))

  @staticmethod
  def __find_like(tweet):
    try:
      like_element = tweet.find_element_by_css_selector('div[data-testid="like"]')
      if like_element.text == "":
        return 0
      else:
        return int(Scraping_utlities._Scraping_utlities__value_to_float(like_element.text))
    except Exception as ex:
      print("Error at method find_all_anchor_tags on line no. {} : {}".format(
          frameinfo.f_lineno, ex))
  @staticmethod
  def __find_images(tweet):
    try:
      image_element = tweet.find_elements_by_css_selector(
          'div[data-testid="tweetPhoto"]')
      images = []
      for image_div in image_element:
        href = image_div.find_element_by_tag_name("img").get_attribute("src")
        images.append(href)
      return images
    except Exception as ex:
      print("Error at method find_all_anchor_tags on line no. {} : {}".format(
          frameinfo.f_lineno, ex))

  @staticmethod
  def __find_videos(tweet):
    try:
      image_element = tweet.find_elements_by_css_selector(
          'div[data-testid="videoPlayer"]')
      videos = []
      for video_div in image_element:
        href = video_div.find_element_by_tag_name("video").get_attribute("src")
        videos.append(href)
      return videos
    except Exception as ex:
      print("Error at method find_all_anchor_tags on line no. {} : {}".format(
          frameinfo.f_lineno, ex))

