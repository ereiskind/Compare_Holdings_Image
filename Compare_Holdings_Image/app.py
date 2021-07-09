from tkinter import messagebox
import Compare_Holdings_Image.GUI as GUI

def main():
    messagebox.showinfo(title="Instructions", message="This program uses a sequence of dialog boxes to walk you through using OpenRefine to compare access entitlements lists from Holdings Management (HM) and Alma. Please note that there is an unresolved bug where the program is hanging after dialog boxes that take in data or feature data to be copied; to continue with the program, use the red \"X\" to close the window that remains after one of the dialog box types mentioned previously closes.")

    #Section: Upload the Title Lists to OpenRefine
    messagebox.showinfo(title="Instructions: Upload the HM Title List", message="""
        1. Find the package in HM
        2. Go to the downloads page, select a package download, and select the package
        3. When the status is completed, download the title list
        4. Upload the Excel file that downloaded to OpenRefine
    """)
    HM_project = GUI.RequestProjectNames("HM")

    messagebox.showinfo(title="Instructions: Upload the Alma Title List", message="""
        1. Find the electronic collection in the institution zone
        2. Select the portfolio list
        3. Download an extended export of the portfolio list
        4. Upload the Excel file that downloaded to OpenRefine
    """)
    Alma_project = GUI.RequestProjectNames("Alma")


    #Section: Reformat the Title Lists
    messagebox.showinfo(title="Instructions: Reformat HM Title List", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
    GUI.CreateJSONDisplay('Prepare_HM_Title_List.json')
    messagebox.showinfo(title="Instructions: Reformat Alma Title List", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
    GUI.CreateJSONDisplay('Prepare_Alma_Title_List.json')


    #Section: Find Title Matches in the Two Projects
    #Subsection: Find ISSN Matches
    messagebox.showinfo(title="Instructions: Find ISSN Matches", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
    GUI.CreateJSONDisplay('Find_ISSN_Matches_1.json', HM_project) 
    messagebox.showinfo(title="Instructions: Find ISSN Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
    GUI.CreateJSONDisplay('Find_ISSN_Matches_2.json', Alma_project) 
    if messagebox.askyesno(title="Instructions", message="Switch to the Alma project and set a blanks facet on column \"KBID\". Are there blank rows remaining?"):
        
        #Subsection: Find URL Identifier Matches
        messagebox.showinfo(title="Instructions: Find URL Identifier Matches", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
        GUI.CreateJSONDisplay('Find_URL_Matches_1.json', HM_project)
        messagebox.showinfo(title="Instructions: Find URL Identifier Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
        GUI.CreateJSONDisplay('Find_URL_Matches_2.json', Alma_project)
        if messagebox.askyesno(title="Instructions", message="Switch to the Alma project and set a blanks facet on column \"KBID\". Are there blank rows remaining?"):
            
            #Subsection: Find Remaining Matches via Title Matching
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
            GUI.CreateJSONDisplay('Find_Title_Matches_1.json')
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
            GUI.CreateJSONDisplay('Find_Title_Matches_2.json', HM_project)
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
            GUI.CreateJSONDisplay('Find_Title_Matches_3.json')
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
            GUI.CreateJSONDisplay('Find_Title_Matches_4.json', HM_project)
            messagebox.showinfo(title="Instructions: Find Title Matches", message="""
                1. On \"Portfolio_ID\", set a blanks filter to true, then for each visible record, star the row with the title (and KBID) that matches the portfolio.
                2. Copy the JSONs in the next two dialog boxes and apply them to the Alma project in OpenRefine.
            """) #ToDo: Figure out why last item in Find_Title_Matches_5.json works only when it's the last item in a JSON
            GUI.CreateJSONDisplay('Find_Title_Matches_5.json')
            GUI.CreateJSONDisplay('Find_Title_Matches_6.json')
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
            GUI.CreateJSONDisplay('Find_Title_Matches_7.json', Alma_project)


    #Section: Compare Data for Individual Holdings
    messagebox.showinfo(title="Instructions: Compare Holdings", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
    GUI.CreateJSONDisplay('Compare_Holdings_Data.json', HM_project)
    messagebox.showinfo(title="Instructions: Evaluate Unmatched Titles", message="""
        1. In Alma project, set blanks filter on \"KBID\" to true to find unmatched portfolios
        2. In HM project, set blanks filter on \"Portfolio_ID\" to true to find unmatched titles
    """)