from flask import Flask, render_template, request
import requests
import os

def get_mongo_db():
    url = PRIMARY_CONNECTION_STRING_DB
    