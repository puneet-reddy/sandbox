#!/usr/bin/env python

"""
@author: puneet.reddy@beyondanalysis.net
@created: 20180605
@blurb: Methods to get an access token for the moneysoft APIs and also some
    some functionality to check and refresh tokens.
"""

import os
import requests
from datetime import (datetime, timedelta)
from urllib.parse import urlencode


class Token:
    def __init__(self, url=os.getenv('ETL_URL', 'https://sandbox.moneysoft.com.au/token'),
                 username=os.getenv('ETL_USERNAME', 'humaniti@beyondanalysis.net'),
                 password=os.getenv('ETL_PASSWORD', 'humaniti1!')):
        """
        @param url (str) - The authentication server endpoint.
        """
        self.auth_url = url
        self.username = username
        self.password = password
        # TODO: Generalize this by moving headers to config with url as key.
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://beyondanalysis.moneysoft.com.au'}
        self._access_token = self._password_grant()

    def __str__(self):
        return str(self._access_token)

    def _parse_time(self, str_time):
        """
        @param: str_time (str) - Time in "%a, %d %b %Y %H:%M:%S %Z" format.
        Parses the expire_time into a datetime object.
        @return: (datetime.datetime) object.
        """
        return datetime.strptime(str_time, "%a, %d %b %Y %H:%M:%S %Z")

    @property
    def access_token(self):
        """
        Access token property. Can't be set explicitly.
        :return:
        """

    @access_token.getter
    def access_token(self):
        """
        Returns an access token which is valid for at least 5 more seconds.
        :return:
        """
        if self._is_expired(self._access_token):
            self._access_token = self._refresh_grant(self._access_token)
        
        return self._access_token

    def _password_grant(self):
        """
        Gets the initial token with a password grant.
        :return: ((str, datetime.datetime) or None) tuple of
            access token, expiry time in UTC or None if failed to acquire.
        """
        try:
            payload = urlencode({
                'grant_type': 'password',
                # TODO: Secure these.
                'username': self.username,
                'password': self.password
            })

            response = requests.request(
                "POST", self.auth_url, data=payload, headers=self.headers)
            if not response.ok:
                # TODO: Log an error here.
                return

            res = response.json()
            a_token = res.get('access_token')
            r_token = res.get('refresh_token')
            lifetime = res.get('expires_in')
            # expiry = self._parse_time(res.get('.expires'))
            # Ignoring the timestamp on the response since the both servers
            # may not be in sync.
            expiry = datetime.utcnow() + timedelta(seconds=int(lifetime))

            return a_token, r_token, expiry

        except (requests.RequestException, ConnectionError) as err:
            # TODO: Log error & stack trace here.
            return

    def _refresh_grant(self, access_token):
        """
        @param: access_token (str, str, datetime.datetime) - A token tuple 
            containing access_token, refresh_token and expiry datetime.
        Attempts to get a new token using the refresh token. If it fails, a
        password type grant is attempted instead.
        @return: (str, str, datetime.datetime) - Same as access_token
        """
        new_token = None

        try:
            refresh_payload = urlencode({
                'grant_type': 'refresh_token',
                'refresh_token': access_token[1]
            })
            response = requests.request("POST", self.auth_url,
                                        data=refresh_payload, headers=self.headers)
            if not response.ok:
                raise(Exception(response.text))
            res = response.json()
            new_token = (
                res['access_token'],
                res['refresh_token'],
                datetime.utcnow() + timedelta(seconds=int(res['expires_in'])))
        except (
                requests.RequestException, ConnectionError, AttributeError) as err:
            # TODO: Logging
            new_token = self._password_grant()

        return new_token

    def _is_expired(self, token):
        """
        @param: token (str, str, datetime.datetime) - A token tuple containing 
            access_token, refresh_token and expiry datetime.
        @return (bool) False if less than 5 seconds to expiry otherwise True
        """
        expired = True
        try:
            expired = (token[2] - datetime.utcnow()).total_seconds() < 5
        except:
            # Intentional supression of error since we can try to get a new token.
            # TODO: Log the error.
            pass
        return expired

    def validity(self):
        """
        :return (int) Number of seconds for which this token is still valid.
        """
        return (self._access_token[2] - datetime.utcnow()).total_seconds()


if __name__ == '__main__':
    # Some very simple tests.
    x = Token()
    print(x)
    print(x.validity())
    print(x.access_token)
