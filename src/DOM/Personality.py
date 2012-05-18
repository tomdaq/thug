#!/usr/bin/env python
#
# Personality.py
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA

import logging
log = logging.getLogger("Thug")

class Personality(dict):
    def __init__(self):
        # Windows XP personalities
        self['xpie60'] = {
                "id"              : 1,
                "description"     : "Internet Explorer 6.0 (Windows XP)",
                "userAgent"       : "Mozilla/4.0 (Windows;  MSIE 6.0;  Windows NT 5.1;  SV1; .NET CLR 2.0.50727)",
                "appCodeName"     : "Mozilla",
                "appName"         : "Microsoft Internet Explorer",
                "appVersion"      : "4.0 (Windows;  MSIE 6.0;  Windows NT 5.1;  SV1; .NET CLR 2.0.50727)",
                "appMinorVersion" : ";SP2;",
                "platform"        : "Win32",
                "browserTag"      : "ie60",
                }

        self['xpie61'] = { 
                "id"              : 2,
                "description"     : "Internet Explorer 6.1 (Windows XP)", 
                "userAgent"       : "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "appCodeName"     : "Mozilla",
                "appName"         : "Microsoft Internet Explorer",
                "appVersion"      : "4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "appMinorVersion" : ";SP2;",
                "platform"        : "Win32",
                "browserTag"      : "ie61",
                }

        self['xpie70'] = {
                "id"              : 3,
                "description"     : "Internet Explorer 7.0 (Windows XP)",
                "userAgent"       : "Mozilla/4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
                "appCodeName"     : "Mozilla",
                "appName"         : "Microsoft Internet Explorer",
                "appVersion"      : "4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
                "appMinorVersion" : ";SP2;",
                "platform"        : "Win32",
                "browserTag"      : "ie70",
                }

        self['xpie80'] = {
                "id"              : 4,
                "description"     : "Internet Explorer 8.0 (Windows XP)",
                "userAgent"       : "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; (R1 1.5); .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "appCodeName"     : "Mozilla",
                "appName"         : "Microsoft Internet Explorer",
                "appVersion"      : "4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; (R1 1.5); .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "appMinorVersion" : ";SP2;",
                "platform"        : "Win32",
                "browserTag"      : "ie80",
                }

        # Windows 2000 personalities
        self['w2kie60'] = {
                "id"              : 5,
                "description"     : "Internet Explorer 6.0 (Windows 2000)",
                "userAgent"       : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "appCodeName"     : "Mozilla",
                "appName"         : "Microsoft Internet Explorer",
                "appVersion"      : "4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "appMinorVersion" : ";SP2;",
                "platform"        : "Win32",
                "browserTag"      : "ie60",
                }

        self['w2kie80'] = {
                "id"              : 6,
                "description"     : "Internet Explorer 8.0 (Windows 2000)",
                "userAgent"       : "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)",
                "appCodeName"     : "Mozilla",
                "appName"         : "Microsoft Internet Explorer",
                "appVersion"      : "5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)",
                "appMinorVersion" : ";SP2;",
                "platform"        : "Win32",
                "browserTag"      : "ie80",
                }

    def isIE(self):
        return self[log.ThugOpts.useragent]['appName'] == "Microsoft Internet Explorer"

    def isFirefox(self):
        return self[log.ThugOpts.useragent]['appName'] == "Netscape"
