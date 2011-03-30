#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
# Contributor(s): Bob Silverberg <bob.silverberg@gmail.com>
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

Created on Mar 29, 2011

'''

import release_submit_feedback_page


class SubmitIdeaPage(release_submit_feedback_page.ReleaseSubmitFeedbackPage):

    _feedback_locator = 'id=idea-desc'
    _remaining_character_count_locator = 'css=#count-idea-desc'
    _submit_feedback_locator = 'css=#idea .submit span'
    _error_locator = 'css=#idea .submit .errorlist li'

    def go_to_submit_idea_page(self):
        self.selenium.open('/release/feedback#idea')

    @property
    def is_submit_feedback_enabled(self):
        return self.selenium.is_element_present('css=#idea .submit a.disabled') == False

    def submit_feedback(self):
        self.selenium.click(self._submit_feedback_locator)