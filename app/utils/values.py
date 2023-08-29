#!/usr/bin/python
# app/utils/values.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2023 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Upload details for the metadata file.
UPLOAD = [
    'file_path',
    'nft_name',
    'external_link',
    'description',
    'collection',
    'properties',
    'levels',
    'stats',
    'unlockable_content',
    'explicit_and_sensitive_content',
    'supply',
    'blockchain'
]

# Sale details for the metadata file.
SALE = [
    'nft_url',
    'supply',
    'blockchain',
    'sale_type',
    'price',
    'method',
    'duration',
    'specific_buyer',
    'quantity'
]

# Upload and sale details for the metadata file.
# Contains all the upload details and the sale
# details without "nft_url", "supply" and "blockchain".
UPLOAD_AND_SALE = UPLOAD + SALE[3:]
