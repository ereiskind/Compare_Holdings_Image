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
    GUI.CreateJSONDisplay("""
[
    {
        "op": "core/column-rename",
        "oldColumnName": "ï»¿KBID",
        "newColumnName": "KBID",
        "description": "Rename column ``ï»¿KBID`` to ``KBID``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "﻿KBID",
        "newColumnName": "KBID",
        "description": "Rename column ``﻿KBID``, where the unknown character image doesn't appear in OpenRefine, to ``KBID``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "ManagedCoverageBegin",
        "newColumnName": "Default_Start_Date",
        "description": "Rename column ``ManagedCoverageBegin`` to ``Default_Start_Date``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "ManagedCoverageEnd",
        "newColumnName": "Default_End_Date",
        "description": "Rename column ``ManagedCoverageEnd`` to ``Default_End_Date``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "CustomCoverageBegin",
        "newColumnName": "Local_Start_Date",
        "description": "Rename column ``CustomCoverageBegin`` to ``Local_Start_Date``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "CustomCoverageEnd",
        "newColumnName": "Local_End_Date",
        "description": "Rename column ``CustomCoverageEnd`` to ``Local_End_Date``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "Embargo",
        "newColumnName": "Default_Embargo",
        "description": "Rename column ``Embargo`` to ``Default_Embargo``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "CustomEmbargo",
        "newColumnName": "Local_Embargo",
        "description": "Rename column ``CustomEmbargo`` to ``Local_Embargo``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "ResourceType",
        "newColumnName": "Resource_Type",
        "description": "Rename column ``ResourceType`` to ``Resource_Type``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "AlternateTitle",
        "newColumnName": "All_Titles",
        "description": "Rename column ``AlternateTitle`` to ``All_Titles``"
    },
    {
        "op": "core/text-transform",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "columnName": "All_Titles",
        "expression": "grel:if(value.split(\\\"|\\\").inArray(cells.Title.value),value,cells.Title.value+\\\"|\\\"+value)",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Add value in ``Title`` to ``All_Titles`` if not already there"
    },
    {
        "op": "core/text-transform",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "columnName": "Default_Start_Date",
        "expression": "grel:if(value.contains(\\\"|\\\"),forEach(value.split(\\\"|\\\"),value,if(value==\\\"Present\\\",value,value.toDate())).join(\\\"|\\\"),if(value==\\\"Present\\\",value,value.toDate()))",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Text transform on cells in column ``Default_Start_Date`` to turn single date strings into date data types and format dates in multi-date entries as date data types"
    },
    {
        "op": "core/text-transform",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "columnName": "Default_End_Date",
        "expression": "grel:if(value.contains(\\\"|\\\"),forEach(value.split(\\\"|\\\"),value,if(value==\\\"Present\\\",value,value.toDate())).join(\\\"|\\\"),if(value==\\\"Present\\\",value,value.toDate()))",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Text transform on cells in column ``Default_End_Date`` to turn single date strings into date data types and format dates in multi-date entries as date data types"
    },
    {
        "op": "core/text-transform",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "columnName": "Local_Start_Date",
        "expression": "grel:if(value.contains(\\\"|\\\"),forEach(value.split(\\\"|\\\"),value,if(value==\\\"Present\\\",value,value.toDate())).join(\\\"|\\\"),if(value==\\\"Present\\\",value,value.toDate()))",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Text transform on cells in column ``Local_Start_Date`` to turn single date strings into date data types and format dates in multi-date entries as date data types"
    },
    {
        "op": "core/text-transform",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "columnName": "Local_End_Date",
        "expression": "grel:if(value.contains(\\\"|\\\"),forEach(value.split(\\\"|\\\"),value,if(value==\\\"Present\\\",value,value.toDate())).join(\\\"|\\\"),if(value==\\\"Present\\\",value,value.toDate()))",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Text transform on cells in column ``Local_End_Date`` to turn single date strings into date data types and format dates in multi-date entries as date data types"
    },
    {
        "op": "core/column-reorder",
        "columnNames": [
            "KBID",
            "PrintISSN",
            "OnlineISSN",
            "Title",
            "All_Titles",
            "PackageName",
            "URL",
            "DOI",
            "Publisher",
            "Default_Start_Date",
            "Default_End_Date",
            "Local_Start_Date",
            "Local_End_Date",
            "Default_Embargo",
            "Local_Embargo",
            "Resource_Type"
        ],
        "description": "Reorder columns, removing unneeded columns"
    },
    {
        "op": "core/transpose-columns-into-rows",
        "combinedColumnName": "ISSN",
        "startColumnName": "PrintISSN",
        "columnCount": 2,
        "ignoreBlankCells": true,
        "fillDown": false,
        "prependColumnName": false,
        "separator": ":",
        "keyColumnName": null,
        "valueColumnName": null,
        "description": "Transpose all ISSN values into one new column named ``ISSN``"
    },
    {
        "op": "core/fill-down",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "columnName": "KBID",
        "description": "Fill down cells in column ``KBID``"
    }
]
    """)
    messagebox.showinfo(title="Instructions: Reformat Alma Title List", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
    GUI.CreateJSONDisplay("""
[
    {
        "op": "core/column-rename",
        "oldColumnName": "PORTFOLIO_PID",
        "newColumnName": "Portfolio_ID",
        "description": "Rename column ``PORTFOLIO_PID`` to ``Portfolio_ID``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "MMS",
        "newColumnName": "MMS (Title ID)",
        "description": "Rename column ``MMS`` to ``MMS (Title ID)``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "TITLE",
        "newColumnName": "Title",
        "description": "Rename column ``TITLE`` to ``Title``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "WARNINGS",
        "newColumnName": "Other_Coverage_Notices",
        "description": "Rename column ``WARNINGS`` to ``Other_Coverage_Notices``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "PUBLISHER",
        "newColumnName": "Publisher",
        "description": "Rename column ``PUBLISHER`` to ``Publisher``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "PARSER_PARAMETERS",
        "newColumnName": "URL_Identifier",
        "description": "Rename column ``PARSER_PARAMETERS`` to ``URL_Identifier``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "ELECTRONIC_MATERIAL_TYPE",
        "newColumnName": "Resource_Type",
        "description": "Rename column ``ELECTRONIC_MATERIAL_TYPE`` to ``Resource_Type``"
    },
    {
        "op": "core/column-rename",
        "oldColumnName": "COVERAGE_STATEMENT",
        "newColumnName": "Selected_Coverage_Statement",
        "description": "Rename column COVERAGE_STATEMENT to Selected_Coverage_Statement"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "baseColumnName": "FROM_YEAR",
        "expression": "grel:toDate(value+\\\"-\\\"+if(isNotNull(cells.FROM_MONTH.value),cells.FROM_MONTH.value,\\\"01\\\")+\\\"-\\\"+if(isNotNull(cells.FROM_DAY.value),cells.FROM_DAY.value,\\\"01\\\"))",
        "onError": "set-to-blank",
        "newColumnName": "Local_Start_Date",
        "columnInsertIndex": 14,
        "description": "Create column ``Local_Start_Date`` by combining the available year, month, and day columns for the local subscription start date as a date data type"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "baseColumnName": "TO_YEAR",
        "expression": "grel:toDate(value+\\\"-\\\"+if(isNotNull(cells.TO_MONTH.value),cells.TO_MONTH.value,\\\"01\\\")+\\\"-\\\"+if(isNotNull(cells.TO_DAY.value),cells.TO_DAY.value,\\\"01\\\"))",
        "onError": "set-to-blank",
        "newColumnName": "Local_End_Date",
        "columnInsertIndex": 16,
        "description": "Create column ``Local_End_Date`` by combining the available year, month, and day columns for the local subscription end date as a date data type"
    },
    {
        "op": "core/text-transform",
        "engineConfig": {
            "facets": [
                {
                    "type": "list",
                    "name": "Local_Start_Date",
                    "expression": "isBlank(value)",
                    "columnName": "Local_Start_Date",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {
                            "v": {
                                "v": false,
                                "l": "false"
                            }
                        }
                    ],
                    "selectBlank": false,
                    "selectError": false
                }
            ],
            "mode": "record-based"
        },
        "columnName": "Local_End_Date",
        "expression": "grel:if(isNull(value),\\\"Present\\\",value)",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "For titles that have a custom/local start date but no corresponding ending date, change the null values in column ``Local_End_Date``  to `Present`"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "baseColumnName": "PUBLICATION_DATE_OPERATOR",
        "expression": "grel:if(isNull(value),null,if(value==\\\">\\\",\\\"Excludes the most recent \\\",\\\"Only the most recent \\\")+((cells.PUBLICATION_DATE_YEAR.value.toNumber()*12)+cells.PUBLICATION_DATE_MONTH.value.toNumber())+\\\" months\\\"+if(value.contains(\\\"=\\\"),\\\"(inclusive of today)\\\",\\\"\\\"))",
        "onError": "set-to-blank",
        "newColumnName": "Local_Embargo",
        "columnInsertIndex": 29,
        "description": "Create column ``Local_Embargo`` based off the columns for the embargo type and the years and months in the embargo for the local embargo length in months"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "baseColumnName": "GLOBAL_FROM_YEAR",
        "expression": "grel:toDate(value+\\\"-\\\"+if(isNotNull(cells.GLOBAL_FROM_MONTH.value),cells.GLOBAL_FROM_MONTH.value,\\\"01\\\")+\\\"-\\\"+if(isNotNull(cells.GLOBAL_FROM_DAY.value),cells.GLOBAL_FROM_DAY.value,\\\"01\\\"))",
        "onError": "set-to-blank",
        "newColumnName": "Default_Start_Date",
        "columnInsertIndex": 32,
        "description": "Create column ``Default_Start_Date`` by combining the available year, month, and day columns for the default/global subscription start date as a date data type"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "baseColumnName": "GLOBAL_TO_YEAR",
        "expression": "grel:toDate(value+\\\"-\\\"+if(isNotNull(cells.GLOBAL_TO_MONTH.value),cells.GLOBAL_TO_MONTH.value,\\\"01\\\")+\\\"-\\\"+if(isNotNull(cells.GLOBAL_TO_DAY.value),cells.GLOBAL_TO_DAY.value,\\\"01\\\"))",
        "onError": "set-to-blank",
        "newColumnName": "Default_End_Date",
        "columnInsertIndex": 32,
        "description": "Create column ``Default_End_Date`` by combining the available year, month, and day columns for the default/global subscription end date as a date data type"
    },
    {
        "op": "core/text-transform",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "columnName": "Default_End_Date",
        "expression": "grel:if(isNull(value),\\\"Present\\\",value)",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Change null values in column ``Default_End_Date``  to `Present`"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "baseColumnName": "GLOBAL_PUBLICATION_DATE_OPERATOR",
        "expression": "grel:if(isNull(value),null,if(value==\\\">\\\",\\\"Excludes the most recent \\\",\\\"Only the most recent \\\")+((cells.GLOBAL_PUBLICATION_DATE_YEAR.value.toNumber()*12)+cells.GLOBAL_PUBLICATION_DATE_MONTH.value.toNumber())+\\\" months\\\"+if(value.contains(\\\"=\\\"),\\\"(inclusive of today)\\\",\\\"\\\"))",
        "onError": "set-to-blank",
        "newColumnName": "Default_Embargo",
        "columnInsertIndex": 44,
        "description": "Create column ``Default_Embargo`` based off the columns for the embargo type and the years and months in the embargo for the default/global embargo length in months"
    },
    {
        "op": "core/column-reorder",
        "columnNames": [
            "Portfolio_ID",
            "MMS (Title ID)",
            "Title",
            "ISSN",
            "ISSN2",
            "ISSN3",
            "Local_Start_Date",
            "Local_End_Date",
            "Local_Embargo",
            "Default_Start_Date",
            "Default_End_Date",
            "Default_Embargo",
            "Selected_Coverage_Statement",
            "Other_Coverage_Notices",
            "Publisher",
            "URL",
            "URL_Identifier",
            "Resource_Type"
        ],
        "description": "Reorder columns, removing unneeded columns"
    },
    {
        "op": "core/transpose-columns-into-rows",
        "combinedColumnName": "All ISSN",
        "startColumnName": "ISSN",
        "columnCount": 3,
        "ignoreBlankCells": true,
        "fillDown": false,
        "prependColumnName": false,
        "separator": ":",
        "keyColumnName": null,
        "valueColumnName": null,
        "description": "Transpose all ISSN values into one new column named ``All ISSN``"
    }
]
    """)


    #Section: Find Title Matches in the Two Projects
    #Subsection: Find ISSN Matches
    messagebox.showinfo(title="Instructions: Find ISSN Matches", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
    GUI.CreateJSONDisplay(f"""
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
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "columnName": "KBID",
        "expression": "grel:if(filter(row.record.cells[\\\"KBID\\\"].value,ID,ID==row.record.cells[\\\"KBID\\\"].value[0]).length()==row.record.cells[\\\"KBID\\\"].value.length(),if(row.index-row.record.fromRowIndex==0,if(isError(row.record.cells[\\\"KBID\\\"].value[0]),row.record.cells[\\\"Portfolio_ID\\\"].value[0]+\\\"-\\\"+toString(row.index-row.record.fromRowIndex),row.record.cells[\\\"KBID\\\"].value[0]),row.record.cells[\\\"Portfolio_ID\\\"].value[0]+\\\"-\\\"+toString(row.index-row.record.fromRowIndex)),row.record.cells[\\\"Portfolio_ID\\\"].value[0]+\\\"-\\\"+toString(row.index-row.record.fromRowIndex))",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Change values in column ``KBID`` so if the ISSNs for a record all had the same KBID match, the KBID(s) appears in the first row of the record and all other rows have the record's portfolio ID and the number of the row in the record, but if the ISSNs in a record match to multiple KBID(s) or don't match to anything, all the rows in the record have the record's portfolio ID and the number of the row in the record"
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "columnName": "KBID",
        "expression": "grel:if(value.contains(\\\"-\\\"),null,value)",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Null values in ``KBID`` containing a hyphen"
    }},
    {{
        "op": "core/multivalued-cell-join",
        "columnName": "All ISSN",
        "keyColumnName": "Portfolio_ID",
        "separator": "|",
        "description": "Combine all values in column ``All ISSN`` in the first row of the record divided by pipes"
    }}
]
    """) 
    messagebox.showinfo(title="Instructions: Find ISSN Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
    GUI.CreateJSONDisplay(f"""
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
    }},
    {{
        "op": "core/blank-down",
        "engineConfig": {{
            "facets": [],
            "mode": "row-based"
        }},
        "columnName": "KBID",
        "description": "Blank down cells in column ``KBID``"
    }},
    {{
        "op": "core/blank-down",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "columnName": "Portfolio_ID",
        "description": "Blank down cells in column ``Portfolio_ID``"
    }},
    {{
        "op": "core/multivalued-cell-join",
        "columnName": "ISSN",
        "keyColumnName": "KBID",
        "separator": "|",
        "description": "Combine all values in column ``ISSN`` in the first row of the record divided by pipes"
    }}
]
""") 
    if messagebox.askyesno(title="Instructions", message="Switch to the Alma project and set a blanks facet on column \\\"KBID\\\". Are there blank rows remaining?"):
        
        #Subsection: Find URL Identifier Matches
        messagebox.showinfo(title="Instructions: Find URL Identifier Matches", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
        GUI.CreateJSONDisplay(f"""
[
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "columnName": "URL_Identifier",
        "expression": "grel:value.match(/jkey=(.*)/)[0].unescape(\\\"url\\\")",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Remove parameter key `jkey` and unescape URL encodings in column ``URL_Identifier``"
    }},
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
    }},
    {{
        "op": "core/text-transform",
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
        "columnName": "KBID",
        "expression": "grel:cells.URL_Match.value",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "In records with no KBID, add values from ``URL_Match`` into column ``KBID``"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "URL_Match",
        "description": "Remove column ``URL_Match``"
    }}
]
        """)
        messagebox.showinfo(title="Instructions: Find URL Identifier Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
        GUI.CreateJSONDisplay(f"""
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
    }},
    {{
        "op": "core/text-transform",
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
                }},
                {{
                    "type": "list",
                    "name": "temp",
                    "expression": "isBlank(value)",
                    "columnName": "temp",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {{
                            "v": {{
                                "v": false,
                                "l": "false"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }}
            ],
            "mode": "record-based"
        }},
        "columnName": "Portfolio_ID",
        "expression": "grel:cells.temp.value",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "For records with no ID in ``Portfolio_ID`` but values in ``temp``, add the value from the latter column to the former"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "temp",
        "description": "Remove column ``temp``"
    }}
]
        """)
        if messagebox.askyesno(title="Instructions", message="Switch to the Alma project and set a blanks facet on column \\\"KBID\\\". Are there blank rows remaining?"):
            
            #Subsection: Find Remaining Matches via Title Matching
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
            GUI.CreateJSONDisplay("""
[
    {
        "op": "core/text-transform",
        "engineConfig": {
            "facets": [
                {
                    "type": "list",
                    "name": "Portfolio_ID",
                    "expression": "isBlank(value)",
                    "columnName": "Portfolio_ID",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {
                            "v": {
                                "v": false,
                                "l": "false"
                            }
                        }
                    ],
                    "selectBlank": false,
                    "selectError": false
                }
            ],
            "mode": "record-based"
        },
        "columnName": "All_Titles",
        "expression": "null",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Null values in column ``All_Titles`` in records already matched to an Alma portfolio"
    },
    {
        "op": "core/multivalued-cell-split",
        "columnName": "All_Titles",
        "keyColumnName": "KBID",
        "mode": "separator",
        "separator": "|",
        "regex": false,
        "description": "Split values in column ``All_Titles`` into new rows at pipes"
    },
    {
        "op": "core/text-transform",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "columnName": "All_Titles",
        "expression": "value.trim()",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Trim extra spaces from column ``All_Titles``"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "baseColumnName": "All_Titles",
        "expression": "grel:value.trim().split(\\\"(\\\")[0].split(\\\":\\\")[0].trim()",
        "onError": "set-to-blank",
        "newColumnName": "Alt_Titles",
        "columnInsertIndex": 5,
        "description": "Create column ``Alt_Titles`` by removing subtitles and parenthetical from ``All_Titles``"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "baseColumnName": "All_Titles",
        "expression": "value.replace(/[‘’‚‛‹›‚]/,\\\"\\'\\\").replace(/[“”«»„]/,\\\"\\\\\"\\\")",
        "onError": "set-to-blank",
        "newColumnName": "All_Titles_1",
        "columnInsertIndex": 5,
        "description": "Create column ``All_Titles_1`` by replacing smart quotes in column ``All_Titles``"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "baseColumnName": "Alt_Titles",
        "expression": "value.replace(/[‘’‚‛‹›‚]/,\\\"\\'\\\").replace(/[“”«»„]/,\\\"\\\\\"\\\")",
        "onError": "set-to-blank",
        "newColumnName": "Alt_Titles_1",
        "columnInsertIndex": 5,
        "description": "Create column ``Alt_Titles_1`` by replacing smart quotes in column ``Alt_Titles``"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "baseColumnName": "All_Titles_1",
        "expression": "grel:if(isNull(value.match(/^(The|the|An|an|A|a)\\s(.*)/)),value,value.match(/^(The|the|An|an|A|a)\\s(.*)/)[1])",
        "onError": "set-to-blank",
        "newColumnName": "All_Titles_2",
        "columnInsertIndex": 5,
        "description": "Create column ``All_Titles_2`` by removing `A`, `An`, and `The` from the beginning of ``All_Titles_1``"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "baseColumnName": "Alt_Titles_1",
        "expression": "grel:if(isNull(value.match(/^(The|the|An|an|A|a)\\s(.*)/)),value,value.match(/^(The|the|An|an|A|a)\\s(.*)/)[1])",
        "onError": "set-to-blank",
        "newColumnName": "Alt_Titles_2",
        "columnInsertIndex": 5,
        "description": "Create column ``Alt_Titles_2`` by removing `A`, `An`, and `The` from the beginning of ``Alt_Titles_1``"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "baseColumnName": "All_Titles_2",
        "expression": "value.replace(\\\"-\\\",\\\" \\\").replace(\\\"&\\\",\\\"And\\\").toTitlecase()",
        "onError": "set-to-blank",
        "newColumnName": "All_Titles_3",
        "columnInsertIndex": 5,
        "description": "Create column ``All_Titles_3`` by by changing ``All_Titles_2``so the titles are in titlecase with hyphens replaced by spaces and ampersands replaced by `And`"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "baseColumnName": "Alt_Titles_2",
        "expression": "value.replace(\\\"-\\\",\\\" \\\").replace(\\\"&\\\",\\\"And\\\").toTitlecase()",
        "onError": "set-to-blank",
        "newColumnName": "Alt_Titles_3",
        "columnInsertIndex": 5,
        "description": "Create column ``Alt_Titles_3`` by by changing ``Alt_Titles_2``so the titles are in titlecase with hyphens replaced by spaces and ampersands replaced by `And`"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "baseColumnName": "All_Titles_3",
        "expression": "grel:value.replace(\\\".\\\",\\\"\\\").replace(\\\",\\\",\\\"\\\").trim()",
        "onError": "set-to-blank",
        "newColumnName": "All_Titles_4",
        "columnInsertIndex": 5,
        "description": "Create column ``All_Titles_4`` by by changing ``All_Titles_3``to remove periods and commas"
    },
    {
        "op": "core/column-addition",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "baseColumnName": "Alt_Titles_3",
        "expression": "grel:value.replace(\\\".\\\",\\\"\\\").replace(\\\",\\\",\\\"\\\").trim()",
        "onError": "set-to-blank",
        "newColumnName": "Alt_Titles_4",
        "columnInsertIndex": 5,
        "description": "Create column ``Alt_Titles_4`` by by changing ``Alt_Titles_3``to remove periods and commas"
    },
    {
        "op": "core/fill-down",
        "engineConfig": {
            "facets": [],
            "mode": "record-based"
        },
        "columnName": "KBID",
        "description": "Fill down cells in column ``KBID``"
    }
]
            """)
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
            GUI.CreateJSONDisplay(f"""
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
        "baseColumnName": "Title",
        "expression": "value.replace(/[‘’‚‛‹›‚]/,\\\"\\'\\\").replace(/[“”«»„]/,\\\"\\\\\"\\\").trim()",
        "onError": "set-to-blank",
        "newColumnName": "All_1",
        "columnInsertIndex": 5,
        "description": "In records not matched to a HM record, create column ``All_1`` with the value of ``Title`` without smart quotes and trimmed for all records not already matched"
    }},
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
        "baseColumnName": "All_1",
        "expression": "grel:value.split(\\\"(\\\")[0].split(\\\":\\\")[0].trim()",
        "onError": "set-to-blank",
        "newColumnName": "Alt_1",
        "columnInsertIndex": 5,
        "description": "In records not matched to a HM record, create column ``Alt_1`` with the value of ``All_1`` without subtitles or parenthetical"
    }},
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
        "baseColumnName": "All_1",
        "expression": "grel:if(isNull(value.match(/^(The|the|An|an|A|a)\\s(.*)/)),value,value.match(/^(The|the|An|an|A|a)\\s(.*)/)[1])",
        "onError": "set-to-blank",
        "newColumnName": "All_2",
        "columnInsertIndex": 5,
        "description": "In records not matched to a HM record, create column ``All_2`` by removing `A`, `An`, and `The` from the beginning of `All_1`"
    }},
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
        "baseColumnName": "All_2",
        "expression": "grel:value.split(\\\"(\\\")[0].split(\\\":\\\")[0].trim()",
        "onError": "set-to-blank",
        "newColumnName": "Alt_2",
        "columnInsertIndex": 5,
        "description": "In records not matched to a HM record, create column ``Alt_2`` with the value of ``All_2`` without subtitles or parenthetical"
    }},
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
        "baseColumnName": "All_2",
        "expression": "value.replace(\\\"-\\\",\\\" \\\").replace(\\\"&\\\",\\\"And\\\").toTitlecase()",
        "onError": "set-to-blank",
        "newColumnName": "All_3",
        "columnInsertIndex": 5,
        "description": "In records not matched to a HM record, create column ``All_3`` with the value of ``All_2`` in titlecase with hyphens replaced by spaces and ampersands replaced by `And`"
    }},
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
        "baseColumnName": "All_3",
        "expression": "grel:value.split(\\\"(\\\")[0].split(\\\":\\\")[0].trim()",
        "onError": "set-to-blank",
        "newColumnName": "Alt_3",
        "columnInsertIndex": 5,
        "description": "In records not matched to a HM record, create column ``Alt_3`` with the value of ``All_3`` without subtitles or parenthetical"
    }},
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
        "baseColumnName": "All_3",
        "expression": "grel:value.replace(\\\".\\\",\\\"\\\").replace(\\\",\\\",\\\"\\\").trim()",
        "onError": "set-to-blank",
        "newColumnName": "All_4",
        "columnInsertIndex": 5,
        "description": "In records not matched to a HM record, create column ``All_4`` with the value of ``All_3`` without periods or commas"
    }},
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
        "baseColumnName": "All_4",
        "expression": "grel:value.split(\\\"(\\\")[0].split(\\\":\\\")[0].trim()",
        "onError": "set-to-blank",
        "newColumnName": "Alt_4",
        "columnInsertIndex": 5,
        "description": "In records not matched to a HM record, create column ``Alt_4`` with the value of ``All_4`` without subtitles or parenthetical"
    }},
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
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "columnName": "Title_KBID",
        "expression": "grel:if(isNotNull(cells.KBID.value),cells.KBID.value,value)",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Add values in column ``KBID`` to column ``Title_KBID``"
    }},
    {{
        "op": "core/text-transform",
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
                }},
                {{
                    "type": "list",
                    "name": "Title_KBID",
                    "expression": "grel:value.contains(\\\"|\\\")",
                    "columnName": "Title_KBID",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {{
                            "v": {{
                                "v": false,
                                "l": "false"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }},
                {{
                    "type": "list",
                    "name": "Title_KBID",
                    "expression": "facetCount(value, 'value', 'Title_KBID') > 1",
                    "columnName": "Title_KBID",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {{
                            "v": {{
                                "v": false,
                                "l": "false"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }}
            ],
            "mode": "record-based"
        }},
        "columnName": "KBID",
        "expression": "grel:cells.Title_KBID.value",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "In records with no KBID, if ``Title_KBID`` is a single unique KBID, add the ``Title_KBID`` value to ``KBID``"
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "columnName": "All_1",
        "expression": "grel:split(if(isNull(value),\\\"\\\",value)+if(isNull(cells.All_2.value),\\\"\\\",\\\"|\\\"+cells.All_2.value)+if(isNull(cells.All_3.value),\\\"\\\",\\\"|\\\"+cells.All_3.value)+if(isNull(cells.All_4.value),\\\"\\\",\\\"|\\\"+cells.All_4.value),\\\"|\\\").uniques().join(\\\"|\\\")",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Move all KBIDs found by matching titles with subtitles to column ``All_1``, keeping the KBIDs separated by pipes"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "All_2",
        "description": "Remove column ``All_2``"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "All_3",
        "description": "Remove column ``All_3``"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "All_4",
        "description": "Remove column ``All_4``"
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "columnName": "All_1",
        "expression": "grel:if(isNotNull(cells.KBID.value),cells.KBID.value,value)",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Add values in column ``KBID`` to column ``All_1``"
    }},
    {{
        "op": "core/text-transform",
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
                }},
                {{
                    "type": "list",
                    "name": "All_1",
                    "expression": "facetCount(value, 'value', 'All_1') > 1",
                    "columnName": "All_1",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {{
                            "v": {{
                                "v": false,
                                "l": "false"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }},
                {{
                    "type": "list",
                    "name": "All_1",
                    "expression": "grel:value.contains(\\\"|\\\")",
                    "columnName": "All_1",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {{
                            "v": {{
                                "v": false,
                                "l": "false"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }}
            ],
            "mode": "record-based"
        }},
        "columnName": "KBID",
        "expression": "grel:cells.All_1.value",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "In records with no KBID, if ``All_1`` is a single unique KBID, add the ``All_1`` value to ``KBID``"
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "columnName": "Alt_1",
        "expression": "grel:split(if(isNull(value),\\\"\\\",value)+if(isNull(cells.Alt_2.value),\\\"\\\",\\\"|\\\"+cells.Alt_2.value)+if(isNull(cells.Alt_3.value),\\\"\\\",\\\"|\\\"+cells.Alt_3.value)+if(isNull(cells.Alt_4.value),\\\"\\\",\\\"|\\\"+cells.Alt_4.value),\\\"|\\\").uniques().join(\\\"|\\\")",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Move all KBIDs found by matching titles without subtitles to column ``Alt_1``, keeping the KBIDs separated by pipes"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "Alt_2",
        "description": "Remove column Alt_2"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "Alt_3",
        "description": "Remove column Alt_3"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "Alt_4",
        "description": "Remove column Alt_4"
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "columnName": "Alt_1",
        "expression": "grel:if(isNotNull(cells.KBID.value),cells.KBID.value,value)",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Add values in column ``KBID`` to column ``Alt_1``"
    }},
    {{
        "op": "core/text-transform",
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
                }},
                {{
                    "type": "list",
                    "name": "Alt_1",
                    "expression": "facetCount(value, 'value', 'Alt_1') > 1",
                    "columnName": "Alt_1",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {{
                            "v": {{
                                "v": false,
                                "l": "false"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }},
                {{
                    "type": "list",
                    "name": "Alt_1",
                    "expression": "grel:value.contains(\\\"|\\\")",
                    "columnName": "Alt_1",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {{
                            "v": {{
                                "v": false,
                                "l": "false"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }}
            ],
            "mode": "record-based"
        }},
        "columnName": "KBID",
        "expression": "grel:cells.Alt_1.value",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "In records with no KBID, if ``Alt_1`` is a single unique KBID, add the ``Alt_1`` value to ``KBID``"
    }},
    {{
        "op": "core/column-addition",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "baseColumnName": "Portfolio_ID",
        "expression": "grel:row.record.index",
        "onError": "set-to-blank",
        "newColumnName": "Order",
        "columnInsertIndex": 1,
        "description": "Create column ``Order`` with the number of the record in the project"
    }},
    {{
        "op": "core/column-addition",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "baseColumnName": "Title_KBID",
        "expression": "grel:if(isNotNull(cells.KBID.value),cells.KBID.value,if(isBlank(value),if(isBlank(cells.All_1.value),if(isBlank(cells.Alt_1.value),\\\"null-\\\"+cells.Order.value,cells.Alt_1.value),cells.All_1.value),value))",
        "onError": "set-to-blank",
        "newColumnName": "Temp",
        "columnInsertIndex": 0,
        "description": "Create column ``Temp`` as new starting column with KBIDs taken from the ``KBID``, ``Title_KBID``, ``All_1``, and ``Alt_1`` columns in that order with records still lacking a KBID value getting `null-` and the number of the record in the project"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "Title_KBID",
        "description": "Remove column ``Title_KBID``"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "All_1",
        "description": "Remove column All_1"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "Alt_1",
        "description": "Remove column Alt_1"
    }},
    {{
        "op": "core/row-reorder",
        "mode": "record-based",
        "sorting": {{
            "criteria": [
                {{
                    "valueType": "string",
                    "column": "Temp",
                    "blankPosition": 2,
                    "errorPosition": 1,
                    "reverse": false,
                    "caseSensitive": false
                }}
            ]
        }},
        "description": "Reorder rows based on ``Temp``"
    }},
    {{
        "op": "core/blank-down",
        "engineConfig": {{
            "facets": [],
            "mode": "row-based"
        }},
        "columnName": "Temp",
        "description": "Blank down cells in column ``Temp``"
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [
                {{
                    "type": "list",
                    "name": "KBID",
                    "expression": "isBlank(value)",
                    "columnName": "KBID",
                    "invert": true,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {{
                            "v": {{
                                "v": false,
                                "l": "false"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }}
            ],
            "mode": "record-based"
        }},
        "columnName": "KBID",
        "expression": "grel:if(row.index-row.record.fromRowIndex==0,if(or(cells.Temp.value.contains(\\\"|\\\"),cells.Temp.value.contains(\\\"-\\\")),value,cells.Temp.value),value)",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "In records where ``KBID`` is null in all rows, if ``Temp`` is a single KBID, add that KBID to ``KBID``"
    }},
    {{
        "op": "core/text-transform",
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
                                "v": false,
                                "l": "false"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }},
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
        "columnName": "KBID",
        "expression": "grel:row.record.cells[\\\"KBID\\\"].value[0]",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "In records where only some rows have values in ``KBID``, fill up and down values in column ``KBID``"
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "columnName": "Temp",
        "expression": "grel:if(filter(row.record.cells[\\\"Temp\\\"].value,bool,bool.contains(\\\"|\\\")).length()>0,row.record.cells[\\\"Temp\\\"].value[0],cells.Order.value)",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "In column ``Temp``, in records with multiple KBIDs separated by pipes, fill up and down the KBIDs, otherwise, replace with the value in ``Order``"
    }},
    {{
        "op": "core/row-reorder",
        "mode": "record-based",
        "sorting": {{
            "criteria": [
                {{
                    "valueType": "number",
                    "column": "Order",
                    "blankPosition": 2,
                    "errorPosition": 1,
                    "reverse": false
                }}
            ]
        }},
        "description": "Reorder rows based on ``Order``"
    }},
    {{
        "op": "core/column-reorder",
        "columnNames": [
            "Portfolio_ID",
            "Order",
            "KBID",
            "MMS (Title ID)",
            "Title",
            "All ISSN",
            "Local_Start_Date",
            "Local_End_Date",
            "Local_Embargo",
            "Default_Start_Date",
            "Default_End_Date",
            "Default_Embargo",
            "Selected_Coverage_Statement",
            "Publisher",
            "URL",
            "URL_Identifier",
            "Resource_Type",
            "Temp"
        ],
        "description": "Reorder columns to put ``Portfolio_ID`` first and ``Temp`` last"
    }},
    {{
        "op": "core/column-split",
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
                                "v": false,
                                "l": "false"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }}
            ],
            "mode": "record-based"
        }},
        "columnName": "Temp",
        "guessCellType": false,
        "removeOriginalColumn": true,
        "mode": "separator",
        "separator": "|",
        "regex": false,
        "maxColumns": 0,
        "description": "In records with multiple possible KBID matches, split those KBIDs in column ``Temp`` at pipes into new columns"
    }},
    {{
        "op": "core/transpose-columns-into-rows",
        "combinedColumnName": "Temp",
        "startColumnName": "Temp 1",
        "columnCount": -1,
        "ignoreBlankCells": true,
        "fillDown": true,
        "prependColumnName": false,
        "separator": ":",
        "keyColumnName": null,
        "valueColumnName": null,
        "description": "Pivot all the columns created by separating ``Temp`` into a new column named ``Temp`` with any newly created rows getting data via filling down"
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "columnName": "Temp",
        "expression": "grel:if(isNull(value),\\\"z-\\\"+cells.Order.value,value)",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "Fill null cells in column ``Temp`` with `z`, a hyphen, and the value from ``Order``"
    }},
    {{
        "op": "core/column-move",
        "columnName": "Temp",
        "index": 1,
        "description": "Move column ``Temp`` to right after ``Portfolio_ID``"
    }},
    {{
        "op": "core/row-reorder",
        "mode": "record-based",
        "sorting": {{
            "criteria": [
                {{
                    "valueType": "string",
                    "column": "Portfolio_ID",
                    "blankPosition": 2,
                    "errorPosition": 1,
                    "reverse": false,
                    "caseSensitive": false
                }}
            ]
        }},
        "description": "Reorder rows based on ``Portfolio_ID``"
    }},
    {{
        "op": "core/blank-down",
        "engineConfig": {{
            "facets": [],
            "mode": "row-based"
        }},
        "columnName": "Portfolio_ID",
        "description": "Blank down cells in column ``Portfolio_ID``"
    }}
]
            """)
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
            GUI.CreateJSONDisplay("""
[
    {
        "op": "core/blank-down",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "columnName": "KBID",
        "description": "Blank down cells in column ``KBID``"
    },
    {
        "op": "core/column-reorder",
        "columnNames": [
            "KBID",
            "Portfolio_ID",
            "ISSN",
            "Title",
            "All_Titles",
            "PackageName",
            "URL",
            "DOI",
            "Publisher",
            "Default_Start_Date",
            "Default_End_Date",
            "Local_Start_Date",
            "Local_End_Date",
            "Default_Embargo",
            "Local_Embargo",
            "Resource_Type"
        ],
        "description": "Remove modified title columns"
    },
    {
        "op": "core/multivalued-cell-join",
        "columnName": "All_Titles",
        "keyColumnName": "KBID",
        "separator": "|",
        "description": "Combine all values in column ``All_Titles`` in the first row of the record divided by pipes"
    }
]
            """)
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
            GUI.CreateJSONDisplay(f"""
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
            """)
            messagebox.showinfo(title="Instructions: Find Title Matches", message="""
                1. On \\\"Portfolio_ID\\\", set a blanks filter to true, then for each visible record, star the row with the title (and KBID) that matches the portfolio.
                2. Copy the JSONs in the next two dialog boxes and apply them to the Alma project in OpenRefine.
            """) #ToDo: Figure out why last item in Find_Title_Matches_5.json works only when it's the last item in a JSON
            GUI.CreateJSONDisplay("""
[
    {
        "op": "core/column-removal",
        "columnName": "Temp_Titles",
        "description": "Remove column ``Temp_Titles``"
    },
    {
        "op": "core/fill-down",
        "engineConfig": {
            "facets": [],
            "mode": "row-based"
        },
        "columnName": "Portfolio_ID",
        "description": "Fill down cells in column ``Portfolio_ID``"
    },
    {
        "op": "core/row-removal",
        "engineConfig": {
            "facets": [
                {
                    "type": "list",
                    "name": "Order",
                    "expression": "facetCount(value, 'value', 'Order') > 1",
                    "columnName": "Order",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {
                            "v": {
                                "v": true,
                                "l": "true"
                            }
                        }
                    ],
                    "selectBlank": false,
                    "selectError": false
                },
                {
                    "type": "list",
                    "name": "Starred Rows",
                    "expression": "row.starred",
                    "columnName": "",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {
                            "v": {
                                "v": false,
                                "l": "false"
                            }
                        }
                    ],
                    "selectBlank": false,
                    "selectError": false
                }
            ],
            "mode": "row-based"
        },
        "description": "Remove rows representing portfolios matched to multiple KBIDs with the incorrect KBID"
    }
]
            """)
            GUI.CreateJSONDisplay("""
[
    {
        "op": "core/text-transform",
        "engineConfig": {
            "facets": [
                {
                    "type": "list",
                    "name": "Starred Rows",
                    "expression": "row.starred",
                    "columnName": "",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {
                            "v": {
                                "v": true,
                                "l": "true"
                            }
                        }
                    ],
                    "selectBlank": false,
                    "selectError": false
                }
            ],
            "mode": "row-based"
        },
        "columnName": "KBID",
        "expression": "grel:cells.Temp.value",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "For records where the KBID was just manually identified, move the value of ``Temp`` into ``KBID``"
    },
    {
        "op": "core/column-removal",
        "columnName": "Temp",
        "description": "Remove column ``Temp``"
    },
    {
        "op": "core/row-star",
        "engineConfig": {
            "facets": [
                {
                    "type": "list",
                    "name": "Starred Rows",
                    "expression": "row.starred",
                    "columnName": "",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {
                            "v": {
                                "v": true,
                                "l": "true"
                            }
                        }
                    ],
                    "selectBlank": false,
                    "selectError": false
                }
            ],
            "mode": "row-based"
        },
        "starred": false,
        "description": "Unstar rows"
    },
    {
        "op": "core/row-reorder",
        "mode": "row-based",
        "sorting": {
            "criteria": [
                {
                    "valueType": "number",
                    "column": "Order",
                    "blankPosition": 2,
                    "errorPosition": 1,
                    "reverse": false
                }
            ]
        },
        "description": "Reorder rows based on ``Order``"
    },
    {
        "op": "core/column-removal",
        "columnName": "Order",
        "description": "Remove column ``Order``"
    }
]
            """)
            messagebox.showinfo(title="Instructions: Find Title Matches", message="Copy the JSON in the next dialog box and apply it to the HM project in OpenRefine.")
            GUI.CreateJSONDisplay(f"""
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
    }},
    {{
        "op": "core/text-transform",
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
                }},
                {{
                    "type": "list",
                    "name": "temp",
                    "expression": "isBlank(value)",
                    "columnName": "temp",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {{
                            "v": {{
                                "v": false,
                                "l": "false"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }}
            ],
            "mode": "record-based"
        }},
        "columnName": "Portfolio_ID",
        "expression": "grel:cells.temp.value",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "For records with no ID in ``Portfolio_ID`` but values in ``temp``, add the value from the latter column to the former"
    }},
    {{
        "op": "core/column-removal",
        "columnName": "temp",
        "description": "Remove column ``temp``"
    }}
]
            """)


    #Section: Compare Data for Individual Holdings
    messagebox.showinfo(title="Instructions: Compare Holdings", message="Copy the JSON in the next dialog box and apply it to the Alma project in OpenRefine.")
    GUI.CreateJSONDisplay(f"""
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
    }},
    {{
        "op": "core/column-addition",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "baseColumnName": "HM_Local_Start_Date",
        "expression": "grel:if(isNull(value),cells.HM_Default_Start_Date.value,value)",
        "onError": "set-to-blank",
        "newColumnName": "EBSCO_Holdings_Start_Date",
        "columnInsertIndex": 7,
        "description": "Create column ``EBSCO_Holdings_Start_Date`` with the EBSCO custom/local holdings start date if there is one or the default holdings start date if there isn't"
    }},
    {{
        "op": "core/column-addition",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "baseColumnName": "Selected_Coverage_Statement",
        "expression": "grel:if(or(value==\\\"Global and local\\\",value==\\\"Global or local\\\"),if(cells.Default_Start_Date.value==cells.Local_Start_Date.value,cells.Default_Start_Date.value,cells.Default_Start_Date.value+\\\"|\\\"+cells.Local_Start_Date.value),if(value==\\\"Only local\\\",cells.Local_Start_Date.value,cells.Default_Start_Date.value))",
        "onError": "set-to-blank",
        "newColumnName": "Alma_Holdings_Start_Date",
        "columnInsertIndex": 8,
        "description": "Create column ``Alma_Holdings_Start_Date`` with the Alma custom/local and/or default/global holdings start date based on the ``Selected_Coverage_Statement`` value for the row, separating the dates with a pipe if both dates are indicated and the dates aren't the same"
    }},
    {{
        "op": "core/column-addition",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "baseColumnName": "HM_Local_End_Date",
        "expression": "grel:if(isNull(value),cells.HM_Default_End_Date.value,value)",
        "onError": "set-to-blank",
        "newColumnName": "EBSCO_Holdings_End_Date",
        "columnInsertIndex": 9,
        "description": "Create column ``EBSCO_Holdings_End_Date`` with the EBSCO custom/local holdings start date if there is one or the default/global holdings start date if there isn't"
    }},
    {{
        "op": "core/column-addition",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "baseColumnName": "Selected_Coverage_Statement",
        "expression": "grel:if(or(value==\\\"Global and local\\\",value==\\\"Global or local\\\"),if(cells.Default_End_Date.value==cells.Local_End_Date.value,cells.Default_End_Date.value,cells.Default_End_Date.value+\\\"|\\\"+cells.Local_End_Date.value),if(value==\\\"Only local\\\",cells.Local_End_Date.value,cells.Default_End_Date.value))",
        "onError": "set-to-blank",
        "newColumnName": "Alma_Holdings_End_Date",
        "columnInsertIndex": 10,
        "description": "Create column ``Alma_Holdings_End_Date`` with the Alma custom/local and/or default/global holdings end date based on the ``Selected_Coverage_Statement`` value for the row, separating the dates with a pipe if both are in the cell"
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [
                {{
                    "type": "list",
                    "name": "Other_Coverage_Notices",
                    "expression": "value",
                    "columnName": "Other_Coverage_Notices",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {{
                            "v": {{
                                "v": "Exports only the first coverage of the multiple coverages defined",
                                "l": "Exports only the first coverage of the multiple coverages defined"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }}
            ],
            "mode": "record-based"
        }},
        "columnName": "Alma_Holdings_Start_Date",
        "expression": "grel:value+\\\"|Other holdings range(s) not exported\\\"",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "For titles where ``Other_Coverage_Notices`` indicates other coverage ranges weren't downloaded, add a pipe and the message `Other holdings range(s) not exported` to the end of ``Alma_Holdings_Start_Date``"
    }},
    {{
        "op": "core/text-transform",
        "engineConfig": {{
            "facets": [
                {{
                    "type": "list",
                    "name": "Other_Coverage_Notices",
                    "expression": "value",
                    "columnName": "Other_Coverage_Notices",
                    "invert": false,
                    "omitBlank": false,
                    "omitError": false,
                    "selection": [
                        {{
                            "v": {{
                                "v": "Exports only the first coverage of the multiple coverages defined",
                                "l": "Exports only the first coverage of the multiple coverages defined"
                            }}
                        }}
                    ],
                    "selectBlank": false,
                    "selectError": false
                }}
            ],
            "mode": "record-based"
        }},
        "columnName": "Alma_Holdings_End_Date",
        "expression": "grel:value+\\\"|Other holdings range(s) not exported\\\"",
        "onError": "keep-original",
        "repeat": false,
        "repeatCount": 10,
        "description": "For titles where ``Other_Coverage_Notices`` indicates other coverage ranges weren't downloaded, add a pipe and the message `Other holdings range(s) not exported` to the end of ``Alma_Holdings_End_Date``"
    }},
    {{
        "op": "core/column-addition",
        "engineConfig": {{
            "facets": [],
            "mode": "record-based"
        }},
        "baseColumnName": "EBSCO_Holdings_Start_Date",
        "expression": "grel:if(and(value==cells.Alma_Holdings_Start_Date.value,cells.EBSCO_Holdings_End_Date.value==cells.Alma_Holdings_End_Date.value),forEachIndex(cells.EBSCO_Holdings_Start_Date.value.split(\\\"|\\\"),i,value,if(isError(value.toDate('yyyy-MM-dd')),value,value.toDate('yyyy-MM-dd').toString(\\\"yyyy-MM-dd\\\"))+\\\" to \\\"+if(isError(cells.Alma_Holdings_End_Date.value.split(\\\"|\\\")[i].toDate('yyyy-MM-dd')),cells.Alma_Holdings_End_Date.value.split(\\\"|\\\")[i],cells.Alma_Holdings_End_Date.value.split(\\\"|\\\")[i].toDate('yyyy-MM-dd').toString('yyyy-MM-dd'))).join(\\\"|\\\"),if(or(value==cells.Alma_Holdings_Start_Date.value,cells.EBSCO_Holdings_End_Date.value==cells.Alma_Holdings_End_Date.value),if(value==cells.Alma_Holdings_Start_Date.value,\\\"Start date match\\\",\\\"End date match\\\"),\\\"No match\\\"))",
        "onError": "set-to-blank",
        "newColumnName": "Holdings_Dates",
        "columnInsertIndex": 7,
        "description": "Create column ``Holdings_Dates`` with the start and end holdings dates separated by `to` if both the beginning and ending holdings dates match (with multiple ranges separated by pipes), `Start date match` or `End date match` if only one sets of dates match, and `No match` if neither set of dates match"
    }}
]
    """)
    messagebox.showinfo(title="Instructions: Evaluate Unmatched Titles", message="""
        1. In Alma project, set blanks filter on \\\"KBID\\\" to true to find unmatched portfolios
        2. In HM project, set blanks filter on \\\"Portfolio_ID\\\" to true to find unmatched titles
    """)