# -*- coding: utf-8 -*-
# Copyright (C) 2018 boslab.org
# Licensed under the MIT License.
# Created   : 14/Jan/2018 18:35
# @Poject   : boslab
# @AUTHOR   : Francis G. Lee
# Email     : francis@boslab.org

from __future__ import print_function  # Use print() instead of print
from flask import url_for


def test_page_urls(client):
    # Visit home page
    response = client.get(url_for('main.home_page'), follow_redirects=True)
    assert response.status_code==200

    # Login as user and visit User page
    response = client.post(url_for('user.login'), follow_redirects=True,
                           data=dict(email='user@example.com', password='Password1'))
    assert response.status_code==200
    response = client.get(url_for('main.member_page'), follow_redirects=True)
    assert response.status_code==200

    # Edit User Profile page
    response = client.get(url_for('main.user_profile_page'), follow_redirects=True)
    assert response.status_code==200
    response = client.post(url_for('main.user_profile_page'), follow_redirects=True,
                           data=dict(first_name='User', last_name='User'))
    response = client.get(url_for('main.member_page'), follow_redirects=True)
    assert response.status_code==200

    # Logout
    response = client.get(url_for('user.logout'), follow_redirects=True)
    assert response.status_code==200

    # Login as admin and visit Admin page
    response = client.post(url_for('user.login'), follow_redirects=True,
                           data=dict(email='admin@example.com', password='Password1'))
    assert response.status_code==200
    response = client.get(url_for('main.admin_page'), follow_redirects=True)
    assert response.status_code==200

    # Logout
    response = client.get(url_for('user.logout'), follow_redirects=True)
    assert response.status_code==200
