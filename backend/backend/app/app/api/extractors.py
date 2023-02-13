import time
import json
import urllib
from typing import List
import validators
from pydantic import EmailStr
import requests
from fastapi import HTTPException
from neo4j._sync import work
from app.core.logger import get_logger
from app.api.deps import get_gdb
from app.neomodels.google import GoogleSearch, GoogleResult, get_google_search_results
from app.api.utils import find_emails, to_clean_domain
from selenium.webdriver.common.by import By


logger = get_logger(name=" app.api.extractors ")

    
def get_google_results(gdb: work.Session, query: str, pages: int = 3, force_search: str = False):
    existing_results = gdb.execute_read(
        get_google_search_results,
        search_query=query,
        pages=pages
    )

    if len(existing_results) != 0 and force_search is False:
        return list({v['url']: v for v in existing_results}.values())
    
    if not query:
        raise Exception("queryRequired")
    
    try:
        logger.info(f'query -- {query}')
        google_resp = requests.get((
            'http://microservice:1323/google?'
            f'query={query}&pages={pages}'
        ))
        google_results = google_resp.json()
    except Exception:
        raise Exception("crawlGoogleError")
    
    stats = google_results.get('stats')
    related_searches = []
    result_stats = []
    if stats is not None:
        for stat in stats:
            if res := stat.get('result'):
                result_stats = result_stats + res
            if related := stat.get('related'):
                related_searches = related_searches + related

    search_node = GoogleSearch(
        search_query=query,
        pages=pages,
        related_searches=related_searches,
        result_stats=result_stats
    ).save()

    for key in list(google_results.keys()):
        if key is not None and key != 'stats':
            if google_results.get(key):
                for result in google_results.get(key):
                    result_node = GoogleResult(
                        title=result.get('title', None),
                        description=result.get('description', None),
                        url=result.get('link', None),
                        breadcrumb=result.get('breadcrumb', None),
                        question=result.get('question', None),
                        result_type=key
                    ).save()
                    search_node.results.connect(result_node)
    search_node.save()
    return gdb.execute_read(get_google_search_results, search_query=query, pages=int(pages))


def get_emails_from_google(gdb: work.Session, domain: str = None, pages: int = 12):
    if not domain:
        raise Exception("domainRequired")

    emails_query = 'intext:"@' + to_clean_domain(domain) + '"'

    try:
        results = get_google_results(gdb, emails_query, pages)
    except Exception as e:
        logger.error(e)
        raise Exception("crawlGoogleError")

    emails = []
    # logger.info(json.dumps(results, indent=2))
    for result in results:
        compare = result.get("title", "") + " " + result.get("description", "")
        emails = emails + find_emails(compare)
    return emails


def get_emails_from_url(driver, url: str = None) -> List[EmailStr]:
    emails = []
    try:
        driver.get(url)
        time.sleep(3)
        for elm in driver.find_elements(by=By.TAG_NAME, value="a"):
            href = elm.get_attribute("href")
            href = href.replace("mailto:", "")
            if validators.email(href):
                emails.append(href)
        
        tags = ["button", "h1", "h2", "h3", "h4", "h5", "h6", "p", "span"]
        
        for tag in tags:
            elements = driver.find_elements(by=By.TAG_NAME, value=tag)
            for elm in elements:
                emails = emails + find_emails(elm.text)
                if elm.text and validators.email(str(elm.text)):
                    emails.append(str(elm.text)) 
                    
        return list(set(emails)) 
    
    except Exception as e:
        logger.error(f"Error fetching Emails for page: {url} - {e}")
        return emails