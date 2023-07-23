import asyncio
import json
from pathlib import Path
from enviroment import EMAIL, PASSWORD
from models_zumbu.login import Login
from models_playwright.cookies import Cookies
from models_playwright.browser import Browser
from models_playwright.context import Context
from constants import BASE_URL, ZUMBU
from interceptors.interceptors import Interceptor