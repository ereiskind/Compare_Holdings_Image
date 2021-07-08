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
    #ToDo: GUI.CreateJSONDisplay with f-string plus Find_ISSN_Matches_1.json
    """
    [
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "All ISSN",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"ISSN\\\").cells.KBID.value.uniques().join(\\\"|\\\")",
            "onError": "set-to-blank",
            "newColumnName": "KBID",
            "columnInsertIndex": 1,
            "description": "Create column ``KBID`` with the KBID for the ISSN in that row with multiples separated by pipes"
        }}
    ]
    """
    messagebox.showinfo(title="Instructions: Find ISSN Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
    #ToDo: GUI.CreateJSONDisplay with f-string plus Find_ISSN_Matches_2.json
    """
    [
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{Alma_project}\\\",\\\"KBID\\\").cells.Portfolio_ID.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "Portfolio_ID",
            "columnInsertIndex": 1,
            "description": "Create column ``Portfolio_ID`` with the portfolio ID matched to the record's KBID"
        }}
    ]
    """
    if messagebox.askyesno(title="Instructions", message="Switch to the Alma project and set a blanks facet on column \"KBID\". Are there blank rows remaining?"):
        #Subsection: Find URL Identifier Matches
        messagebox.showinfo(title="Instructions: Find URL Identifier Matches", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
        #ToDo: GUI.CreateJSONDisplay with Find_URL_Matches_1.json, f-string, Find_URL_Matches_2.json
        """
        [
            {{
                "op": "core/column-addition",
                "engineConfig": {{
                    "facets": [
                        {{
                            "type": "list",
                            "name": "KBID",
                            "expression": "isBlank(value)",
                            "columnName": "KBID",
                            "invert": false,
                            "omitBlank": false,
                            "omitError": false,
                            "selection": [
                                {{
                                    "v": {{
                                        "v": true,
                                        "l": "true"
                                    }}
                                }}
                            ],
                            "selectBlank": false,
                            "selectError": false
                        }}
                    ],
                    "mode": "record-based"
                }},
                "baseColumnName": "URL_Identifier",
                "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"URL\\\").cells.KBID.value.uniques().join(\\\"|\\\")",
                "onError": "set-to-blank",
                "newColumnName": "URL_Match",
                "columnInsertIndex": 2,
                "description": "Create column ``URL_Match`` with all of the the KBIDs matching the record's ``URL_Identifier`` value for those records that don't already have a KBID match"
            }}
        ]
        """
        messagebox.showinfo(title="Instructions: Find URL Identifier Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
        #ToDo: GUI.CreateJSONDisplay with f-string plus Move_Data_From_Temp.json
        """
        [
            {{
                "op": "core/column-addition",
                "engineConfig": {{
                    "facets": [
                        {{
                            "type": "list",
                            "name": "Portfolio_ID",
                            "expression": "isBlank(value)",
                            "columnName": "Portfolio_ID",
                            "invert": false,
                            "omitBlank": false,
                            "omitError": false,
                            "selection": [
                                {{
                                    "v": {{
                                        "v": true,
                                        "l": "true"
                                    }}
                                }}
                            ],
                            "selectBlank": false,
                            "selectError": false
                        }}
                    ],
                    "mode": "record-based"
                }},
                "baseColumnName": "KBID",
                "expression": "grel:cell.cross(\\\"{Alma_project}\\\",\\\"KBID\\\").cells.Portfolio_ID.value.uniques().join(\\\"|\\\")",
                "onError": "set-to-blank",
                "newColumnName": "temp",
                "columnInsertIndex": 1,
                "description": "For records without portfolio IDs, create column ``temp`` with all the portfolio IDs matching the KBID separated by pipes"
            }}
        ]
        """
        if messagebox.askyesno(title="Instructions", message="Switch to the Alma project and set a blanks facet on column \"KBID\". Are there blank rows remaining?"):
            #Subsection: Find Remaining Matches via Title Matching
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
            GUI.CreateJSONDisplay('Find_Title_Matches_1.json')
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
            #ToDo: GUI.CreateJSONDisplay with Find_Title_Matches_2.json, f-string, Find_Title_Matches_3.json
            """
            [
                {{
                    "op": "core/column-addition",
                    "engineConfig": {{
                        "facets": [],
                        "mode": "record-based"
                    }},
                    "baseColumnName": "Title",
                    "expression": "grel:split(if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles\\\").cells.KBID.value),\\\"\\\",cell.cross(\\\"{HM_project}\\\",\\\"All_Titles\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_1\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_1\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_1\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_1\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_2\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_2\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_2\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_2\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_3\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_3\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_4\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value.join(\\\"|\\\")),\\\"|\\\").uniques().join(\\\"|\\\")",
                    "onError": "set-to-blank",
                    "newColumnName": "Title_KBID",
                    "columnInsertIndex": 4,
                    "description": "Create column ``Title_KBID`` by matching the value in ``Title`` to one of the title values in the HM project"
                }},
                {{
                    "op": "core/text-transform",
                    "engineConfig": {{
                        "facets": [],
                        "mode": "record-based"
                    }},
                    "columnName": "All_1",
                    "expression": "grel:split(if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_1\\\").cells.KBID.value),\\\"\\\",cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_1\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_1\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_1\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_2\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_2\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_2\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_2\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_3\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_3\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_4\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value.join(\\\"|\\\")),\\\"|\\\").uniques().join(\\\"|\\\")",
                    "onError": "keep-original",
                    "repeat": false,
                    "repeatCount": 10,
                    "description": "Change the value in column ``All_1`` to the KBID(s) of all exactly matching titles at the given or greater level of modification"
                }},
                {{
                    "op": "core/text-transform",
                    "engineConfig": {{
                        "facets": [],
                        "mode": "record-based"
                    }},
                    "columnName": "Alt_1",
                    "expression": "grel:split(if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_1\\\").cells.KBID.value),\\\"\\\",cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_1\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_2\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_2\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value.join(\\\"|\\\")),\\\"|\\\").uniques().join(\\\"|\\\")",
                    "onError": "keep-original",
                    "repeat": false,
                    "repeatCount": 10,
                    "description": "Change the value in column ``Alt_1`` to the KBID(s) of all exactly matching titles at the given or greater level of modification"
                }},
                {{
                    "op": "core/text-transform",
                    "engineConfig": {{
                        "facets": [],
                        "mode": "record-based"
                    }},
                    "columnName": "All_2",
                    "expression": "grel:split(if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_2\\\").cells.KBID.value),\\\"\\\",cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_2\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_2\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_2\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_3\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_3\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_4\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value.join(\\\"|\\\")),\\\"|\\\").uniques().join(\\\"|\\\")",
                    "onError": "keep-original",
                    "repeat": false,
                    "repeatCount": 10,
                    "description": "Change the value in column ``All_2`` to the KBID(s) of all exactly matching titles at the given or greater level of modification"
                }},
                {{
                    "op": "core/text-transform",
                    "engineConfig": {{
                        "facets": [],
                        "mode": "record-based"
                    }},
                    "columnName": "Alt_2",
                    "expression": "grel:split(if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_2\\\").cells.KBID.value),\\\"\\\",cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_2\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value.join(\\\"|\\\")),\\\"|\\\").uniques().join(\\\"|\\\")",
                    "onError": "keep-original",
                    "repeat": false,
                    "repeatCount": 10,
                    "description": "Change the value in column ``Alt_2`` to the KBID(s) of all exactly matching titles at the given or greater level of modification"
                }},
                {{
                    "op": "core/text-transform",
                    "engineConfig": {{
                        "facets": [],
                        "mode": "record-based"
                    }},
                    "columnName": "All_3",
                    "expression": "grel:split(if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_3\\\").cells.KBID.value),\\\"\\\",cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_3\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_4\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value.join(\\\"|\\\")),\\\"|\\\").uniques().join(\\\"|\\\")",
                    "onError": "keep-original",
                    "repeat": false,
                    "repeatCount": 10,
                    "description": "Change the value in column ``All_3`` to the KBID(s) of all exactly matching titles at the given or greater level of modification"
                }},
                {{
                    "op": "core/text-transform",
                    "engineConfig": {{
                        "facets": [],
                        "mode": "record-based"
                    }},
                    "columnName": "Alt_3",
                    "expression": "grel:split(if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value),\\\"\\\",cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_3\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value.join(\\\"|\\\")),\\\"|\\\").uniques().join(\\\"|\\\")",
                    "onError": "keep-original",
                    "repeat": false,
                    "repeatCount": 10,
                    "description": "Change the value in column ``Alt_3`` to the KBID(s) of all exactly matching titles at the given or greater level of modification"
                }},
                {{
                    "op": "core/text-transform",
                    "engineConfig": {{
                        "facets": [],
                        "mode": "record-based"
                    }},
                    "columnName": "All_4",
                    "expression": "grel:split(if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_4\\\").cells.KBID.value),\\\"\\\",cell.cross(\\\"{HM_project}\\\",\\\"All_Titles_4\\\").cells.KBID.value.join(\\\"|\\\"))+if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value),\\\"\\\",\\\"|\\\"+cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value.join(\\\"|\\\")),\\\"|\\\").uniques().join(\\\"|\\\")",
                    "onError": "keep-original",
                    "repeat": false,
                    "repeatCount": 10,
                    "description": "Change the value in column ``All_4`` to the KBID(s) of all exactly matching titles at the given or greater level of modification"
                }},
                {{
                    "op": "core/text-transform",
                    "engineConfig": {{
                        "facets": [],
                        "mode": "record-based"
                    }},
                    "columnName": "Alt_4",
                    "expression": "grel:split(if(isNull(cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value),\\\"\\\",cell.cross(\\\"{HM_project}\\\",\\\"Alt_Titles_4\\\").cells.KBID.value.join(\\\"|\\\")),\\\"|\\\").uniques().join(\\\"|\\\")",
                    "onError": "keep-original",
                    "repeat": false,
                    "repeatCount": 10,
                    "description": "Change the value in column ``Alt_4`` to the KBID(s) of all exactly matching titles at the given or greater level of modification"
                }}
            ]
            """
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
            GUI.CreateJSONDisplay('Find_Title_Matches_4.json')
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
            #ToDo: GUI.CreateJSONDisplay with f-string
            """
            [
                {{
                    "op": "core/column-addition",
                    "engineConfig": {{
                        "facets": [
                            {{
                                "type": "list",
                                "name": "Temp",
                                "expression": "grel:isNumeric(value)",
                                "columnName": "Temp",
                                "invert": false,
                                "omitBlank": false,
                                "omitError": false,
                                "selection": [
                                    {{
                                        "v": {{
                                            "v": true,
                                            "l": "true"
                                        }}
                                    }}
                                ],
                                "selectBlank": false,
                                "selectError": false
                            }}
                        ],
                        "mode": "record-based"
                    }},
                    "baseColumnName": "Temp",
                    "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.All_Titles.value[0]",
                    "onError": "set-to-blank",
                    "newColumnName": "Temp_Titles",
                    "columnInsertIndex": 2,
                    "description": "Create column ``Temp_Titles`` with the HM title options for the row's KBID"
                }}
            ]
            """
            messagebox.showinfo(title="Instructions: Find Title Matches", message="""
                1. On \"Portfolio_ID\", set a blanks filter to true, then for each visible record, star the row with the title (and KBID) that matches the portfolio.
                2. Copy the JSONs in the next two dialog boxes and apply them to the Alma project in OpenRefine.
            """) #ToDo: Figure out why last item in Find_Title_Matches_5.json works only when it's the last item in a JSON
            GUI.CreateJSONDisplay('Find_Title_Matches_5.json')
            GUI.CreateJSONDisplay('Find_Title_Matches_6.json')
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
            #ToDo: GUI.CreateJSONDisplay with f-string plus Move_Data_From_Temp.json
            """
            [
                {{
                    "op": "core/column-addition",
                    "engineConfig": {{
                        "facets": [
                            {{
                                "type": "list",
                                "name": "Portfolio_ID",
                                "expression": "isBlank(value)",
                                "columnName": "Portfolio_ID",
                                "invert": false,
                                "omitBlank": false,
                                "omitError": false,
                                "selection": [
                                    {{
                                        "v": {{
                                            "v": true,
                                            "l": "true"
                                        }}
                                    }}
                                ],
                                "selectBlank": false,
                                "selectError": false
                            }}
                        ],
                        "mode": "record-based"
                    }},
                    "baseColumnName": "KBID",
                    "expression": "grel:cell.cross(\\\"{Alma_project}\\\",\\\"KBID\\\").cells.Portfolio_ID.value.uniques().join(\\\"|\\\")",
                    "onError": "set-to-blank",
                    "newColumnName": "temp",
                    "columnInsertIndex": 1,
                    "description": "For records without portfolio IDs, create column ``temp`` with all the portfolio IDs matching the KBID separated by pipes"
                }}
            ]
            """


    #Section: Compare Data for Individual Holdings
    messagebox.showinfo(title="Instructions: Compare Holdings", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
    #ToDo: GUI.CreateJSONDisplay with f-string, Compare_Holdings_Data.json
    """
    [
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.Title.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_Title",
            "columnInsertIndex": 4,
            "description": "Create column ``HM_Title`` with the title for the KBID"
        }},
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.ISSN.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_ISSN",
            "columnInsertIndex": 6,
            "description": "Create column ``HM_ISSN`` with the ISSNs for the KBID"
        }},
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.Local_Start_Date.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_Local_Start_Date",
            "columnInsertIndex": 8,
            "description": "Create column ``HM_Local_Start_Date`` with the local/custom start date for the KBID"
        }},
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.Local_End_Date.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_Local_End_Date",
            "columnInsertIndex": 10,
            "description": "Create column ``HM_Local_End_Date`` with the local/custom end date for the KBID"
        }},
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.Local_Embargo.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_Local_Embargo",
            "columnInsertIndex": 12,
            "description": "Create column ``HM_Local_Embargo`` with the local/custom embargo for the KBID"
        }},
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.Default_Start_Date.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_Default_Start_Date",
            "columnInsertIndex": 14,
            "description": "Create column ``HM_Default_Start_Date`` with the default/global start date for the KBID"
        }},
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.Default_End_Date.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_Default_End_Date",
            "columnInsertIndex": 16,
            "description": "Create column ``HM_Default_End_Date`` with the default/global end date for the KBID"
        }},
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.Default_Embargo.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_Default_Embargo",
            "columnInsertIndex": 18,
            "description": "Create column ``HM_Default_Embargo`` with the global/default embargo for the KBID"
        }},
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.Publisher.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_Publisher",
            "columnInsertIndex": 22,
            "description": "Create column ``HM_Publisher`` with the publisher for the KBID"
        }},
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.URL.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_URL",
            "columnInsertIndex": 25,
            "description": "Create column ``HM_URL`` with the URL for the KBID"
        }},
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.DOI.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_DOI",
            "columnInsertIndex": 26,
            "description": "Create column ``HM_DOI`` with the DOI for the KBID"
        }},
        {{
            "op": "core/column-addition",
            "engineConfig": {{
                "facets": [],
                "mode": "record-based"
            }},
            "baseColumnName": "KBID",
            "expression": "grel:cell.cross(\\\"{HM_project}\\\",\\\"KBID\\\").cells.Resource_Type.value[0]",
            "onError": "set-to-blank",
            "newColumnName": "HM_Resource_Type",
            "columnInsertIndex": 28,
            "description": "Create column ``HM_Resource_Type`` with the resource type for the KBID"
        }}
    ]
    """
    messagebox.showinfo(title="Instructions: Evaluate Unmatched Titles", message="""
        1. In Alma project, set blanks filter on \"KBID\" to true to find unmatched portfolios
        2. In HM project, set blanks filter on \"Portfolio_ID\" to true to find unmatched titles
    """)