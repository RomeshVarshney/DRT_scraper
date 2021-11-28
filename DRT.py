class DRT:
    """
        DRT class
    """

    def __init__(self, diary_no, case_type, case_no, date_of_filling, applicant, respondent, applicant_advocate, respondent_advocate):
        """
            constructor used to initialize the class attributes
        """
        self.diary_no = diary_no
        self.case_type = case_type
        self.case_no = case_no
        self.date_of_filling = date_of_filling
        self.applicant = applicant
        self.respondent = respondent
        self.applicant_advocate = applicant_advocate
        self.respondent_advocate = respondent_advocate
