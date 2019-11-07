from googleapiclient.discovery import build
import database_connection as db


def google_search(search_term, api_key, cse_id, user, **kwargs):
    """"
    Function to search keyword on google, return the search links and store search keywords in db.
    """
    results =[]
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    for result in  res['items']:
        results.append(result["link"])

    # search keyword insertion in database    
    conn = db.create_connection()
    with conn:
        cursor = conn.cursor()
        insert_sql_query ="insert into search_history values(%s,%s)"
        cursor.execute(insert_sql_query, (user,search_term))

    return results


def get_history(history_keyword,user):
    """
    Function to return user search history.
    """
    conn = db.create_connection()
    with conn:
        cursor = conn.cursor()
        username="'"+user+"'"
        keyword = "%" + history_keyword + "%"
        sql = "select search_keyword from search_history where user=%s and lower(search_keyword) like lower('%s')"%(username,keyword)
        cursor.execute(sql)
        results = cursor.fetchall()
        if results:
            total_hisotry =set([row[0] for row in results])
        else:
            total_hisotry = 'No such item found'
        return total_hisotry
