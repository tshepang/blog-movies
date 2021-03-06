#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

site = {
    'name': 'Tshepang logs - movies',
    'url': 'http://movies.tshepang.net',
}

output = '.output'
config = {
    'source': 'content',
    'output': output,
    'static': os.path.join(output, 'static'),
    'static_prefix': '/static/',
    'permalink': '{{clean_title}}',
    'perpage': 1000,
    'feedcount': 1000,
    'timezone': '+02:00',
}

author = {
    'default': 'tshepang',
    'vars': {
        'tshepang': {
            'name': 'Tshepang Lekhonkhobe',
        }
    }
}


# theme variables are defined by theme creator
theme = {
    'vars': {
        'disqus': 'tshepanglogs',
        'analytics': 'UA-16685250-3',
        'navigation': [
            {'name': 'main blog', 'link': 'http://tshepang.net'},
            {'name': 'key-posts', 'link': '/key-posts'},
            {'name': 'about-me', 'link': 'http://tshepang.net/about-me'},
        ]
    }
}

reader = {
    'active': [
        'custom.MyReader',
    ],
    'vars': {
        'post_class': 'custom.MyPost',
    }
}

writer = {
    "active": [
        "liquidluck.writers.core.PostWriter",
        "liquidluck.writers.core.PageWriter",
        "liquidluck.writers.core.ArchiveWriter",
        "liquidluck.writers.core.ArchiveFeedWriter",
        "liquidluck.writers.core.FileWriter",
        "liquidluck.writers.core.StaticWriter",
        "liquidluck.writers.core.YearWriter",
        "liquidluck.writers.core.CategoryWriter",
        "liquidluck.writers.core.CategoryFeedWriter",
        "liquidluck.writers.core.TagWriter",
        "liquidluck.writers.core.TagCloudWriter",
    ],
}
