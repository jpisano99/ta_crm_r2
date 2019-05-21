from datetime import datetime
from my_app.my_secrets import passwords
import os


# database configuration settings
# db_config = dict(
#     DATABASE="jpisano$ta_adoption_db",
#     USER="jpisano",
#     PASSWORD = passwords["DB_PASSWORD"],
#     HOST="127.0.0.1")

db_config = dict(
    DATABASE = "ta_customer_db",
    USER= "root",
    PASSWORD=passwords["DB_PASSWORD"],
    HOST="localhost")

# SSH Tunnel configuration settings
ssh_config = dict(
    ENDPOINT='ssh.pythonanywhere.com',
    USER='jpisano',
    PASSWORD=passwords["SSH_PASSWORD"],
    REMOTE_BIND_ADDRESS='jpisano.mysql.pythonanywhere-services.com',
    REMOTE_BIND_PORT=3306
)


# Smart sheet Config settings
ss_token = dict(
    SS_TOKEN=passwords["SS_TOKEN"]
)


# application predefined constants
app_cfg = dict(
    VERSION=1.0,
    GITHUB="{url}",
    HOME=os.path.expanduser("~"),
    WORKING_DIR='ta_adoption_data',
    UPDATES_DIR='ta_data_updates',
    ARCHIVES_DIR='archives',
    PROD_DATE='',
    UPDATE_DATE='',
    META_DATA_FILE='config_data.json',
    FY17_RAW_BOOKINGS='FY17 TA Master Bookings as of',
    FY18_RAW_BOOKINGS='FY18 TA Master Bookings as of',
    FY19_RAW_BOOKINGS='FY19 TA Master Bookings as of',
    FY19_RAW_RENEWALS='TA Master Renewals as of',
    XLS_RENEWALS='tmp_Master Renewals.xlsx',
    XLS_BOOKINGS='tmp_TA Master Bookings.xlsx',
    XLS_AS_SKUS='tmp_TA AS SKUs.xlsx',
    XLS_CUSTOMER='tmp_TA Customer List.xlsx',
    XLS_ORDER_DETAIL='tmp_TA Order Details.xlsx',
    XLS_ORDER_SUMMARY='tmp_TA Scrubbed Orders.xlsx',
    XLS_BOOKINGS_TRASH='tmp_Bookings Trash.xlsx',
    XLS_DASHBOARD='tmp_TA Unified Adoption Dashboard.xlsx',
    SS_SAAS='SaaS customer tracking',
    SS_CX='CX Tetration Customer Comments v3.0',
    # SS_CX='Tetration Engaged Customer Report',
    SS_AS='Tetration Shipping Notification & Invoicing Status',
    SS_COVERAGE='Tetration Coverage Map',
    SS_SKU='Tetration SKUs',
    SS_CUSTOMERS='TA Customer List',
    SS_DASHBOARD='TA Unified Adoption Dashboard',
    SS_WORKSPACE='Tetration Customer Adoption Workspace',
    AS_OF_DATE=datetime.now().strftime('_as_of_%m_%d_%Y')
)



