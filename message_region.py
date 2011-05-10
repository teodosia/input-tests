#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Firefox Input.
#
# The Initial Developer of the Original Code is
# Mozilla Corp.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Dave Hunt <dhunt@mozilla.com>
#                 Teodosia Pop <teodosia.pop@softvision.ro>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
'''
Created on Mar 28, 2011
'''
from vars import ConnectionParameters

page_load_timeout = ConnectionParameters.page_load_timeout

class Message(object):

    _type_locator = " .type"
    _body_locator = " .body"
    _time_locator = " time"
    _platform_locator = " .meta li:nth(1)"
    _locale_locator = " .meta li:nth(2)"
    _site_locator = " .meta li:nth(3)"
    _more_options_locator = " .options"
    _copy_user_agent_locator = " .options .copy_ua"
    _copy_user_agent_locator = " .options .copy_ua"
    _translate_message_locator = " li:nth(1) a"
    _tweet_this_locator = " .options .twitter"

    _platform_link_locator = "//div[@id='messages']/ul/li/ul/li[2]/a"
    _locale_link_locator = "//div[@id='messages']/ul/li/ul/li[3]/a"
   
    def __init__(self, selenium, index):
        self.selenium = selenium
        self.index = index

    def click_platform_link(self):
        self.selenium.click(self._platform_link_locator)
        self.selenium.wait_for_page_to_load(page_load_timeout)
        
    def click_locale_link(self):
        self.selenium.click(self._locale_link_locator)
        self.selenium.wait_for_page_to_load(page_load_timeout)
    
    def click_timestamp_link(self):
        self.selenium.click(self._time_locator)
        self.selenium.wait_for_page_to_load(page_load_timeout)
    
    def is_platform_visble(self):
        """
        Returns True if the platform in an individual theme page is visible
        """
        platforms = ("Mac OS X, Windows 7, Windows XP, Windows Vista, Linux, Android, Maemo")
        return platforms.find(self.platform) > -1

    def is_language_visible(self):
        """
        Returns True if the language in an individual theme page is visible
        """
        language = ("English (US), Spanish, English (British), Portuguese (Brazilian)" +
                    "German, French, Russian, Italian, Polish, Turkish, Hungarian")
        return language.find(self.locale) > -1
    
    def platform_goes_to_product_filter(self, filter, platform):
        platforms = {"Windows 7" : 1, 
                     "Windows XP": 2,
                     "Windows Vista" : 3,
                     "Linux" : 4,
                     "Mac OS X": 5,
                     "Android": 6,
                     "Maemo" : 7}
        filters = {"win7" : 1, 
                   "winxp": 2,
                   "vista" : 3,
                   "linux" : 4,
                   "mac": 5,
                   "android": 6,
                   "maemo" : 7}
        return platforms[platform] == filters[filter]
    
    def language_goes_to_locale_filter(self, language, locale):
        languages = {"English (US)": 1,
                     "Spanish": 2,
                     "English (British)": 3,
                     "Portuguese (Brazilian)": 4,
                     "German": 5,
                     "French": 6,
                     "Russian": 7,
                     "Italian": 8,
                     "Polish:": 9,
                     "Turkish": 10,
                     "Hungarian": 11}
        locales = {"en-US": 1,
                   "es": 2,
                   "en-GB": 3,
                   "pt-BR": 4,
                   "de": 5,
                   "fr": 6,
                   "ru": 7,
                   "it": 8,
                   "pl": 9,
                   "tr": 10,
                   "hu": 11}
        return languages[language] == locales[locale]
    
    def absolute_locator(self, relative_locator):
        return self.root_locator + relative_locator    
           
    @property
    def root_locator(self):
        return "css=#messages .message:nth(" + str(self.index - 1) + ")"

    @property
    def type(self):
        return self.selenium.get_text(self.absolute_locator(self._type_locator))

    @property
    def body(self):
        return self.selenium.get_text(self.absolute_locator(self._body_locator).encode('utf-8'))

    @property
    def time(self):
        return self.selenium.get_text(self.absolute_locator(self._time_locator))

    @property
    def platform(self):
        return self.selenium.get_text(self.absolute_locator(self._platform_locator))
    
    @property
    def platform_link(self):
        return self.selenium.get_value(self.absolute_locator(self._platform_locator))
        
    @property
    def locale(self):
        return self.selenium.get_text(self.absolute_locator(self._locale_locator))

    @property
    def site(self):
        return self.selenium.get_text(self.absolute_locator(self._site_locator))
