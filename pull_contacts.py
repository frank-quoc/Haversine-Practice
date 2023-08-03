from hubapi import get_all_records_with_property
from pprint import pprint

def migrate_contacts_from_hubspot():
    """Method that uses _migrate_obj_from_hubspot to migrate contacts from HubSpot."""
    
    props = [
        "firstname", 
        "form___first_name",
        "zoom_webinar___first_name",
        "lastname", 
        "form___last_name",
        "zoom_webinar___last_name",
        "email", 
        "work_email",
        "phone", 
        "mobilephone",
        "form___phone_number",
        "hs_whatsapp_phone_number",
        "zoom_webinar___phone_number",
        "jobtitle", 
        "form___job_title",
        "zoom_webinar___job_title",
        "job_function",
        "company", 
        "form___company_name",
        "zoom_webinar___company_name",
        "company_size", 
        "company_size__zoominfo_",
        "employee_size_zoom",
        "numemployees",
        "personal_state", 
        "state",
        "state__u_s__",
        "personal_city", 
        "city",
        "form___city",
        "zoom_webinar___city",
        "personal_zip_code", 
        "zip",
        "industry",
        "primary_industry",
    ]
    df = get_all_records_with_property('contacts', props)
    print(df.head())
    df.to_csv(index=False)
    
migrate_contacts_from_hubspot()