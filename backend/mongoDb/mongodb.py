from __future__ import annotations

import os

import certifi
import motor.motor_asyncio

ca = certifi.where

# Create a new client and connect to the server
client = motor.motor_asyncio.AsyncIOMotorClient(
    os.environ['MONGODB_URI'], tlsCAFile=ca,
)
db = client.book


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print('Pinged your deployment. You successfully connected to MongoDB!')
except Exception as e:
    print(e)
