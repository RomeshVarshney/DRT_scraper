import sqlite3
from DRT import DRT

# creating SQLite3 connection
conn = sqlite3.connect('drt.db')
c = conn.cursor()

def save_DRT(DRT):
    """
        saves the information in the database
    """
    
    c.execute("CREATE TABLE IF NOT EXISTS DRT(diary_no text, case_type text, case_no text, date_of_filling date, applicant text, respondent text, applicant_advocate text, respondent_advocate text)")
    with conn:
        query = "INSERT INTO DRT VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            DRT.diary_no, DRT.case_type, DRT.case_no, DRT.date_of_filling, DRT.applicant.strip(), 
            DRT.respondent.strip(), DRT.applicant_advocate.strip(), DRT.respondent_advocate.strip()
        )
        c.execute(query)

def get_all_drts():
    c.execute("SELECT * FROM DRT")
    return c.fetchall()